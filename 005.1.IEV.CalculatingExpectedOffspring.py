pairPop = open("rosalind_iev.txt","r").read().rstrip().split()
pairDomProb = [1,1,1,0.75,0.5,0]
expOffspring = 0
for i,pair in enumerate(pairPop):
    expOffspring += 2*int(pair)*pairDomProb[i]
print expOffspring
