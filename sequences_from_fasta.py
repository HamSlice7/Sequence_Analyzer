import re

def sequence_from_fasta(fasta_file) -> dict:
    """
    Input: FASTA file
    Output: Dictionary where the key is the gene name and the value is the sequence
    """

    gene_name = []
    sequences = []

    with open(fasta_file, "r") as file:
        for line in file:
            line = line.strip()
            if line[0] == ">":
                line = re.search("[^>]+", line)
                gene_name.append(line.group())  
            else:
                sequences.append(line)

        gene_name_with_sequence = dict(zip(gene_name, sequences))
        

    return gene_name_with_sequence
   
