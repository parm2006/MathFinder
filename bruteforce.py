from math import sqrt
from math import e as E
operations = ['+', '-', '*', '/'] 
nums = [0,1,2,3,4,5,6,7,8,9,10]

found = False
def solve(target):
    for i in range(1,6):
        do(i,target,f"{i}",depth=0)


def do(inp,tar,opstr,depth=0):
    global found
    if depth == 5:
        return
    if found == True:
        return
    elif inp == tar:
        found = True
        print(opstr)
        return
    
    if inp < 22:
        do(E**inp,tar,f"(e^({opstr}))",depth+1)
    if inp>0:
        do(sqrt(inp),tar,f"sqrt({opstr})",depth+1)
    for i in nums:
        do(inp+i,tar,f"({opstr}+{i})",depth+1)
        do(inp-i,tar,f"({opstr}-{i})",depth+1)
        do(inp*i,tar,f"({opstr}*{i})",depth+1)
        if i != 0:
            do(inp/i,tar,f"({opstr}/{i})",depth+1)
        
