# Syntax Errors & Indentation Errors

Errors where Python can't even read your code — like a sentence with broken grammar.

---

<!-- Entries go below — newest at the top -->

## SyntaxError: expected ':' — condition given to `else`

**When I hit it:** Day 4 — `bmiPracticeAdvanced-Day4.py`, line 24

**What Python says:**
```
File "bmiPracticeAdvanced-Day4.py", line 24
    else calculateBMI(userWeight, userHeight) >= 25:
         ^^^^^^^^^^^^
SyntaxError: expected ':'
```

**What it means (plain English):**
`else` cannot have a condition. It is the catch-all — it handles everything not caught by `if` or `elif`. If you need to check a condition, use `elif` instead.

**Analogy:**
`if/elif/else` is like a club bouncer with a checklist:
- `if` → "Are you VIP?" (checks condition)
- `elif` → "Are you staff?" (checks another condition)
- `else` → "Everyone else, come in." (no check — catches whoever is left)

Giving `else` a condition is like the bouncer saying "Everyone else who is over 25..." — that's not a catch-all, that's a new check. Use `elif` for that.

**What broke (my code):**
```python
else calculateBMI(userWeight, userHeight) >= 25:   # ❌ else can't have a condition
```

**Fix:**
```python
# Option 1 — if you need the condition, use elif
elif calculateBMI(userWeight, userHeight) >= 25:
    print("Obese")

# Option 2 — drop the condition entirely (cleaner for BMI)
else:
    print("Obese")
```

**Why it works now:**
`else` is the final bucket — if nothing above matched, this runs. No condition needed because it's already implied: "everything that didn't match above."

**Remember:**
- Has a condition? → `elif`
- No condition, just catch the rest? → `else:`
- `else` always ends with just `:` — nothing after it

---

## SyntaxError: invalid syntax — `&` instead of `and` + incomplete comparison

**When I hit it:** Day 4 — `bmiPracticeAdvanced-Day4.py`, line 22

**What Python says:**
```
File "bmiPracticeAdvanced-Day4.py", line 22
    elif calculateBMI(userWeight, userHeight) >= 18.5 & < 25:
                                                        ^
SyntaxError: invalid syntax
```

**What it means (plain English):**
Two mistakes in one line:
1. `&` is not "AND" in Python — it's a bitwise operator used for binary math, not comparisons
2. `< 25` has no left side — Python doesn't know *what* is less than 25

**Analogy:**
Like saying "If the temperature is above 18 AND less than" — you stopped mid-sentence. Less than *what*? Referring to *what*? Python needs every comparison written out fully. It doesn't carry context from the previous condition like your brain does.

**What broke (my code):**
```python
elif calculateBMI(userWeight, userHeight) >= 18.5 & < 25:  # ❌ & wrong, < 25 incomplete
```

**Fix:**
```python
# Option 1 — Pythonic chained comparison (cleanest)
elif 18.5 <= calculateBMI(userWeight, userHeight) < 25:

# Option 2 — explicit, spell out both sides fully
elif calculateBMI(userWeight, userHeight) >= 18.5 and calculateBMI(userWeight, userHeight) < 25:
```

**Why it works now:**
- `and` is the correct logical operator (not `&`)
- Every comparison needs a left side AND a right side — Python won't infer it
- Python supports chained comparisons: `18.5 <= x < 25` is valid and clean

**Remember:**
- Logical AND → `and` (plain English word)
- `&` → bitwise operator, only for binary math, never use in `if` conditions
- Always write both sides of every comparison fully

---

## SyntaxError: invalid syntax — mismatched parentheses in `if` statement

**When I hit it:** Day 4 — `bmiPracticeAdvanced-Day4.py`, line 20

**What Python says:**
```
File "bmiPracticeAdvanced-Day4.py", line 20
    if ((calculateBMI(userWeight, userHeight) > 18.5):
                                                     ^
SyntaxError: invalid syntax
```

**What it means (plain English):**
You opened two `((` brackets but only closed one `)`. Python is waiting for the second closing bracket and gets confused when it hits `:` instead.

**Analogy:**
Brackets are like gloves — every left glove `(` needs a matching right glove `)`. You put on two left gloves but only took off one. Python is standing there holding an unmatched glove, not knowing what to do next.

**What broke (my code):**
```python
if ((calculateBMI(userWeight, userHeight) > 18.5):   # ❌ opened (( but only closed )
```

**Fix:**
```python
# Option 1 — close both brackets
if ((calculateBMI(userWeight, userHeight) > 18.5)):

# Option 2 — simplest, use no extra brackets (recommended)
if calculateBMI(userWeight, userHeight) > 18.5:
```

**Why it works now:**
Every opening bracket must have a matching closing bracket. Python counts them — if they don't balance, it throws a SyntaxError.

**Remember:**
Count your `(` and `)` — they must always be equal. In a simple `if` condition you don't need extra brackets at all.

---

## SyntaxError: invalid syntax — `return` with `=` assignment

**When I hit it:** Day 4 — `bmiPracticeAdvanced-Day4.py`, line 14

**What Python says:**
```
File "bmiPracticeAdvanced-Day4.py", line 14
    return bmiValue = (num1 / (num2 ** 2))
                    ^
SyntaxError: invalid syntax
```

**What it means (plain English):**
You tried to assign a value to a variable and return it in the same line. Python can't do both at once — you have to store first, then return separately.

**Analogy:**
Like telling a chef to cook a dish AND plate it simultaneously in one single motion. He can't — he cooks first, then plates. `=` stores the value (cooking), `return` sends it out (plating). Two separate steps.

**What broke (my code):**
```python
def calculateBMI(num1, num2):
    return bmiValue = (num1 / (num2 ** 2))   # ❌ can't assign and return together
```

**Fix:**
```python
# Option 1 — store first, then return
def calculateBMI(num1, num2):
    bmiValue = (num1 / (num2 ** 2))
    return bmiValue

# Option 2 — return directly (skip storing)
def calculateBMI(num1, num2):
    return num1 / (num2 ** 2)
```

**Why it works now:**
Python processes one action per line. `=` and `return` are two separate actions — they can't share a line.

**Remember:**
`return` sends a value OUT. `=` stores a value IN. Never mix them on the same line.

---
