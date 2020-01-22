#!/usr/bin/python3

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
        a = factorial(n)
        return int(a / ((factorial(r)) * factorial(n - r)))


def factorial(n):
        """Pascal's Triangle"""
        if n == 0:
                r = 1
        else:
                r = n * factorial(n - 1)
        return r
