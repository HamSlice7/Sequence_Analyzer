def sequence_from_fasta(fasta_file):

    sequences = []

    with open(fasta_file, "r") as file:
        for line in file:
            line = line.strip()
            if line[0] != ">":
                sequences.append(line)    
    return sequences
