#!/bin/python

import getopt
import sys
import csv
# -l [1,2,3]
# -c [3,4,5]

class OPT(object):
    """
    """
    
    def __init__(self, argvs, options):
        """
        """
        optlist = None
        try:
            optlist, self._args = getopt.getopt(argvs, options)
        except getopt.GetoptError, e:
            print e
            sys.exit(-1)
        self._opts = {}
        for (switch,data) in optlist:
            self._opts[switch]=data
        print self._opts

    def getOption(self, option):
        if option in self._opts:
            return self._opts[option]
        else:
            return None
        
# if __name__ == '__main__':
#     opt = OPT(sys.argv[1:],"c:r:s")
#     print opt.getOption("-c")
#     print opt.getOption("-r")
#     print opt.getOption("-s")

if __name__ == '__main__':
    optlist, args = getopt.getopt(sys.argv[1:], 'c:r:')
    columns = []
    rows = []
    for (switch,data) in optlist:
        if switch=="-c":
            for col in data.split(","):
                columns.append(int(col))
        if switch=="-r":
            for row in data.split(","):
                rows.append(int(row))
    fileName = args[0]

    input_fd = open(fileName, "r")
    spamreader = csv.reader(input_fd, delimiter='~', quotechar='\"')
    k=1
    for row in spamreader:
        if k in rows:
            for h in columns:
                print row[h-1]+" ",
            print ""
        k = k+1
    input_fd.close()
