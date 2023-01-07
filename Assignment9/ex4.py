import random
from multiprocessing import Pool
import argparse


def get_quarter_circle_hits(n: int) -> int:
    hits = 0
    for i in range(n):
        (x, y) = (random.random(), random.random())
        if x*x + y*y < 1:
            hits += 1
    return hits


parser = argparse.ArgumentParser()

parser.add_argument("-p", "--processes", type=int, default=1, help="number of processes")

parser.add_argument("-n", type=int, default=1000, help="checks per process")

args = parser.parse_args()

if __name__ == "__main__":
    N = args.processes * args.n

    arguments = [args.n]*args.processes

    with Pool(args.processes) as _pool:
        pool_returns = _pool.map(get_quarter_circle_hits, arguments) #imap and imap_unordered were much slower

    C = sum(pool_returns)

    pi_approx = 4*C/N

    print(f"{args.processes} processes with {args.n} checks each")
    print(f"total tries: {N}")
    print(f"total hits: {C}")
    print(f"pi approximation: {pi_approx}")
