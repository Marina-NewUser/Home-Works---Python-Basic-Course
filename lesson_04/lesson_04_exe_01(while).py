a=list(map(int,input('Vvedite elementi spiska cherez probel: ').split()))
n=0
dov=len(a)
s=0

while n<dov:
    s += a[n]
    n+=1

print('Summa elementov spiska: ',s)
