import argparse
from math import gcd

def get_pn_min(m, Rm, a):
    pn = [a]
    for i in range(m - 1):
        value = pn[i]*m%Rm
        pn.append(value)
    print("Сопряжение=",pn, min(pn))
    return min(pn)


def main(args):
    p = args.p
    m = args.m
    n = args.n
    r = args.r
    print(f"parameters: p={p}, m={m}, n={n}")
    Rm = p**m - 1
    print(f"1. p^m-1={Rm}")
    r = []
    print([i for i in range(1, p**m - 1)])
    for n in range(1, p**m - 1):
        print(f"Для n={n}")
        n_gcd = gcd(n, Rm)
        print(f"НОД({n}, {Rm}) = {n_gcd}")
        if n_gcd == 1:
            pn_min = get_pn_min(m, Rm, n)
            if pn_min == n:
                r.append(n)
        print('\n')
    print(f"2. R={r}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--p", type=int, required=True, help="p - is prime number")
    ap.add_argument("--m", type=int, required=True, help="m from S=m*n")
    ap.add_argument("--n", type=int, required=True, help="m form S=m*n")
    ap.add_argument("--r", type=int, required=False, help="r")
    args = ap.parse_args()
    main(args)