from numpy import *

#dataset = open("rosalind_pdst.txt","r")
dataset = open("rosalind_pdst_2.txt","r")

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
#print dnaStringID
#print dnaString

dnaCount = len(dnaString)
distMatrix = zeros((dnaCount,dnaCount))

for i in range(dnaCount):
    for j in range(dnaCount):
        #distance matrix is symmetric along the diagonal
        #calculate for the upper half only (i<j)
        #and mirror the vlaues for the lower half
        if i < j:
            dna1,dna2 = dnaString[i],dnaString[j]
            dnaLen = len(dna1) #i and j have the same length
            distMatrix[i][j] = sum([1.0/dnaLen for k in range(dnaLen) if dna1[k] != dna2[k]])
        elif i > j:
            distMatrix[i][j] = distMatrix[j][i] 

for i in distMatrix:
    print ' '.join([str(j) for j in i])
