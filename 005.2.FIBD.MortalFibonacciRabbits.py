'''
Rosalind Bioinformatics Problem
Mortal Fibonacci Rabbits
http://rosalind.info/problems/fibd/

Example:
n=7, k=1, m=3
   month   | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
   young   | 1 | 0 | 1 | 1 | 1 | 2 | 2 |
new adults | 0 | 1 | 0 | 1 | 1 | 1 | 2 |
adultAgePop|0,0|0,1|1,0|0,1|1,1|1,1|1,2|
   adult   | 0 | 1 | 1 | 1 | 2 | 2 | 3 |
'''

n = 95 #total number of months ##n
k = 1 #number of rabbit offspring per rabbit pair
#expected test answer: 31746005499562581706 (young+adult)
##95 Adult = 19619529532959845082 Young = 12126475966602736624

m = 18 #rabbit lifespan ##m

adultAgePop = [0]*(m-1) #initial number of mature (capable of reproduction) rabbit pairs
young = 0 #initial number of young rabbit pairs
adult = 0 #initial number of adult rabbit pairs

for i in range(n):
    if i>0 :
        newAdults = young #growth
        young = adult*k #reproduce
        if m-1 > 1:
            adultAgePop = adultAgePop[1:] + [newAdults]
        else:
            adultAgePop = [newAdults]
        adult = sum(adultAgePop)
    else:
        young += 1

print str(i+1) + ' Adult = ' + str(adult) + ' Young = ' + str(young)


