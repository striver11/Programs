
'''
Test 1
Input
Expected output
3837339789
9873333789
02
 
Test 2
Input
Expected output
6834866643
8664334668
03
 
Test 3
Input
Expected output
7777777777777
7777777777777
04
 
Test 4
Input
Expected output
23124134334
43321412334
05
 
Test 5
Input
Expected output
3518587137
8753113578
06
 
Test 6
Input
Expected output
58232328523232
85332222223358

'''

'''
s=list(input())
l=sorted(s[0:len(s)//2])
print(l)
v=sorted(s[len(s)//2:])
print(v)
if l==v:
    print("".join(v+l[::-1]))
    print("".join(l[::-1]+v))
'''

'''
n = inptu()
res = ''
for i in sorted(set(n),reverse=True):
    res+=i*(n.count(i)//2)
g=res+res[::-1]
print(g)
'''
