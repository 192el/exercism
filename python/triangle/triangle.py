def equilateral(sides):
    if isatriangle(sides):
        if sides[0] == sides[1] and sides[1] == sides[2]:
            return True
        else:
            return False
    else:
        return False


def isosceles(sides):
    if isatriangle(sides):
        if equilateral(sides) or sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
            return True
        else:
            return False
    else:
        return False


def scalene(sides):
    if isatriangle(sides):
        if sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]:
            return True
        else:
            return False
    else:
        return False



def isatriangle(sides):
    if sum(sides) > 0:
        sortedsides = sorted(sides)
        if sortedsides[0] + sortedsides[1] > sortedsides[2]:
            return True
        else:
            return False
    else:
        return False
