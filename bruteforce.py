from collections import deque
from math import sqrt, e as E,log,sin,cos,tan
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
    count = 0
    while len(queue) != 0:
        inp,tar,opstr,depth = queue.popleft()
        if depth == 5:
            continue
        elif abs(inp - tar) < 0.0000000001:
            print(opstr)
            print(count)
            return
        
        if inp < 22:
            res = E**inp
            count+=1
            if res not in seen:
                count-=1
                seen.add(res)
                queue.append((res,tar,f"(e^({opstr}))",depth+1))
        if inp>0:
            res = sqrt(inp)
            count+=1
            if res not in seen:
                count-=1
                seen.add(res)
                queue.append((res,tar,f"sqrt({opstr})",depth+1))
            res = log(inp)
            count+=1
            if res not in seen:
                count-=1
                seen.add(res)
                queue.append((res,tar,f"log({opstr})",depth+1))
        res = sin(inp)
        count+=1
        if res not in seen:
            count-=1
            seen.add(res)
            queue.append((res,tar,f"sin({opstr})",depth+1))
        res = cos(inp)
        count+=1
        if res not in seen:
            count-=1
            seen.add(res)
            queue.append((res,tar,f"cos({opstr})",depth+1))
        res = tan(inp)
        count+=1
        if res not in seen:
            count-=1
            seen.add(res)
            queue.append((res,tar,f"tan({opstr})",depth+1))
        for i in nums:
            res = inp+i
            count+=1
            if res not in seen:
                count-=1
                seen.add(res)
                queue.append((res,tar,f"({opstr}+{i})",depth+1))
            res = inp-i
            count+=1
            if res not in seen:
                count-=1
                seen.add(res)
                queue.append((res,tar,f"({opstr}-{i})",depth+1))
            res = inp*i
            count+=1
            if res not in seen:
                count-=1
                seen.add(res)
                queue.append((res,tar,f"({opstr}*{i})",depth+1))
            if i != 0:
                res = inp/i
                count+=1
                if res not in seen:
                    count-=1
                    seen.add(res)
                    queue.append((res,tar,f"({opstr}/{i})",depth+1))
    
    print("Not Found")
    return