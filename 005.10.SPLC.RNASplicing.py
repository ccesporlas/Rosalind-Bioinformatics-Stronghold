dataset = open("rosalind_splc.txt","r")
#dataset = open('test.txt','r')

def getFASTA(dataset):
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
    return dnaStringID,dnaString

def getRNA(dna):
    return dna.replace('T','U')

def getRNACodonMap():
    rnaCodonMapFile = open("rnacodons.txt","r")
    rnaCodonAminoAcidMap = {}
    for line in rnaCodonMapFile:
        translation = line.rstrip().split()
        rnaCodonAminoAcidMap[translation[0]] = translation[1]
    return rnaCodonAminoAcidMap

def getRNATranslation(rna):
    rnaTranslation = ''
    rnaCodonAminoAcidMap = getRNACodonMap()
    for i in range(0,len(rna)-1,3):
        aminoAcid = rnaCodonAminoAcidMap[rna[i:i+3]]
        if aminoAcid == 'Stop':
            break
        else:
            rnaTranslation += aminoAcid
    return rnaTranslation

dnaID,dna = getFASTA(dataset)
DNA = dna[0]
for i in dna[1:]:
    DNA = DNA.replace(i,'')
print getRNATranslation(getRNA(DNA))
