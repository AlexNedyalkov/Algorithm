from random import randint
# Swap function
def swap_positions(my_list, pos1, pos2):
    my_list[pos1], my_list[pos2] = my_list[pos2], my_list[pos1]
    return my_list


def shuffle(my_list: list):

    for i in range(len(my_list)):
        rnd = i + randint(0, len(my_list) - 1 - i)
        my_list = swap_positions(my_list, i, rnd)
    return my_list


my_list = [23, 65, 19, 90]
# pos1, pos2 = 1, 3
#
# print(swap_positions(my_list, pos1 - 1, pos2 - 1))
print(shuffle(my_list))
