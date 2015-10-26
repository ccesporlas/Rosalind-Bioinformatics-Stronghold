dataset = open("rosalind_rna.txt","r")
#dataset = open("rosalind_ini9_test.txt","r")

rnaNucleotideComplement = {'T':'U','G':'G','A':'A','C':'C'}

for line in dataset:
    rnaString = ''
    line = line.rstrip()
    for nucleotide in line:
        rnaString += rnaNucleotideComplement[nucleotide]
    print rnaString
