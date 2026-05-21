# Type Errors & Value Errors

Errors where Python gets the right kind of instruction but the wrong type of data.

---

<!-- Entries go below — newest at the top -->

## TypeError: unsupported operand type(s) for &: 'str' and 'str'

**When I hit it:** Day 4 — `pizzaOrderingPractice-Day4.py`, line 13

**What Python says:**
```
TypeError: unsupported operand type(s) for &: 'str' and 'str'
```

**What it means (plain English):**
You used `&` between two strings. `&` is a binary/math operator — it only works on numbers. It has no idea what to do with text like `"S"` or `"Y"`.

**Analogy:**
`&` is a calculator. You handed it two words instead of numbers. The calculator says "I only work with numbers — I don't know what to do with letters." Use `and` instead — it's the plain English logical connector, not a math tool.

**What broke (my code):**
```python
if userPizzaSize == "S" & userPepperoni == "Y":   # ❌ & can't compare strings
```

**Fix:**
```python
if userPizzaSize == "S" and userPepperoni == "Y":  # ✅ and is the logical connector
```

**Why it works now:**
`and` checks if both conditions are True — it works with any type (strings, numbers, booleans). `&` is bitwise math and only works on integers.

**Remember:**
- Comparing conditions? → always `and`, `or`, `not`
- `&`, `|` → only for binary math on numbers, never in `if` conditions

---
