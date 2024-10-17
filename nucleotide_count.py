
sequence = 'ATGCTAGCTGATGCATGC'


def nucleotide_count(sequence:str) -> dict:
    """
    From a nucleotide sequence, determines the number and percentage of the 4 standard nucleotides.

    Input: Nucleotide sequence
    Output: Data frame of each sequence and the corresponding nucleotide count and percentages

    """
    A_count = 0
    T_count = 0
    C_count = 0
    G_count = 0
    Other = 0

    length_sequence = len(sequence)

    for nuclotide in sequence:
        if nuclotide == "A":
            A_count += 1
        elif nuclotide == "T":
            T_count += 1
        elif nuclotide == "C":
            C_count += 1
        elif nuclotide == "G":
            G_count += 1
        else:
            Other += 1
    
    nucleotide_count_dict = {'A count': A_count, 
                             'T count': T_count, 
                             'C count': C_count, 
                             'G count': G_count, 
                             'Other': Other, 
                             '%A': (f'{round(A_count/length_sequence, 3) * 100} %'),
                             '%T': (f'{round(T_count/length_sequence, 3) * 100} %'),
                             '%C': (f'{round(C_count/length_sequence, 3) * 100} %'),
                             '%G': (f'{round(G_count/length_sequence, 3) *100} %')} 
                            

    
    print(nucleotide_count_dict)
   
    return nucleotide_count_dict

nucleotide_count(sequence)

