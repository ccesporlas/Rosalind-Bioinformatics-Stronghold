dataset = open("rosalind_tree.txt","r")
#dataset = open("rosalind_tree_2.txt","r")
#dataset = open("minTree.txt","r")

totalNodes = int(dataset.readline().rstrip())
totalEdges = len(dataset.read().rstrip().split('\n'))
minEdges = totalNodes-1
print minEdges - totalEdges

'''
nodes = 0
treesNodesTemp = []
nodeList = []
lineCount = 0
for line in dataset:
    if lineCount == 0:
        nodes = int(line.rstrip())
    else:
        pair = line.rstrip().split()        
        nodeList = list(set(nodeList + pair))

        createNewTree = True
        if len(treesNodesTemp) > 0:
            a,b = pair
            for tree in treesNodesTemp:
                if a in tree or b in tree:
                    tree = list(set(tree + pair))
                    createNewTree = False
                    break
                else:
                    continue
        if createNewTree:
            treesNodesTemp.append(pair)
                
    lineCount += 1
dataset.close()

#print nodes
#print adjList
#print nodeList
#print treesNodesTemp

#number of nodes that are not connected
#minimum #edges for n nodes = n-1
unlinkedTot = nodes - len(nodeList)
unlinkedEdges = unlinkedTot-1 if unlinkedTot > 0 else 0
                                
print 'Total expect nodes: ' + str(nodes) + '\t Min total edges: ' + str(nodes-1)
print 'Total linked nodes: ' + str(len(nodeList)) + '\t Existing #edges: ' + str(lineCount-1)
print 'Total unlinked nodes: ' + str(unlinkedTot) + '\t Min #edges to make tree from unlinked nodes: ' + str(unlinkedEdges)

treeCount = len(treesNodesTemp) + 1 if unlinkedTot > 0 else len(treesNodesTemp)
print 'Total existing trees: ' + str(treeCount) + '\t Min edges to connect trees: ' + str(treeCount-1)

addEdgeCount = (treeCount - 1) + unlinkedEdges
print 'addEdgeCount = Min #edges to make tree from unlinked nodes + Min edges to connect trees'
print 'addEdgeCount ' + str(addEdgeCount)

#Below is the correct formula. To check: why is the addEdgeCount algorithm wrong?
print 'Min total edges - Existing #edges = ' + str((nodes-1) - (lineCount-1))
'''
