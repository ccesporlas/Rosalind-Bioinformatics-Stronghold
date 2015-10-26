#   AA  Aa  aa
#AA 100 100 100
#Aa 100 75  50
#aa 100 50  0

k = 26.
m = 28.
n = 17.
t = k+m+n

Pkk = 1*1*(k/t)*((k-1)/(t-1))
Pkm = 2*1*(k/t)*(m/(t-1))
Pkn = 2*1*(k/t)*(n/(t-1))

Pmm = 1*0.75*(m/t)*((m-1)/(t-1))
Pmn = 2*0.5*(m/t)*(n/(t-1))

Ptot = Pkk + Pkm + Pkn + Pmm + Pmn
print Ptot


