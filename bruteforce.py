from collections import deque
from math import sqrt, e as E,log,sin,cos,tan
operations = ['+', '-', '*', '/'] 
nums = [0,1,2,3,4,5,6,7,8,9,10]

found = False
def solve(target,layers):
    iterative_dfs(target,layers)

    #dobfs(target)
    
    # for i in range(1,6):
    #     dodfs(i,target,f"{i}",depth=0)


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

def iterative_dfs(target,layers):
    global found
    
    for i in range(1,layers+1): #layers
        seen = {}
        print("Layer : ",i)
        for j in range(0,6): #initial nums
            seen[j] = 0
            exp = dodfs(j,target,f"{j}",seen, depth=0,depthlimit=i)
            if exp != None:
                print(exp)
                return
    print("Not Found")
    return

def dodfs(inp,tar,opstr,seen, depth=0,depthlimit=0):
    if abs(inp - tar) < 0.0000000001:
        return opstr
    if depth >= depthlimit:
        return None

    def try_op(res, new_opstr):
        next_depth = depth + 1
        if res not in seen or next_depth < seen[res]:
            seen[res] = next_depth
            return dodfs(res, tar, new_opstr, seen, next_depth, depthlimit)
        return None
    
    if inp < 22:
        ret = try_op(E**inp, f"(e^({opstr}))")
        if ret != None:
            return ret
    if inp > 0:
        ret = try_op(sqrt(inp), f"sqrt({opstr})")
        if ret != None:
            return ret
        ret = try_op(log(inp), f"log({opstr})")
        if ret != None:
            return ret
    ret = try_op(sin(inp), f"sin({opstr})")
    if ret != None:
        return ret
    ret = try_op(cos(inp), f"cos({opstr})")
    if ret != None:
        return ret
    ret = try_op(tan(inp), f"tan({opstr})")
    if ret != None:
        return ret
    for i in nums:
        ret = try_op(inp + i, f"({opstr}+{i})")
        if ret != None:
            return ret
        ret = try_op(inp - i, f"({opstr}-{i})")
        if ret != None:
            return ret
        ret = try_op(inp * i, f"({opstr}*{i})")
        if ret != None:
            return ret
        if i != 0:
            ret = try_op(inp / i, f"({opstr}/{i})")
            if ret != None:
                return ret
    return None
        
