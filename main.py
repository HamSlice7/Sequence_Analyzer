import sys
import sequences_from_fasta
import gene_analysis

#fasta_file = sys.argv[1]

#sequences = sequences_from_fasta.sequence_from_fasta(fasta_file)

g1 = gene_analysis.GeneSequence('GCTA', 'COX1', 'Homo sapiens')

print(g1.complement())