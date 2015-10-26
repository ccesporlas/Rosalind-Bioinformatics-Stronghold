import numpy as np
from Bio import Phylo
from cStringIO import StringIO

dataset = open('rosalind_nwck.txt').read().rstrip().split('\n\n')
#dataset = open('test.txt').read().rstrip().split('\n\n')
distance = []

for i in dataset:
    nwck,nodePair = i.split(';\n')
    tree = Phylo.read(StringIO(nwck),'newick')
    node1,node2 = nodePair.split()
    #print tree    

    ancestor = tree.common_ancestor(node1,node2)
    ancPath1 = tree.trace(ancestor,node1)
    ancPath2 = tree.trace(ancestor,node2)
    dist = (len(ancPath1)-1)+(len(ancPath2)-1)
    #print ancestor, dist

    distance.append(str(dist))

print ' '.join(distance)
