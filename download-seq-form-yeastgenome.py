import wget

#set all the gene names be searched
gene_symbol = ["ARG1", "KRT10", "KRT1"]

#set the No for the first gene
count = 4424

#search and download every gene sequence from www.yeastgenome.org
for x in gene_symbol:
  url = "https://www.yeastgenome.org/run_seqtools?format=fasta&type=coding&genes=" + x + "&strains=S288C"
  path = "your file path" + str(count) + "_" + x + ".fsa"
  wget.download(url, path)
  count = count +1
  print(" " + x)

'''
https://www.yeastgenome.org/run_seqtools?format=fasta&type=coding&genes=LSM3&strains=S288C
*If want to get protein sequence, change type=coding to type=protein
https://www.yeastgenome.org/run_seqtools?format=fasta&type=protein&genes=LSM3&strains=S288C

Author: Takumii
Date: 2023.07.17
'''




