#!/usr/bin/python3
import sys
import hidden_4

if __name__ == "__main__":
    for my_str in dir(hidden_4):
        if my_str[0] != '_' and my_str[1] != '_':
            print(my_str)
