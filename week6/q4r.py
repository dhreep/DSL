from itertools import groupby
from operator import itemgetter
import sys
import pandas as pd


def main(sep='\t'):
    odd = 0
    even = 0

    for line in sys.stdin:
        try:
            a = int(line.strip())
            if a % 2 == 0:
                even += 1
            else:
                odd += 1
        except ValueError:
            continue
    print("Total Even Numbers:", even)
    print("Total Odd Numbers:", odd)


if __name__ == "__main__":
    main()
