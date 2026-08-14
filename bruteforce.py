from bruteforce import found
from math import sqrt
from math import e as E
operations = ['+', '-', '*', '/'] 
nums = [1,2,3,4,5]

found = False
def solve(target):
    for i in range(1,6):
        do(i,target,"i")


def do(inp,tar,opstr):
    print(opstr)
    global found

    if found == True:
        return
    elif inp == tar:
        found = True
        print(opstr)
        return
    for i in nums:
        do(inp+i,tar,opstr+"+i")
        do(inp-i,tar,opstr+"-i")
        do(inp*i,tar,opstr+"*i")
        do(inp/i,tar,opstr+"/i")
        do(E**inp,tar,"e^("+opstr+")")
        if inp>0:
            do(sqrt(inp),tar,"sqrt("+opstr+")")
