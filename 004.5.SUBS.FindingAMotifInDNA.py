s,t = open('rosalind_subs.txt').read().rstrip().split('\n')
print ' '.join([str(i+1) for i in range(len(s)) if s[i:].startswith(t)])
