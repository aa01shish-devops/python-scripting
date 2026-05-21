'''
    BMI Calculator with Interpretations
Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.

If the bmi is under 18.5 (not including), print out "underweight"

If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"

If the bmi is 25 (including) or over, print out "overweight"

'''

def calculateBMI(num1, num2):
    bmiValue = (num1 / (num2 ** 2))
    return bmiValue

userWeight = float(input('Please Enter The Weight(kgs)?\n'))
userHeight = float(input('Please Enter The Height(mts)?\n'))

if calculateBMI(userWeight, userHeight) < 18.5:
    print(f'underweight')
elif 18.5 <= calculateBMI(userWeight, userHeight) < 25:
    print(f'normal weight')
elif calculateBMI(userWeight, userHeight) >= 25:
    print(f'overweight')

    



