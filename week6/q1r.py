from itertools import groupby
from operator import itemgetter
import sys


def rmo(file: str, sep='\t'):
    for line in file:
        yield line.rstrip().split(sep, 1)


def main(sep='\t'):
    data = rmo(sys.stdin, sep='\t')
    print(groupby(data, itemgetter(0)))
    for cw, g in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for cw, count in g)
            print("%s%s%d" % (cw, sep, total_count))
        except ValueError:
            pass


if __name__ == "__main__":
    main()
