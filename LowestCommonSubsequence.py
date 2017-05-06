#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 21:59:52 2017

@author: kunal
"""
def lcs(x,y):

    m=len(x) + 1 ##for x
    n=len(y) + 1 ## for y
    
    c=[[(i+1) for i in range(m)]for j in range(n)]
    b=[[i for i in range(1,m)]for j in range(1,n)]
    for i in range(m):
        c[0][i]=0
    
    for i in range(n):
        c[i][0]=0
    
    for i in range(1,m):
        for j in range(1,n):
            if(x[i-1]==y[j-1]):
                c[j][i]=c[j-1][i-1] + 1
                b[j-1][i-1]='NW'# NW just for showing NorthWest arrow u can simply use arrow sign
            elif c[j-1][i]>=c[j][i-1]: 
                
                c[j][i]=c[j-1][i]
                b[j-1][i-1]='S' #S for arrow in SOUTH Direction 
            else:
                c[j][i]=c[j][i-1]
                b[j-1][i-1]='W' # for arrow in WEST direction
    return c and b
                
def Print(b,y,i,j):
    """b=lcs(x,y) as y is taken in row side so we use y in calling Print sin
    since as we are decreasing row wise so we use y
    Print(b,y,len(b)-1,len(b[0])-1)"""
    if i<0 or j<0:
        return
    if b[i][j]=='NW':
        
        Print(b,y,i-1,j-1)
        print(y[i])
    elif b[i][j]=='S':#S for arrow in south direction
        Print(b,y,i-1,j)
    else:Print(b,y,i,j-1)
    
