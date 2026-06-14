numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 1000

def binary_search_target():
    for number in numbers:
        if number == target:
            target_index = numbers.index(number)
        else:
            target_index = numbers[-1]

    print(target_index)


binary_search_target()

