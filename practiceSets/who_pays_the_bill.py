import random

list_of_friends = ['Aashish', 'Devansh', 'Vrtika', 'Aditya', 'Aanchal', 'Hardik', 'Richa']

user_input = input('Lets Press Enter To See The Name: [SPACE]')

if user_input == "":
    bill_payer = random.choice(list_of_friends)
    
print(f'{bill_payer} please pay the bill.')


