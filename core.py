import argparse
from math import gcd

def get_pn_min(m, Rm, a):
    pn = [a]
    for i in range(m - 1):
        value = pn[i]*m%Rm
        pn.append(value)
    print("Сопряжение=",pn, min(pn))
    return min(pn)

def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]

def main(args):
    p = args.p
    m = args.m
    n = args.n
    r = args.r
    N = p**(m*n) - 1

    Rm = p**m - 1
    print(f"parameters: p={p}, m={m}, n={n}, r={r}")
    S = m*n
    l = int((p**S - 1) / (p**m - 1) + 1)
    print(l)
    if p > 2:
        C10 = [r + i*(p**m - 1) for i in range(l + 1)]
    elif p == 2:
        C10 = [r + 2*i*(p**m - 1) for i in range(l + 1)]

    rp = convert_base(C10[0], to_base=p)


    def gc(s):
        r = 0
        for i in s:
            r += int(i)
        return r


    gr = gc(rp)
    match = []
    for c in C10:
        if c > N:
            break
        print(c)
        cb = convert_base(c, to_base=p)
        if gc(cb) == gr:
            
            pSopr = [c]
            for i in range(S - 1):
                pSopr += [pSopr[i] * p % (p**S - 1)]
            print( cb, gc(cb), gr, pSopr)
            pS = min(pSopr)
            if pS % 2 == 1:
                match += [pS]

    print(C10)
    print(sorted(set(match)))


    print(f"1. p^m-1={Rm}")
    r = []
    print([i for i in range(1, p**m - 1)])
    for n in range(1, p**m - 1):
        n_gcd = gcd(n, Rm)
        
        if n_gcd == 1:
            print(f"n={n}, НОД({n}, {Rm}) = {n_gcd}")
            pn_min = get_pn_min(m, Rm, n)
            if pn_min == n:
                r.append(n)
    print(f"2. R={r}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--p", type=int, required=True, help="p - is prime number")
    ap.add_argument("--m", type=int, required=True, help="m from S=m*n")
    ap.add_argument("--n", type=int, required=True, help="m form S=m*n")
    ap.add_argument("--r", type=int, required=False, help="r")
    args = ap.parse_args()
    main(args)
