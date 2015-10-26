protSeq = open('rosalind_mrna.txt','r').read().strip()

def getRNACodonMap():
    rnaCodonMapFile = open("rnacodons.txt","r")
    rnaCodonAminoAcidMap = {}
    for line in rnaCodonMapFile:
        translation = line.rstrip().split()
        rnaCodonAminoAcidMap[translation[0]] = translation[1]
    return rnaCodonAminoAcidMap

rnaCodonAminoAcidMap = getRNACodonMap()
values = rnaCodonAminoAcidMap.values()
rnaStringsTotal = values.count('Stop')
for i in protSeq:
    rnaStringsTotal *= values.count(i)

print rnaStringsTotal % 1000000
