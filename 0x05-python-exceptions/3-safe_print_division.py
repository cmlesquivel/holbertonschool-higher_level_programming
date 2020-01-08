#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        print("Inside result:", end="")
        result = a/b
    except:
        print("None")
    else:
        print(result)
    finally:
        pass
