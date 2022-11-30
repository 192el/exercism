def proteins(strand):
    codons_to_protein = {}
    codons_to_protein.update(dict.fromkeys(['AUG'], 'Methionine'))
    codons_to_protein.update(dict.fromkeys(['UUU', 'UUC'], 'Phenylalanine'))
    codons_to_protein.update(dict.fromkeys(['UUA', 'UUG'], 'Leucine'))
    codons_to_protein.update(dict.fromkeys(['UCU', 'UCC', 'UCA', 'UCG'], 'Serine'))
    codons_to_protein.update(dict.fromkeys(['UAU', 'UAC'], 'Tyrosine'))
    codons_to_protein.update(dict.fromkeys(['UGU', 'UGC'], 'Cysteine'))
    codons_to_protein.update(dict.fromkeys(['UGG'], 'Tryptophan'))
    codons_to_protein.update(dict.fromkeys(['UAA', 'UAG', 'UGA'], 'STOP'))
    codon = []
    proteins = []
    for i in range(len(strand) // 3):
        breakcondition = False
        for y in range(3):
            codon.append(strand[y])
        if len(codon) == 3:
            codon_string = ''.join(codon)
            if codons_to_protein[codon_string] == 'STOP':
                breakcondition = True
                break
            else:
                proteins.append(codons_to_protein[codon_string])
                codon.clear()
                strand = strand[3:]
        if breakcondition:
            break
    return proteins