# Python Error Journal — Aashish's Reference Book

My personal go-to book for Python errors. Every error I hit during practice gets logged here with a plain-English explanation and a real-world analogy.

## Categories

| File | Error Types |
|------|------------|
| [syntax_errors.md](syntax_errors.md) | SyntaxError, IndentationError |
| [type_errors.md](type_errors.md) | TypeError, ValueError |
| [name_errors.md](name_errors.md) | NameError, UnboundLocalError |
| [logic_errors.md](logic_errors.md) | Wrong output, infinite loops, off-by-one |
| [import_errors.md](import_errors.md) | ModuleNotFoundError, ImportError |
| [index_errors.md](index_errors.md) | IndexError, KeyError |

## Entry Template

Copy this for every new error:

---

## ErrorType: exact error message here

**When I hit it:** _(which day / which script)_

**What Python says:**
```
paste the full error message here
```

**What it means (plain English):**
One or two sentences. No jargon.

**Analogy:**
Real-world comparison that makes it click.

**What broke (my code):**
```python
# the broken code
```

**Fix:**
```python
# the working code
```

**Why it works now:**
One sentence explanation.

**Remember:**
One-liner memory tip to never hit this again.

---
