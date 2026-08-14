from collections import deque
from math import sqrt, e as E
operations = ['+', '-', '*', '/'] 
nums = [0,1,2,3,4,5,6,7,8,9,10]

found = False
def solve(target):
    dobfs(target)
    # for i in range(1,6):
    #     dobfs(i,target,f"{i}",depth=0)


def dodfs(inp,tar,opstr,depth=0):
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
        dodfs(E**inp,tar,f"(e^({opstr}))",depth+1)
    if inp>0:
        dodfs(sqrt(inp),tar,f"sqrt({opstr})",depth+1)
    for i in nums:
        dodfs(inp+i,tar,f"({opstr}+{i})",depth+1)
        dodfs(inp-i,tar,f"({opstr}-{i})",depth+1)
        dodfs(inp*i,tar,f"({opstr}*{i})",depth+1)
        if i != 0:
            dodfs(inp/i,tar,f"({opstr}/{i})",depth+1)
        

def dobfs(target):
    queue = deque((i,target, f"{i}", 0) for i in nums)
    seen = set()
    while len(queue) != 0:
        inp,tar,opstr,depth = queue.popleft()
        if inp in seen:
            continue
        else:
            seen.add(inp)
        if depth == 5:
            continue
        elif abs(inp - tar) < 0.0001:
            print(opstr)
            return
        
        if inp < 22:
            queue.append((E**inp,tar,f"(e^({opstr}))",depth+1))
        if inp>0:
            queue.append((sqrt(inp),tar,f"sqrt({opstr})",depth+1))
        
        for i in nums:
            queue.append((inp+i,tar,f"({opstr}+{i})",depth+1))
            queue.append((inp-i,tar,f"({opstr}-{i})",depth+1))
            queue.append((inp*i,tar,f"({opstr}*{i})",depth+1))
            if i != 0:
                queue.append((inp/i,tar,f"({opstr}/{i})",depth+1))
    
    print("Not Found")
    return