#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =======================================================


from itertools import product


def getPlaces(string):
    leet = [
        "Aa@",
        "Bb",
        "Cc",
        "Dd",
        "Ee",
        "Ff",
        "Gg",
        "Hh",
        "Ii1",
        "Jj",
        "Kk",
        "Ll1",
        "Mm",
        "Nn",
        "Oo0",
        "Pp",
        "Qq9",
        "Rr",
        # "Ss$5",
        "Ss5",
        "Tt",
        "Uu",
        "Vv",
        "Ww",
        "Xx",
        "Yy",
        "Zz2"
    ]

    result = []
    for el in string:
        result.append(leet[ord(el.upper()) - 65])

    return result


# leet listを返す
def GetLeetList(string):
    for letters in product(*getPlaces(string)):
        yield "".join(letters)
