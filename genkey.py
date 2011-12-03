#! /usr/bin/python
import string
from random import choice
import sys

def main():
    USAGE_MSG = 'usage: "genkey length" where length is an ingeter in the range 0 ~ 1024'
    s = string.letters + string.digits
    if not (len(sys.argv) == 2 and sys.argv[1].isdigit() and int(sys.argv[1]) in range(0, 1025)):
        print USAGE_MSG
    else:
        print ''.join([choice(s) for _ in range(0, int(sys.argv[1]) + 1)])

if __name__ == '__main__':
    main()
