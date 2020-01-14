#!/usr/bin/python3

"""
This is a module for the test the functions
add_integer function add
"""


def matrix_divided(matrix, div):

    """function that divides all elements of a matrix.
Args:
    matrix(list of lists of integers or floats): list
    div(int o float): number to divede the matrix
Returns:
    Returns a new matrix
Raises:
    TypeError: matrix must be a matrix (list of lists) of integers/floats
    ZeroDivisionError: division by zero
"""
    lengt_matrix = []
    new_matrix = []
    mensaje = "matrix must be a matrix (list of lists) of integers/floats"

    if matrix is None:
        raise TypeError(mensaje)

    if not isinstance(matrix, list):
        raise TypeError(mensaje)

    for x in range(len(matrix)):
        lengt_matrix.append(len(matrix[x]))

    lengt_matrix = set(lengt_matrix)

    if len(lengt_matrix) > 1:
        raise TypeError('Each row of the matrix must have the same size')

    for row in matrix:
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(mensaje)

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    else:
        new_matrix = [row[:] for row in matrix]

        for row in range(len(new_matrix)):
            for i in range(len(new_matrix[row])):
                new_matrix[row][i] = round(new_matrix[row][i]/div, 2)
        return new_matrix
