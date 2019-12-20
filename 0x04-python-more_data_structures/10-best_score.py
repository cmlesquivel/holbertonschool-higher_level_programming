#!/usr/bin/python3
def best_score(a_dictionary):
        if a_dictionary:
            a = max(zip(a_dictionary.values(), a_dictionary.keys()))
            return a[1]
        return None
