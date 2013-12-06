#!/bin/python

import getopt
import sys
import csv
# -l [1,2,3]
# -c [3,4,5]

class OPT(object):
    """
    """
    
    def __init__(self, argvs, options, defaultValue):
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
        for (switch,data) in defaultValue:
            self._opts[switch]=data

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
    
            
        
    
    
if __name__ == '__main__':
    opt = OPT(sys.argv[1:],"c:r:d:q:h",[("-d",","),("-q","\"")])
    if opt.getOption("-h") is not None:
        print """
        Usage:
           -c column numbers in this format [4-7],[9-10],11,24
           -r row numbers in this format [4-7],[9-10],11,24
           -d delimiter (default ,)
           -q quote char (default ")
        Example:
           csvcat.py -c "[4-7],[9-10]" -r "[1-4],6" test.csv
        """
        sys.exit(0)
    user_delimiter=opt.getOption("-d")
    user_quotechar=opt.getOption("-q")
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
    spamreader = csv.reader(input_fd, delimiter=user_delimiter, quotechar=user_quotechar)
    k=1
    for row in spamreader:
        if k in rows:
            rowLen = len(row)
            for h in columns:
                if h<rowLen:
                    print row[h-1]+" ",
            print ""
        k = k+1
    input_fd.close()
