# Logic Errors

No error message — but the output is wrong. The hardest type to catch.

---

<!-- Entries go below — newest at the top -->

## Logic Error: wrong comparison operator — `>` instead of `<`

**When I hit it:** Day 4 — `bmiPracticeAdvanced-Day4.py`, line 20

**What Python says:**
```
No error — code runs fine but prints wrong result.
BMI 29.58 (overweight) was printed as "underweight"
```

**What it means (plain English):**
The condition `> 18.5` catches everything ABOVE 18.5 — which is the opposite of underweight. Python matched the very first `if`, printed "underweight", and never checked the rest.

**Analogy:**
You put the "underweight" sign on the heavy door instead of the light one. The doors worked fine — the labels were just swapped. Python follows your instructions exactly, even when they're logically backwards.

**What broke (my code):**
```python
if calculateBMI(userWeight, userHeight) > 18.5:   # ❌ > means greater than — catches overweight people
    print('underweight')
```

**Fix:**
```python
if calculateBMI(userWeight, userHeight) < 18.5:   # ✅ < means less than — correctly catches underweight
    print('underweight')
elif 18.5 <= calculateBMI(userWeight, userHeight) < 25:
    print('normal weight')
elif calculateBMI(userWeight, userHeight) >= 25:
    print('overweight')
```

**Why it works now:**
`<` (less than) correctly identifies BMI below 18.5 as underweight. The first `if` no longer swallows everyone above 18.5.

**Remember:**
Logic errors have NO error message — always test with known values.
For BMI 29.58, expected output is "overweight". If you get anything else, the condition signs are flipped.

---
