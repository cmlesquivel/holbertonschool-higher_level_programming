#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1:
        tuple_ax = (tuple_a[0], 0)
    elif len(tuple_a) == 0:
        tuple_ax = (0, 0)
    else:
        tuple_ax = tuple_a
    if len(tuple_b) == 1:
        tuple_bx = (tuple_b[0], 0)
    elif len(tuple_b) == 0:
        tuple_bx = (0, 0)
    else:
        tuple_bx = tuple_b
    a = tuple_ax[0] + tuple_bx[0]
    b = tuple_ax[1] + tuple_bx[1]

    return (a, b)
