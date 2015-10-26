dataset = open("rosalind_gc.txt","r")
#dataset = open("rosalind_ini7_test.txt","r")

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

dnaGcContent = []

for i in range(len(dnaStringID)):
    dnaStr = dnaString[i]
    gcContent = (dnaStr.count('G') + dnaStr.count('C'))*(100/float(len(dnaStr)))
    dnaGcContent.append(gcContent)
#print dnaGcContent

maxGcContent = max(dnaGcContent)
maxDnaID = dnaStringID[dnaGcContent.index(maxGcContent)]
print maxDnaID
print maxGcContent
