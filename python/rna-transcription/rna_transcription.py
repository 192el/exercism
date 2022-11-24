def to_rna(dna_strand):
    list(dna_strand)
    rna_transcription = []
    for i in range(len(dna_strand)):
        if dna_strand[i] == 'G':
            rna_transcription.append('C')
        elif dna_strand[i] == 'C':
            rna_transcription.append('G')
        elif dna_strand[i] == 'T':
            rna_transcription.append('A')
        elif dna_strand[i] == 'A':
            rna_transcription.append('U')
    return ''.join(rna_transcription)
