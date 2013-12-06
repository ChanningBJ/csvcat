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
        print self._args

    def getOption(self, option):
        if option in self._opts:
            return self._opts[option]
        else:
            return None

    def getArgs(self,):
        return self._args
        
import re
def parseColumnRowNumber(optstr):
    """
    """
    numberSet = set()
    rangeRe = re.compile("\[(\w+)-(\w+)\]")
    for item in optstr.split(","):
        regGroup = rangeRe.match(item)
        if regGroup is None:
            try:
                numberSet.add(int(item))
            except ValueError,e:
                print e
                sys.exit(-1)
        else:
            (start,end) = regGroup.groups()
            numberSet = numberSet | set(range(int(start),int(end)+1))
    return sorted(numberSet)
    
            
        
    
    
# if __name__ == '__main__':
#     opt = OPT(sys.argv[1:],"c:r:s")
#     print opt.getOption("-c")
#     print opt.getOption("-r")
#     print opt.getOption("-s")
# [2-4],3,4,5,6,[8-9]
if __name__ == '__main__':
    opt = OPT(sys.argv[1:],"c:r:")
    
    columnStr = opt.getOption("-c")
    if columnStr is None or columnStr=="":
        print "Need use -c to specify the columns"
        sys.exit(-1)
    columns = parseColumnRowNumber(columnStr)

    rowStr = opt.getOption("-r")
    if rowStr is None or rowStr=="":
        print "Need use -r to specify the rows"
        sys.exit(-1)
    rows = parseColumnRowNumber(rowStr)

    fileName = opt.getArgs()[0]

    input_fd = open(fileName, "r")
    spamreader = csv.reader(input_fd, delimiter=',', quotechar='\"')
    k=1
    for row in spamreader:
        if k in rows:
            rowLen = len(row)
            for h in columns:
                if h<rowLen:
                    print row[h-1]+" ",
                else:
                    print None," ",
            print ""
        k = k+1
    input_fd.close()
