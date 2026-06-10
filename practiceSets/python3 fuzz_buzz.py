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

for numbers in range(1, 11):
    if numbers % 3 == 0:
        fizz = numbers
    if numbers % 5 == 0:
        buzz = numbers
    if numbers % 5 == 0 and numbers % 3 == 0:
        fizzbuzz = numbers
    print(numbers)

