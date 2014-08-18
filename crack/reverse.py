#!/usr/bin/python
# Simple Algorithm To Reverse A String

import sys

def main():
    if len(sys.argv) != 2:
        print 'usage: ./reverse.py %s' % ('"string"')
        sys.exit(1)
    index = {}
    str = sys.argv[1]
    rev= ""
    for c in str:
        rev = c + rev     
    print rev
    return rev

if __name__ == '__main__':
    main()

