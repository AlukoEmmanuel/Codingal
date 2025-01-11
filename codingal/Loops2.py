N=int(input("Enter N:"))
c=0
for i in range(1,N+1):
    if N%i==i:
        c+=1
if c==2:
    print(N,"is Prime")
else:
    print(N,"is composite")
