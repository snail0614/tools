# -*- encoding=utf-8 -*-
import os, sys

def writefile(nameindex):
    try:
        rfile = open("C:/Users/Administrator/Desktop/abc.txt", "r")
        wfile = open("C:/Users/Administrator/Desktop/abc2.txt", "w")
    except IOError:
        print ("The file don't exist, Please double check!")
        exit()
    n = 0;
    AllLines = rfile.readlines()
    for EachLine in AllLines:
        if (n != nameindex):
            wfile.write(''+'\n')
            # print(n)
        else:
            wfile.write(EachLine)
        n=n+1
    rfile.close()
    wfile.close()

    S1 = wfile.closed
    if True == S1:
        print( 'the file is closed')
    else:
        print ('The file donot close')

if __name__ == "__main__":
    i=1
    writefile(i)