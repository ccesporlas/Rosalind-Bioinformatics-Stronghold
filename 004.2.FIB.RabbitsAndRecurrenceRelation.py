adultPairs = 1
youngPairs = 0

n = 36 #test 5
k = 2 #test 3
#expected test answer: 19

for i in range(n):
    if i > 0:
        newAdultPairs = youngPairs #growth
        youngPairs = adultPairs*k #reproduce
        adultPairs += newAdultPairs
    print str(i+1) + ' Adult = ' + str(adultPairs) + ' Young = ' + str(youngPairs)

##1 Adult = 1 Young = 0
##2 Adult = 1 Young = 3
##3 Adult = 4 Young = 3
##4 Adult = 7 Young = 12
##5 Adult = 19 Young = 21
