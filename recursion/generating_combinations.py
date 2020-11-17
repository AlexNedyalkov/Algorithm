def generate_combinations_01(vector_length, index, vector):
    if index >= vector_length:
        print(vector)
    else:
        for i in range(2):
            vector[index] = i
            generate_combinations_01(number_of_elements, index + 1, vector)


def generating_combinations(numbers, vector, index = 0):
    print(index)
    if index == len(vector):
        print(vector)
    for i in range(len(numbers)):
        vector[index] = numbers[i]
        generating_combinations(numbers[index:], vector, index + 1)


number_of_elements = 3
my_list = [None] * number_of_elements
# generate_combinations_01(8, 0, my_list)

numbers = [1, 2, 3]
k = 2
vector = [None] * k
generating_combinations(numbers, vector)
