#/usr/bin/env python3
import sys


def primefactor(b):
    if b <= 3:
        return int(b)
    if b % 2 == 0:
        return 2
    elif b % 3 == 0:
        return 3
    else:
        for a in range(5, int((b)**0.5) + 1, 6):
            if b % a == 0:
                return int(a)
            if b % (a + 2) == 0:
                return primefactor(b/(a+2))
    return int(b)


print(primefactor(int(sys.argv[1])))
