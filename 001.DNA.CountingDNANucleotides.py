dataset = open("rosalind_dna.txt","r")
dnaString = ""
for line in dataset:
    dnaString += line.upper().rstrip()
dataset.close()

#dnaString = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
#print dnaString
#print len(dnaString)

#we already have a set of expected values. count only these.
nucleotides = ['A','C','G','T']

#store the count per nucleotide in the same sequence
nucleotidesCount = []

#sum of count per nucleotide must be equal to the total dna length
checkDnaLength = 0

#go through the list of nucleotides and count the number of occurences of the nucleotide in the DNA sequence
#DNA sequence must be formatted correctly once received (e.g. expect that data must contain only uppercase letters)
for i in nucleotides:
    count = dnaString.count(i)
    nucleotidesCount.append(str(count))
    checkDnaLength += count
print ' '.join(nucleotidesCount)
#print checkDnaLength
