'''
#Functions

def f1():
    print("Hello Emmanuel")

f1() #function calling


#Calculator

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
x=int(input("Enter 1st number : "))
y=int(input("Enter 2nd number : "))

print(add(x,y))
print(sub(x,y))
print(mul(x,y))
print(div(x,y))
'''

#3) factorial
#3! = 1x2x3,    7!=1x2x3x4x5x6x7,      n!=1x2x3.......xn
n=int(input("Enter n : "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

#1x2x3x4x5 = 120

#4)Fibonacci series
# 0   1   1   2   3   5   8   13.....
'''
  x   y   z
      x   y   z


  '''
n=int(input("Enter n : "))        
x,y=0,1
print(x,end=" ")
print(y,end=" ")
for i in range(3,n+1):
    z=x+y
    print(z,end=" ")