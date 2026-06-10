'''
fuzz = [] 

buzz = []

fuzz_buzz = []

for numbers in range(1, 101):
    #print(numbers)
    if numbers % 3 == 0:
        fuzz.append(numbers)
    if numbers % 5 == 0:
        buzz.append(numbers)
    if numbers % 5 == 0 and numbers % 3 == 0:
        fuzz_buzz.append(numbers)


print(f'fuzz numbers are: {fuzz}\nbuzz numbers are: {buzz}\nfuzz_buzz numbers are: {fuzz_buzz}')
'''
new_numbers = [
    "fizzbuzz" if numbers % 3 == 0 and numbers % 5 == 0 
    else "fizz" if numbers % 3 == 0 
    else "buzz" if numbers % 5 == 0 
    else numbers # Fallback for numbers not divisible by 3 or 5
    for numbers in range(1, 16)
]

for numbers in new_numbers:
    print(numbers)
