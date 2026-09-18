#!/usr/bin/env node
/**
 * Validate Membership Credentials against the rb-ds-membership SHACL shapes.
 *
 *   npm install                      # once, in this directory
 *   ./validate-membership.mjs credential.jsonld
 *   ./validate-membership.mjs --strict ../jsonld/sample-data/*.json
 *
 * Accepts W3C VCDM credentials in JSON-LD, or RDF in Turtle / N-Triples /
 * N-Quads. JSON-LD is converted to RDF with jsonld.js, a JSON-LD 1.1
 * processor. That matters: parsers without 1.1 support drop
 * attestationLegalCategory, because the vocabulary defines it inside a nested
 * scoped context, and the credential then fails validation for the wrong
 * reason.
 *
 * Exit status: 0 conforms, 1 violations found, 2 could not run.
 */

import rdf from '@zazuko/env-node'
import SHACLValidator from 'rdf-validate-shacl'
import jsonld from 'jsonld'
import { Readable } from 'node:stream'
import { readFile } from 'node:fs/promises'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const HERE = path.dirname(fileURLToPath(import.meta.url))
const CORE_SHAPES = path.join(HERE, 'ds-membership-shacl.ttl')

const SHACL = 'http://www.w3.org/ns/shacl#'
const EBWV = 'https://w3id.org/ebwv#'
const CRED = 'https://www.w3.org/2018/credentials#'
const NS = {
  member: `${EBWV}member`,
  onboardedBy: `${EBWV}onboardedBy`,
  identifier: `${EBWV}identifier`,
  legalIdentifier: `${EBWV}legalIdentifier`,
}

const RDF_MEDIA_TYPES = {
  '.ttl': 'text/turtle',
  '.nt': 'application/n-triples',
  '.nq': 'application/n-quads',
  '.n3': 'text/n3',
}

/** Parse a credential file into an RDF dataset. */
async function loadCredential(file) {
  const mediaType = RDF_MEDIA_TYPES[path.extname(file).toLowerCase()]
  if (mediaType) {
    return rdf.dataset().import(rdf.fromFile(file, { mediaType }))
  }
  const document = JSON.parse(await readFile(file, 'utf8'))
  const nquads = await jsonld.toRDF(document, { format: 'application/n-quads' })
  return parseNQuads(nquads)
}

async function parseNQuads(nquads) {
  const stream = rdf.formats.parsers.import(
    'application/n-quads',
    Readable.from([nquads]),
  )
  return rdf.dataset().import(stream)
}

/**
 * IR-06, which SHACL Core cannot express: the two values carry different
 * datatypes, an identifier scheme against ebwv:Euid or none at all, so
 * sh:equals and sh:disjoint compare RDF terms and cannot see a collision of
 * lexical forms. The companion graph
 * ds-membership-shacl-sparql.ttl states the same rule for SHACL-SPARQL engines.
 */
function checkIr06(dataset) {
  const findings = []
  const objects = (s, p) => [...dataset.match(s, rdf.namedNode(p))].map((q) => q.object)

  for (const { object: subject } of dataset.match(null, rdf.namedNode(`${CRED}credentialSubject`))) {
    for (const member of objects(subject, NS.member)) {
      const authoritative = objects(member, NS.legalIdentifier).map((t) => t.value)
      if (authoritative.length === 0) continue

      // the holder's further identifiers, wherever they are carried
      const candidates = [
        ...objects(member, NS.identifier).map((t) => [t, 'member.identifier']),
        ...objects(subject, NS.onboardedBy)
          .flatMap((o) => objects(o, NS.member))
          .flatMap((m) => objects(m, NS.identifier))
          .map((t) => [t, 'onboardedBy.member.identifier']),
      ]

      for (const [term, property] of candidates) {
        if (authoritative.includes(term.value)) {
          findings.push({
            severity: 'Violation',
            property,
            focus: subject.value,
            message: `IR-06: a value of ${property} must not repeat the value of member.legalIdentifier.`,
          })
        }
      }
    }
  }
  return findings
}

