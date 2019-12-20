#!/usr/bin/python3
def best_score(a_dictionary):
    max = 0
    score = ''

    if a_dictionary:
        for clave, valor in sorted(a_dictionary.items()):
            if valor > max:
                score = clave
        return score
    return None
