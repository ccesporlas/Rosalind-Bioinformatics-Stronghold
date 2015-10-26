dataset = open("rosalind_revc.txt","r")
#dataset = open("rosalind_ini8_test.txt","r")

nucleotideComplement = {'A':'T','T':'A','C':'G','G':'C'}
reverseComplement = ''

for line in dataset:
    line = line.rstrip()
    for nucleotide in line[::-1]:
        reverseComplement += nucleotideComplement[nucleotide]
    print reverseComplement
dataset.close()
