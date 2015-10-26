rnaCodonMapFile = open("rnacodons.txt","r")

rnaCodonAminoAcidMap = {}
for line in rnaCodonMapFile:
    translation = line.rstrip().split()
    rnaCodonAminoAcidMap[translation[0]] = translation[1]
#print rnaCodonAminoAcidMap
#print len(rnaCodonAminoAcidMap)

dataset = open("rosalind_prot.txt","r")
#dataset = open("rosalind_ini10_test.txt","r")

for line in dataset:
    line = line.rstrip()
    rnaTranslation = ''
    for i in range(0,len(line)-1,3):
        aminoAcid = rnaCodonAminoAcidMap[line[i:i+3]]
        if aminoAcid == 'Stop':
            break
        else:
            rnaTranslation += aminoAcid
    print rnaTranslation
dataset.close()
