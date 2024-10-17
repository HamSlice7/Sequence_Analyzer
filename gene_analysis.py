class GeneSequence(object):
    
    def __init__(self, sequence, gene_name, species_name):
        self.sequence = sequence
        self.gene_name = gene_name
        self.species_name = species_name
        

    def complement(self):
        replace_1 = self.sequence.replace('A', 't')
        replace_2 = replace_1.replace('T', 'a')
        replace_3 = replace_2.replace('C', 'g')
        replace_4 = replace_3.replace('G', 'c')
        gene_complement = replace_4.upper()
        return gene_complement
    
    def get_AT(self):
        length = len(self.sequence)
        a_count = self.sequence.count('A')
        t_count = self.sequence.count('T')
        at_count = (a_count + t_count)/length
        return at_count
    
g1 = GeneSequence('ATATTATATATTATTATTA', 'COX1', 'Homo sapiens')
print(g1.complement())
print(g1.get_AT())