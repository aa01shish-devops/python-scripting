userPizzaSize = input('Welcome To Python Pizza Deliveries!\nWhat Size Of Pizza Do You Want? S, M, L: ')
userPepperoni = input('Do You Want Pepperoni On Your Pizza? Y, N: ')
userExtraCheese = input('Do You Want Extra Cheese On Your Pizza? Y, N: ')

totalBill = 0

# Step 1 — base price by size
if userPizzaSize == "S":
    totalBill = 15
elif userPizzaSize == "M":
    totalBill = 20
elif userPizzaSize == "L":
    totalBill = 25

# Step 2 — add pepperoni
if userPepperoni == "Y":
    if userPizzaSize == "S":
        totalBill += 2
    else:
        totalBill += 3

# Step 3 — add extra cheese
if userExtraCheese == "Y":
    totalBill += 1

# Step 4 — print once
print(f'Your final bill is: ${totalBill}')
