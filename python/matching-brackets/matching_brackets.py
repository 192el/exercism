def is_paired(input_string):
    brackets = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for c in input_string:
        if c in brackets:
            stack.append(c)
        elif c in brackets.values():
            if not stack or brackets[stack.pop()] != c:
                return False
    return not stack

