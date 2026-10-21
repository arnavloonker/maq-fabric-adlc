# Domain: Order Management

Status: Draft | Run ID: 2026-10-21-om-01 | Last reviewed: never

## 1. Purpose and owner
- Purpose: Capture, fulfil, and invoice customer orders.
- Owner: Unknown
- Standards documents: none identified

## 2. Business vocabulary
Implementation-free definitions only.

| Term | Definition | Synonyms |
|------|------------|----------|
| Order | A customer's committed request to buy goods or services. | Sales order |
| Fulfilment | Delivery of what an order promised. | Shipment |

## 3. Source systems
| System | Owner | Authoritative link | Provenance |
|--------|-------|--------------------|------------|
| Example ERP | Unknown | https://example.invalid/erp | Repo README, 2026-10-21 |

## 4. Data products
| Product | Consumers | Authoritative link | Provenance |
|---------|-----------|--------------------|------------|
| Orders semantic model | Finance reporting | https://example.invalid/model | Workspace metadata, 2026-10-21, DEV |

## 5. Source-of-truth references
- Order policy: link to the authoritative system or document.

## 6. Reviewed rules
| ID | Rule | Reviewer | Review date | Source |
|----|------|----------|-------------|--------|
| R-001 | An order is cancellable until it ships. | A. Reviewer | 2026-10-01 | Policy doc link |

## 7. Provisional observations
Inferred from code or data; not business policy until reviewed.

| ID | Observation | Source | Observed | Environment | Confidence | Limitations |
|----|-------------|--------|----------|-------------|------------|-------------|
| P-001 | Orders appear to be excluded when status is test. | Repo transformation code | 2026-10-21 | DEV | Medium | Not confirmed with owner |

## 8. Explicit conflicts
| ID | Claim A (source) | Claim B (source) | Status |
|----|------------------|------------------|--------|
| C-001 | Order date means placement date (glossary) | Order date means approval date (report) | Open |

## 9. Change log
| Run ID | Date | Summary |
|--------|------|---------|
| 2026-10-21-om-01 | 2026-10-21 | Initial record |

---

# Index (`domain\index.md`)

| Domain | Owner | Purpose | File | Last reviewed | Open conflicts |
|--------|-------|---------|------|---------------|----------------|
| Order Management | Unknown | Capture, fulfil, and invoice orders | [order-management.md](order-management.md) | never | 1 |
