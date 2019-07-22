from Bio import Seq

seq_1 = Seq('ATG')

#Sequencia Complementar
my_seq_complementar = seq_1.complement()
print (my_seq_complementar)

#Sequencia Revesa Complementar
my_seq_rev_complementar = seq_1.reverse_complement()
print (my_seq_rev_complementar)

#Trnscrição
my_rna = seq_1.transcribe()
print (my_rna)

my_dna = my_rna.back_transcribe()
print (my_dna)

#Tradução
my_proteina_rna = my_rna.translate()
my_proteina_dna = my_dna.translate()
print (my_proteina_rna)
print (my_proteina_dna)
