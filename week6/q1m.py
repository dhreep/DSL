import sys
sep = '\t'
for line in sys.stdin:
    words = line.strip().split()
    for word in words:
        print("%s%s%d"%(word,sep,1))