import sys
import sequences_from_fasta
import gene_analysis

fasta_file = sys.argv[1]

sequences = sequences_from_fasta.sequence_from_fasta(fasta_file)


for sequence in sequences:
    gene = gene_analysis.GeneSequence(sequence)
    print(gene.get_AT())
    print(gene.get_GC())



