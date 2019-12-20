#!/usr/bin/python3
def common_elements(set_1, set_2):
    list_common = []
    for i in set_1:
        for x in set_2:
            if i in x:
                list_common.append(x)

    return list_common
