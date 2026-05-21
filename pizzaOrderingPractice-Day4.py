userPizzaSize = input(f'Welcome To Python Pizza Deliveries!\nWhat Size Of Pizza Do You Want? S, M, L: ')
userPepperoni = input(f'Do You Want Pepperoni On Your Pizza? Y, N: ')
userExtraCheese = input(f'Do You Want Extra Cheese On Your Pizza? Y, N: ')

totalBill = 0
smallPizza = 50
mediumPizza = 100
largePizza = 150
pepperoniPrice = 20
extraCheesePrice = 5
extraPay = 0

if userPizzaSize == "S" and userPepperoni == "Y":
    totalBill = smallPizza + pepperoniPrice
    extraPay = smallPizza - pepperoniPrice
    print(f'Your Total Bill is {totalBill},  You are Paying {extraPay} extra')

elif userPizzaSize == "S" and userPepperoni == "N":
    totalBill = smallPizza
    print(f'Your Total Bill is {totalBill},  You are Paying Nothing extra')

if userPizzaSize == "M" and userPepperoni == "Y":
    totalBill = mediumPizza + pepperoniPrice
    extraPay = mediumPizza - pepperoniPrice
    print(f'Your Total Bill is {totalBill},  You are Paying {extraPay} extra')

elif userPizzaSize == "M" and userPepperoni == "N":
    totalBill = mediumPizza
    print(f'Your Total Bill is {totalBill},  You are Paying Nothing extra')

if userPizzaSize == "L" and userPepperoni == "Y":
    totalBill = largePizza + pepperoniPrice
    extraPay = largePizza - pepperoniPrice
    print(f'Your Total Bill is {totalBill},  You are Paying {extraPay} extra')

elif userPizzaSize == "L" and userPepperoni == "N":
    totalBill = largePizza
    print(f'Your Total Bill is {totalBill},  You are Paying Nothing extra')

if userPizzaSize == "S" and userExtraCheese == "Y":
    totalBill = smallPizza + extraCheesePrice
    extraPay = smallPizza - extraCheesePrice
    print(f'Your Total Bill is {totalBill},  You are Paying {extraPay} extra')

elif userPizzaSize == "S" and userExtraCheese == "N":
    totalBill = smallPizza
    print(f'Your Total Bill is {totalBill},  You are Paying Nothing extra')

if userPizzaSize == "M" and userExtraCheese == "Y":
    totalBill = mediumPizza + extraCheesePrice
    extraPay = mediumPizza - extraCheesePrice
    print(f'Your Total Bill is {totalBill},  You are Paying {extraPay} extra')

elif userPizzaSize == "M" and userExtraCheese == "N":
    totalBill = mediumPizza
    print(f'Your Total Bill is {totalBill},  You are Paying Nothing extra')

if userPizzaSize == "L" and userExtraCheese == "Y":
    totalBill = largePizza + extraCheesePrice
    extraPay = largePizza - extraCheesePrice
    print(f'Your Total Bill is {totalBill},  You are Paying {extraPay} extra')

elif userPizzaSize == "L" and userPepperoni == "N":
    totalBill = largePizza
    print(f'Your Total Bill is {totalBill},  You are Paying Nothing extra')










