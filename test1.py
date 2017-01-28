#!/usr/bin/env python
#import sys
'''
Created on Jan 28, 2017
This code opens a text file and reads it, saving it to line and then printing it.
@author: rkbergsma
'''

f = open('Article1.txt','r')            #open to read

line = f.readlines()                    #reads all lines in file
#line = [x.strip() for x in line]       #strip gets rid of newline characters
#print(line)                            #prints as list with bad formatting
print(*line, end='\n')                  #print the text only in a list, can replace '\n' with ' '

f.close()
