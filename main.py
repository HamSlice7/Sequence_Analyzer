import sys
import sequences_from_fasta

fasta_file = sys.argv[1]

sequences = sequences_from_fasta.sequence_from_fasta(fasta_file)