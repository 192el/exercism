def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    if strand_a == strand_b:
        return 0
    else:
        hammingdistance = []
        for i in range(len(strand_a)):
            if strand_a[i] != strand_b[i]:
                hammingdistance.append(1)
        return sum(hammingdistance)

