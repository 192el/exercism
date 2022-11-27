def find_anagrams(word, candidates):
    anagrams = []
    lowerword = word.lower()
    lowercandidates = [candidate.lower() for candidate in candidates]
    for i in range(len(candidates)):
        if list(sorted(lowerword)) == list(sorted(lowercandidates[i])) and list(lowerword) != list(lowercandidates[i]):
            anagrams.append(candidates[i])
    return anagrams
