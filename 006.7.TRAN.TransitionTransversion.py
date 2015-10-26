dataset = open("rosalind_tran.txt","r")
#dataset = open("1.txt","r")

dnaStringID = []
dnaString = []

count = 0
marker = '>'

for line in dataset:
    line = line.rstrip()
    if line.startswith(marker):
        dnaStringID.append(line.strip(marker))
        count += 1
    else:
        if len(dnaString) < count:
            dnaString.append(line)
        else:
            dnaString[count-1] = dnaString[count-1] + line

transitions = {'A':'G','G':'A','C':'T','T':'C'}

dnaString1 = dnaString[0]
dnaString2 = dnaString[1]

transitionsCount = 0
transversionsCount = 0
totalSubstitutions = 0

for i in range(len(dnaString1)):
    if dnaString1[i] != dnaString2[i]:
        if transitions[dnaString1[i]] == dnaString2[i]:
            transitionsCount += 1
        else:
            transversionsCount += 1
        totalSubstitutions += 1

print transitionsCount/float(transversionsCount)

##dataset
##>Rosalind_0209
##GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
##AGTACGGGCATCAACCCAGTT
##>Rosalind_2200
##TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
##GGTACGAGTGTTCCTTTGGGT

#answer = 2.27272727273
