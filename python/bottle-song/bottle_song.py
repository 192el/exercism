NUMBERS = [
    "No",
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
]
def recite(start, take=1):
    returnlist = []
    for i in range(start, start-take, -1):
        returnlist.append(NUMBERS[i] + f" green bottle{'' if NUMBERS[i] in ['No', 'One'] else 's'} hanging on the wall,")
        returnlist.append(NUMBERS[i] + f" green bottle{'' if NUMBERS[i] in ['No', 'One'] else 's'} hanging on the wall,")
        returnlist.append("And if one green bottle should accidentally fall,")
        returnlist.append("There'll be " + NUMBERS[i-1].lower() + f" green bottle{'' if NUMBERS[i-1] in ['One'] else 's'} hanging on the wall.")
        returnlist.append("")
    return returnlist[:-1]