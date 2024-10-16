import sys

fasta_file = sys.argv[1]

print(fasta_file)

def nucleotide_count(file):

    sequences = []

    with open(fasta_file, "r") as file:
        for line in file:
            line = line.strip()
            if line[0] != ">":
                sequences.append(line)
    
    

nucleotide_count(fasta_file)

