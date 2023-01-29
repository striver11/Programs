'''
You are driving a car to go to a destination .So while driving you will need to go sometimes forward some times right some times left
Dont worry ; There is NO GOING BACK

you will get a string of the road containing three symbols ("L" , "R" , " -.")
"L" : means you need to turn left
"R" : means you need to turn right
"-" : means you need to go forward

each "-" is a block
Input
a string R showing the road
Output
N lines: Each line is a string for the next action (N is the total number of actions).
Constraints
R is always a valid string of instruction and will not be empty or contain any invalid characters.
Example
Input
----R--R-L
Output
Go 4 blocks Forward
Turn Right
Go 2 blocks Forward
Turn Right
Go 1 blocks Forward
Turn Left
You ve reached your destination
'''


"""
from itertools import groupby
s=input()

for k,l in groupby(s):
    if k=="-":
        print(f"Go {len(list(l))} blocks forward")
        #print(f"Go {len(list(l))} blocks forward")
    elif k=="L":
        print("Turn Left")
    else:
        print("Turn Right")
print("You Ve reached your destination")
"""



"""
r = input()
while r:
    if r[0]=="R":print("Turn Right");r=r[1:]
    elif r[0]=="L":print("Turn Left");r=r[1:]
    else:print("Go",len(r)-len(r.lstrip("-")),"blocks Forward");r=r.lstrip("-")
print("You ve reached your destination")
"""



"""
s=input()
t=(s.replace("R"," R ").replace("L"," L ")).strip()
for i in t.split(" "):
    if i[-1]=="-":
        print(F"Go {len(i)} blocks Forward")
        print(f"Go {len(i)} blocks Forward") #above and below are the same
    elif i[0]=="R":
        print("Turn Right")
    else:
        print("Turn Left")
print("You Ve reached your destination")
"""


"""
s=input()
t=(s.replace("R"," R ").replace("L"," L ")).strip()
print(len(t))
for i in t.split():
    if i[0]=="-":
        print(f"Go {len(i)} blocks forward")
    elif i[0]=='L':
        print("Turn Left")
    else:
        print("Turn Right")
print("you have reached your destination")
"""
