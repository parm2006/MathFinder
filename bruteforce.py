from collections import deque
import heapq
from math import sqrt, e as E,log,sin,cos,tan
operations = ['+', '-', '*', '/'] 
nums = [0,1,2,3,4,5,6,7,8,9,10]

found = False
def solve(target,layers):
    #dobeam(target,layers)
    
    iterative_dfs(target,layers)

    #dobfs(target)
    
    # for i in range(1,6):
    #     dodfs(i,target,f"{i}",depth=0)

def dobeam(target,width): #dist, value,target,opstr,depth
    min_heap = [(abs(i - target), i, target, f"{i}", 0) for i in nums]
    heapq.heapify(min_heap)
    seen = {round(i, 8) for i in nums}
    while len(min_heap) != 0:
        dist, inp, tar, opstr, depth = heapq.heappop(min_heap)
        if depth == 5:
            continue
        elif dist <= 0.00000001:
            print(opstr)
            return
        
        def try_op(res, new_opstr):
            r_res = round(res, 8)
            if r_res not in seen:
                seen.add(r_res)
                d = abs(res - tar)
                heapq.heappush(min_heap, (d, res, tar, new_opstr, depth + 1))
                if len(min_heap) > width:
                    worst_idx = max(range(len(min_heap)), key=lambda idx: min_heap[idx][0])
                    worst_item = min_heap.pop(worst_idx)
                    heapq.heapify(min_heap)
                    seen.discard(round(worst_item[1], 8))
        
        if inp < 22:
            try_op(E**inp, f"(e^({opstr}))")

        if inp > 0:
            try_op(sqrt(inp), f"sqrt({opstr})")

            try_op(log(inp), f"log({opstr})")

        try_op(sin(inp), f"sin({opstr})")
        try_op(cos(inp), f"cos({opstr})")
        try_op(tan(inp), f"tan({opstr})")
        
        for i in nums:
            if i != 0:
                try_op(inp / i, f"({opstr}/{i})")
            try_op(inp + i, f"({opstr}+{i})")
            try_op(inp - i, f"({opstr}-{i})")
            try_op(inp * i, f"({opstr}*{i})")
            
    
    print("Not Found")
    return

def dobfs(target):
    queue = deque((i,target, f"{i}", 0) for i in nums)
    seen = set()
    while len(queue) != 0:
        inp,tar,opstr,depth = queue.popleft()
        if depth == 5:
            continue
        elif abs(inp - tar) < 0.0000000001:
            print(opstr)
            return
        
        def try_op(res, new_opstr):
            if res not in seen:
                seen.add(res)
                queue.append((res, tar, new_opstr, depth + 1))

        if inp < 22:
            try_op(E**inp, f"(e^({opstr}))")
        if inp > 0:
            try_op(sqrt(inp), f"sqrt({opstr})")
            try_op(log(inp), f"log({opstr})")
        try_op(sin(inp), f"sin({opstr})")
        try_op(cos(inp), f"cos({opstr})")
        try_op(tan(inp), f"tan({opstr})")
        for i in nums:
            try_op(inp + i, f"({opstr}+{i})")
            try_op(inp - i, f"({opstr}-{i})")
            try_op(inp * i, f"({opstr}*{i})")
            if i != 0:
                try_op(inp / i, f"({opstr}/{i})")
    
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
        
