def to_rna(dna_strand):
    dna_cod = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    rna = ''

    for cod in dna_strand:
        rna = rna + dna_cod[cod]
    return rna
