"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 69
SUPERLIST = 420
EQUAL = 666
UNEQUAL = 6969


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if checksublist(list_one, list_two):
        return SUBLIST
    if checksublist(list_two, list_one):
        return SUPERLIST
    else:
        return UNEQUAL



def checksublist(list_one, list_two):
    #check if list_one is a sublist of list_two
    if len(list_one) > len(list_two):
        return False
    for i in range(len(list_two) - len(list_one) + 1):
        if list_one == list_two[i:i+len(list_one)]:
            return True
    return False
