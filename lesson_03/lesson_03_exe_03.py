n=int(input("vvedite chislo: "))

for i in range(1,n//2+1):
    if not n%i:
        print(i, end=' ')
print(" - dilniki chisla ", n)

