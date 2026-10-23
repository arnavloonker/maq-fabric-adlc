# PR brief: <repository> !<pr-id> — <PR title>

- Status: <active|completed|abandoned> | Review version: iteration <n>
- Baseline: target `<commit>` → source `<commit>` (native review diff)
- Links: PR <url>; story <url or "none supplied">
- Coverage: <files reviewed / total>; unavailable, generated, binary, or truncated: <list or "none">

## What changed
<Two to five plain sentences: what is different and, if a source states it, why. Say "Intent not stated" if unknown.>

## Before and after
<Repeat the appropriate view for each meaningful change; remove the unused alternatives and replace all illustrative content with baseline evidence. Identify artifact/path and Before/After commit links. Use "not present" for evidenced creates/deletes and "unavailable" for unreadable content.>

### Table view (alternative)
Artifact: <name>; Before: `<target-commit>:<path>`; After: `<source-commit>:<path>`

**Before**

| Field | Type | Change |
| --- | --- | --- |
| id | int | unchanged |

**After**

| Field | Type | Change |
| --- | --- | --- |
| id | int | unchanged |
| **email** | **string** | **added** |

### Artifact/diagram view (alternative)
Artifact: <name>; Before: `<target-commit>:<path>`; After: `<source-commit>:<path>`

```mermaid
flowchart LR
  subgraph Before
    A1["Source"] --> B1["Artifact"]
  end
  subgraph After
    A2["Source"] --> B2["Artifact"] --> C2["Consumer (added)"]
  end
  classDef changed stroke:#b36b00,stroke-width:3px
  class C2 changed
```
Notes: <what moved, was added, changed, or removed; styling and text identify changes>

### Code-block view (alternative)
Artifact: <name>; Before: `<target-commit>:<path>`; After: `<source-commit>:<path>`

**Before**
```diff
 line 1
 line 2
```

**After**
```diff
 line 1
 line 2
+line 3
```
Notes: <prefixes are display markers; explain the added/changed/removed lines>

## Impact
| Artifact or consumer | Relationship | Basis | Effect |
| --- | --- | --- | --- |
| <name> | direct / downstream | evidenced / inferred / unknown | <effect> |

## Intended versus verified
| Intent or criterion | Source | Verified? | Evidence |
| --- | --- | --- | --- |
| <criterion> | <story / approach> | yes / no / not checked | <link or "static review only"> |

## Limits
<Inferences made, unknowns, access gaps, and that Mermaid is unrendered unless checked. No runtime success is claimed from static changes.>
