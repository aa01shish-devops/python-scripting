userBill = int(input('Welcome To Tip Calculator\nWhat Was The Total Bill?\n'))
userTip = int(input('How Much Tip Would You Like To Give ?\n'))
userCount = int(input('How Many People To Split The Bill?'))

sharePerPerson = float(userBill + userTip / userCount)
print(f'Each Person Should Pay: {sharePerPerson}')