/**
 * Label a result by its property. A sequence or inverse path is a blank node
 * rather than a predicate IRI, so fall back to the sh:name the shape declares.
 */
function propertyLabel(result, shapes) {
  const path = result.path
  if (path?.termType === 'NamedNode') return path.value.split(/[#/]/).pop()
  const shape = result.sourceShape
  if (shape) {
    for (const { object } of shapes.match(shape, rdf.namedNode(`${SHACL}name`))) {
      return object.value
    }
  }
  return '-'
}

/** Turn a SHACL ValidationResult into a flat finding, keeping only leaves. */
function toFinding(result, shapes) {
  return {
    severity: (result.severity?.value ?? '').split('#').pop() || 'Violation',
    property: propertyLabel(result, shapes),
    focus: result.focusNode?.termType === 'BlankNode'
      ? `_:${result.focusNode.value}`
      : (result.focusNode?.value ?? '-'),
    message: result.message.map((m) => m.value).join(' '),
  }
}

/**
 * A sh:node constraint reports a generic result at the outer level and hangs
 * the specific one off sh:detail. Keep only the leaves, so the message names
 * the property that actually failed.
 */
function leafResults(results) {
  return results.flatMap((result) =>
    result.detail?.length ? leafResults(result.detail) : [result],
  )
}

function dedupe(findings) {
  const seen = new Set()
  return findings.filter((f) => {
    const key = `${f.severity}|${f.property}|${f.focus}|${f.message}`
    if (seen.has(key)) return false
    seen.add(key)
    return true
  })
}

async function validateFile(file, validator, shapes, strict) {
  const data = await loadCredential(file)
  const report = await validator.validate(data)

  const findings = dedupe([
    ...leafResults(report.results).map((r) => toFinding(r, shapes)),
    ...checkIr06(data),
  ]).sort((a, b) => a.property.localeCompare(b.property))

  const violations = findings.filter((f) => strict || f.severity !== 'Warning')
  const passed = violations.length === 0

  console.log(`${passed ? 'PASS' : 'FAIL'}  ${file}`)
  for (const f of findings) {
    const label = !strict && f.severity === 'Warning' ? 'warning' : f.severity
    console.log(`      [${label}] ${f.property}`)
    console.log(`        ${f.message}`)
    console.log(`        focus: ${f.focus}`)
  }
  return passed
}

async function main(argv) {
  const strict = argv.includes('--strict')
  const shapesIndex = Math.max(argv.indexOf('-s'), argv.indexOf('--shapes'))
  const shapesFile = shapesIndex === -1 ? CORE_SHAPES : argv[shapesIndex + 1]
  const files = argv.filter((a, i) =>
    !a.startsWith('-') && !(shapesIndex !== -1 && i === shapesIndex + 1))

  if (files.length === 0) {
    console.error('usage: validate-membership.mjs [--strict] [-s shapes.ttl] credential.jsonld ...')
    return 2
  }

  let shapes
  try {
    shapes = await rdf.dataset().import(rdf.fromFile(shapesFile))
  } catch (error) {
    console.error(`cannot read shapes graph ${shapesFile}: ${error.message}`)
    return 2
  }
  const validator = new SHACLValidator(shapes, { factory: rdf })

  let failed = 0
  for (const file of files) {
    try {
      if (!await validateFile(file, validator, shapes, strict)) failed += 1
    } catch (error) {
      // malformed JSON, unreachable @context, unparseable RDF
      console.error(`ERROR ${file}: ${error.name}: ${error.message}`)
      return 2
    }
  }

  const advisory = strict ? '' : '  (warnings advisory; --strict to fail on them)'
  console.log(`\n${files.length - failed}/${files.length} conform${advisory}`)
  return failed ? 1 : 0
}

process.exit(await main(process.argv.slice(2)))
