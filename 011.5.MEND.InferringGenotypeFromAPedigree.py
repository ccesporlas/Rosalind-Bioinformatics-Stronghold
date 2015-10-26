import numpy
from Bio import Phylo
from cStringIO import StringIO
import itertools

def genotypeProbability(genotype):
    #   AA Aa aa (genotypes)
    #   0  1  2  (# of recessive allele a)
    #AA 1  0  0  (prob of getting 0,1,2 a allele in AA)
    #Aa 0  1  0  (prob of getting 0,1,2 a allele in Aa)
    #aa 0  0  1  (prob of getting 0,1,2 a allele in aa)
    return numpy.array([int(genotype.count('a') == i) for i in range(3)])

def childGenotypeProbability(p1,p2):
    ##Given AA,Aa,aa prob for parents p1 and p2
    ##Prob of child getting genotype:
    
    #AA             #Aa             #aa
    #   AA  Aa   aa #   AA  Aa  aa  #   AA Aa   aa
    #AA 1   0.5  0  #AA 0   0.5 1   #AA 0  0    0
    #Aa 0.5 0.25 0  #Aa 0.5 0.5 0.5 #Aa 0  0.25 0.5
    #aa 0   0    0  #aa 1   0.5 0   #aa 0  0.5  1

    PAA = [[1.0,0.5,0.0],[0.5,0.25,0.0],[0.0,0.0,0.0]]
    PAa = [[0.0,0.5,1.0],[0.5,0.5,0.5],[1.0,0.5,0.0]]
    Paa = [[0.0,0.0,0.0],[0.0,0.25,0.5],[0.0,0.5,1.0]]

    AA,Aa,aa = 0,0,0
    for i in range(3):
        for j in range(3):
            AA += p1[i]*p2[j]*PAA[i][j]
            Aa += p1[i]*p2[j]*PAa[i][j]
            aa += p1[i]*p2[j]*Paa[i][j]

    return numpy.array([AA,Aa,aa])

nwck = open('rosalind_mend.txt').read().rstrip()
'''
Calculate prob per parent pair starting from all terminals/leaves
and work your way up to each level per pair of parents
Store AA,Aa,aa probabilities as clade names
test = ((((Aa,aa),(Aa,Aa)),((aa,aa),(aa,AA))),Aa);
9nodes: AA, aa, Aa, Aa, aa, aa, aa, AA, Aa
5nodes: AA-aa, Aa-Aa, aa-aa, aa-AA, Aa
3nodes: AAaa-AaAa, aaaa-aaAA, Aa
2nodes: AAaaAaAa-aaaaaaAA, Aa
1node: AAaaAaAaaaaaaaAA-Aa
'''
#nwck = open('rosalind_.txt').read().rstrip()
tree = Phylo.read(StringIO(nwck),'newick')
currNodes = tree.get_terminals()
for i in currNodes:
    i.name = genotypeProbability(i.name)

pairedNodes = []
nextNodes = []

while len(currNodes) > 1:
    currNodesLen = len(currNodes)
    for i in range(currNodesLen):
        A = currNodes[i]
        withPair = False
        if A in pairedNodes:
            continue
        for j in range(currNodesLen):
            if i < j:
                B = currNodes[j]
                trace = tree.trace(A,B)
                if len(trace) == 2:
                    trace[0].name = childGenotypeProbability(A.name,B.name)
                    nextNodes.append(trace[0])
                    pairedNodes.append(A)
                    pairedNodes.append(B)
                    withPair = True
        if not withPair:
            nextNodes.append(A)
    currNodes,pairedNodes,nextNodes = nextNodes,[],[]
    #print [i.name for i in currNodes]

print ' '.join([str(i) for i in currNodes[0].name])
