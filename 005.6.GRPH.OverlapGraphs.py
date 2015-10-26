dataset = open("rosalind_grph.txt","r")

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
dataset.close()

#print dnaStringID
#print dnaString

nodeCount = len(dnaString)

k = 3

for i in range(nodeCount):
    for j in range(nodeCount):
        iPref = dnaString[i][:k]
        iSuff = dnaString[i][::-1][:k][::-1]
        #comment this out - directed graph only!
        #jPref = dnaString[j][:k]
        #jSuff = dnaString[j][::-1][:k][::-1]
        #or jSuff == iPref
        if i != j and iSuff == jPref:
            print dnaStringID[i] + ' ' + dnaStringID[j]
