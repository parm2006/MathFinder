import time
import bruteforce as bf
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            target = float(sys.argv[1])
            layers = int(sys.argv[2])
            
            start_time = time.perf_counter()
            bf.solve(target,layers)
            elapsed = time.perf_counter() - start_time
            print(f"Time taken: {elapsed:.4f}s")
        except ValueError:
            print("Please provide a valid number")
    else:
        print("Please provide a number")