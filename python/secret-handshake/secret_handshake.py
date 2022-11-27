def commands(binary_str):
    moves = list(binary_str)
    handshake = []
    if moves[4] == "1":
        handshake.append("wink")
    if moves[3] == "1":
        handshake.append("double blink")
    if moves[2] == "1":
        handshake.append("close your eyes")
    if moves[1] == "1":
        handshake.append("jump")
    if moves[0] == "1":
        handshake.reverse()
    return handshake
