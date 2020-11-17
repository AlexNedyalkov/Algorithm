def recursive_sum(my_array: list, index: int = 0) -> float:
    if index == len(my_array) - 1:
        return my_array[len(my_array) - 1]
    current_sum = my_array[index] + recursive_sum(my_array, index + 1)
    return current_sum


def recursive_factorial(number: int):
    if number == 0:
        return 1
    return number * recursive_factorial(number - 1)


def recursive_drawing(number):
    if number == 0:
        return
    print('*' * number)
    recursive_drawing(number - 1)
    print('#' * number)


my_array = [1,2,3,4]
print(recursive_sum(my_array))
print(recursive_factorial(10))
recursive_drawing(3)