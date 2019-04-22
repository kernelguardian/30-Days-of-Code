import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    bin_n=list(bin(n)[2:])
    #print(type(bin_n),bin_n)
    L1=0
    L2=0
    #bin_n_temp=bin_n
    #print(bin_n)
    for i in bin_n:
        #print(type(i),type('1'))
        if(i=='1'):
            L1=L1+1
            #print('L1',L1)
            L2=max(L1,L2)
        elif(i=='0'):
            #print("\nL2",L2)
            L2=max(L1,L2)
            L1=0
    print(L2)
