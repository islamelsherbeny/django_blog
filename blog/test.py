
import unicodecsv


with open('com.csv', 'rb') as f:
    reader = list(unicodecsv.DictReader(f))

totals=[]
coms = []
exps=[]
print(reader)
for i in reader :
    for d in i.values() :
        totals.append(d)
        


print(totals)
k=0
while k <= len (totals)-1:
    coms.append(totals[k])
    k+=2

k=1
while k <= len (totals)-1:
    exps.append(totals[k])
    k+=2

print(coms)
print(exps)