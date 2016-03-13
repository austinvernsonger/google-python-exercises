    #!/usr/bin/python

import sys

def main():
    if len(sys.argv) != 2:
        print 'usage: ./unique.py %s' % ('"string"')
        sys.exit(1)
    index = {}
    str = sys.argv[1]
    for c in str:
        if c in index:
            print "\"%s\" not unique: %c repeated" % (str, c)
            sys.exit(1)
        else:
            index[c]= 1
    print "\"%s\" is unique" % (str)
    return

if __name__ == '__main__':
    main()

