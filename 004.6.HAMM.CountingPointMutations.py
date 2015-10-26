s,t = open('rosalind_hamm.txt').read().rstrip().split('\n')
print len([i for i in range(len(s)) if s[i] != t[i]])
