def append(list1, list2):
    if list2 != []:
        for i in range(len(list2)):
            list1.append(list2[i])
    return list1


def concat(lists):
    updatedlist = []
    for i in range(len(lists)):
        updatedlist += lists[i]
    return updatedlist


def filter(function, list):
    return [item for item in list if function(item) == True]


def length(list):
    return len(list)


def map(function, list):
    for i in range(len(list)):
        list[i] = function(list[i])
    return list


def foldl(function, list, initial):
    if list == []:
        return initial
    if all(isinstance(item, str) for item in list):
        list.append(initial)
        return ''.join(list)
    else:
        for i in range(len(list)):
            initial += list[i]
        return initial



def foldr(function, list, initial):
    if list == []:
        return initial
    if all(isinstance(item, str) for item in list):
        list.append(initial)
        return ''.join(list)
    else:
        for i in range(len(list)):
            initial += list[i]
        return initial


def reverse(list):
    list.reverse()
    return list
