import math
n=int(input())
g=math.sqrt(n)
print(g)
print(2==2.000000000000)
print(int(g))
if int(g)==g:
    print("perfect")
else:
    print("not perfect")
'''
input1:
4
output:
2.0
True
2
perfect

input2:
10
output:
3.1622776601683795
True
3
not perfect
'''

import math
n=int(input())
g=n**0.5
print(g)
print(2==2.000000000000)
print(int(g))
if g**2==n:
    print("perfect")
else:
    print("not perfect")

'''
input1:
4
output:
2.0
True
2
perfect

input2:
10
output:
3.1622776601683795
True
3
not perfect
'''
