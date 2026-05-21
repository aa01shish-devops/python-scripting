def checkNumbers(num):
    if num % 2 == 0:
        print(f'The Num Entered is Even')
    else:
        print(f'The Num Entered is Odd')

userValue = int(input('Please Enter The Number\n'))

checkNumbers(userValue)
