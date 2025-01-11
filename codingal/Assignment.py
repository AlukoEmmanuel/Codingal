#simple if : 1 situation



points = int(input("Enter your points :"))
if points>100:
    print("you are qulified")

n=int(input("Enter number:"))
if n%2==0:
    print(n,"is even")
else:
    print(n,"is odd")

n=int(input("Enter nunber:"))
if n%2==0:
    if n>0:
        print(n,"is even positive")
    else:
        print(n,"is even negative")
else:
    if n>0:
         print(n,"is odd positive")
    else:
         print(n,"is odd negative")

per=int(input("Enter percentage :"))
if per<33:
    grade="F"
elif per<50:
    grade="D"
elif per<70:
    grade="C"
elif per<90:
    grade="B"
else:
    grade="A"
print(grade)

