def transpose(lines):
    lines = lines.split('\n')
    longline = max(map(len, lines))
    lines = map(lambda x: x + '\0' * (longline - len(x)), lines)
    return '\n'.join(map(lambda x: ''.join(x).rstrip('\0'), zip(*lines))).replace('\0', ' ')