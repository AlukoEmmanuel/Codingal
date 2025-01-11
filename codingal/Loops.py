#1)The table of N

'''

i N=3

1 x N

2 x N

3 x N

. x N

.

.

10 x N
'''
N=int(input("Enter N : "))

for i in range(1,11):

    print(N,"x",i,"=",N*i)



#2) Summation of N natural numbers :

'''

sum=0

sum=sum+i

i sum

1 0 +1=1

2 1+2=3

3 3+3=6

4 6+4=10

.

.

'''

sum=0

N=int(input("Enter N:"))

for i in range(1,N+1):

    sum=sum+i

print(sum)




N=int(input("Enter N:"))
c=0
for i in range(1,N+1):
    if N%i==i:
        c+=1
if c==2:
    print(N,"is Prime")
else:
    print(N,"is composite")
