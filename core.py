import argparse
from math import gcd



def get_pn_min(m, Rm, a, S):
    pn = [a]
    print(S)
    for i in range(S - 1):
        value = pn[i]*m % Rm
        pn.append(value)
    print(pn)
    return min(pn)


def convert_base(num, to_base=10, from_base=10):
    """ Function for convert numbers
    """
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


def compute_indexes(p, m, n, r):
    N = p**(m*n) - 1
    S = m*n
    l = int((p**S - 1) / (p**m - 1) + 1)

    if p > 2:
        C10 = [r + i*(p**m - 1) for i in range(l + 1)]
    elif p == 2:
        C10 = [r + 2*i*(p**m - 1) for i in range(l + 1)]
    
    rp = convert_base(C10[0], to_base=p)

    def gc(s):
        r = 0
        m = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "A": 10,
            "B": 11,
            "C": 12,
            "D": 13,
            "E": 14,
            "F": 15

        }
        for i in s:
            r += m[i]
        return r

    gr = gc(rp)
    match = []
    for c in C10:
        if c > N:
            break
        # print(c)
        cb = convert_base(c, to_base=p)
        if gc(cb) == gr:

            pSopr = [c]
            for i in range(S - 1):
                pSopr += [pSopr[i] * p % (p**S - 1)]
            # print( cb, gc(cb), gr, pSopr)
            pS = min(pSopr)
            if pS % 2 == 1:
                match += [pS]
    C10 = sorted(set(match))
    return C10, [convert_base(i, p) for i in C10]

def without_r(p, m, n):
    Rm = p**m - 1
    S = m * n
    r=[]
    
    # print([i for i in range(1, p**m - 1)])
    for n in range(1, p**m - 1):
        n_gcd=gcd(n, Rm)

        if n_gcd == 1:
            pn_min=get_pn_min(p, Rm, n, S)
            if pn_min == n:
                r.append(n)

    try:
        if r[0] == 1:
            r = r[1:]
    except:
        pass
    return r

def main(args):
    p=args["p"]
    m=args["m"]
    n=args["n"]

    if args["use_r"]:
        r=args["r"]
        return with_r(p, m, n, r)
    else:
        return without_r(p, m, n)


if __name__ == "__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--p", type=int, required=True, help="p - is prime number")
    ap.add_argument("--m", type=int, required=True, help="m from S=m*n")
    ap.add_argument("--n", type=int, required=True, help="m form S=m*n")
    ap.add_argument("--r", type=int, required=False, help="r")
    ap.add_argument("--use_r", type=bool, required=False, help="use r (1/0)")
    args=ap.parse_args()
    main(vars(args))
