import bruteforce as bf
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            target = float(sys.argv[1])
            layers = int(sys.argv[2])
            bf.solve(target,layers)
        except ValueError:
            print("Please provide a valid number")
    else:
        print("Please provide a number")