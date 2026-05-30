import random

coin = ['Head', 'Tail']

for i in range(1000):
    output = random.choice(coin)
    print(f'The Side Of The Coin is: {output}')
