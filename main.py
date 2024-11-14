import sys
import sequences_from_fasta
import gene_analysis
import matplotlib.pyplot as plt

"""
Use GeneSequence class to get data from a fasta file and output a csv file for the user
"""

fasta_file = sys.argv[1]

sequences = sequences_from_fasta.sequence_from_fasta(fasta_file)


validation_data_sequence_lengths = []

for gene_name,gene_sequences in sequences.items():
    gene = gene_analysis.GeneSequence(gene_sequences, gene_name)
    #print(f"AT content of {gene_name} is {gene.get_AT()}")
    #print(f"GC content of {gene_name} is {gene.get_GC()}")
    validation_data_sequence_lengths.append(gene.get_length())

validation_peptides = [peptide for peptide in validation_data_sequence_lengths if peptide <= 100]

print(validation_peptides)

plt.hist(validation_peptides)

plt.show()