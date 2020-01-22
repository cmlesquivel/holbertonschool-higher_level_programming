#!/usr/bin/python3
import math

result = []


def pascal_triangle(n):
        """Pascal's Triangle"""
        for count in range(n):
                row = []
                for element in range(count + 1):
                        row.append(combination(count, element))
                result.append(row)
        return result


def combination(n, r):
        """Pascal's Triangle"""
        a = (math.factorial(n))
        return int(a / ((math.factorial(r)) * math.factorial(n - r)))
