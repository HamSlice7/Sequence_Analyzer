class GeneSequence(object):
    
    def __init__(self, sequence:str):
        self.sequence = sequence
        
        

    def complement(self):
        """
        Input: instance of the GeneSequence class

        Output: The complement of the instance of the GeneSequence class
        """
        replace_1 = self.sequence.replace('A', 't')
        replace_2 = replace_1.replace('T', 'a')
        replace_3 = replace_2.replace('C', 'g')
        replace_4 = replace_3.replace('G', 'c')
        gene_complement = replace_4.upper()
        return gene_complement
    
    def get_AT(self):
        """
        Input: instance of the GeneSequence class

        Output: The AT content of the instance of the GeneSequence class
        """
        length = len(self.sequence)
        a_count = self.sequence.count('A')
        t_count = self.sequence.count('T')
        at_count = (a_count + t_count)/length
        return at_count
    
    def get_GC(self):
        """
        Input: instance of the GeneSequence class

        Output: The GC content of the instance of the GeneSequence class
        """
        length = len(self.sequence)
        g_count = self.sequence.count('G')
        c_count = self.sequence.count('C')
        gc_count = (g_count + c_count)/length
        return gc_count
    
    def reverse_complement(self):
        """
        Input: instance of the GeneSequence class

        Output: The reverse complement of the instance of the GeneSequence class
        """
        reverse_gene = self.sequence[::-1]
        reverse_replace_1 = reverse_gene.replace('A', 't')
        reverse_replace_2 = reverse_replace_1.replace('T', 'a')
        reverse_replace_3 = reverse_replace_2.replace('C', 'g')
        reverse_replace_4 = reverse_replace_3.replace('G', 'c')
        reverse_gene_complement = reverse_replace_4.upper()
        return reverse_gene_complement
    
