n=int(input())
s=0
g=n
while n>0:
    r=n%10
    s=s+r
    n=n//10
if g>0:
    if s%3==0:
        print("true")
    else:
        print("false")
else:
    print("no negative numbers")
