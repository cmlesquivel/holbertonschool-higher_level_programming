#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    is_div_two = []
    for x in my_list:
        if x % 2 == 0:
            is_div_two.append(True)
        else:
            is_div_two.append(False)
    return is_div_two
