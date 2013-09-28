#!/usr/bin/env python
"""
class descriptions here
"""
import os
import sys
import getopt

class ClassName(object):
    def __init__(self, arg):
        pass

    def __del__(self):
        pass

    def foo1(self):
        """
        what does this foo1 do?
        """
        print "foo1"

    def foo2(self):
        """
        what does this foo2 do?
        """
        print "foo2"

def usage():
    import textwrap

    USAGE=textwrap.dedent("""\
        Usage:
            test.py [options]
        
        Options:
            -h
               Show a detailed help message
            -c 
               something here
        example:
            test.py -h 
            test.py -c
        """)

    print USAGE

def main():
    # Test cases here
    opts, args = getopt.getopt(sys.argv[1:], "hc", ["help", "run"])
    if not opts:
        usage()
        sys.exit(1)

    c1=ClassName(None)
    
    c1.foo1()
    c1.foo2()
    

if __name__ == "__main__":
    main()
