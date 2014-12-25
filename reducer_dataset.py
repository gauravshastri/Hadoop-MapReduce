#!/usr/bin/python

import sys

aString = "A" # for USER records
bString = "B" # for POST records

userArray=[None]*5
Array=[None]*13
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if (len(data_mapped) == 6):
	for i in range(6):
            if (i == 0):
                userArray[i] = data_mapped[i]
            elif (i == 1):
                pass
            else:
                userArray[i - 1] = data_mapped[i]
    elif (len(data_mapped) == 10):
	if (data_mapped[0] != userArray[0]):
        	continue
	for i in range(5):	
		Array[i]=userArray[i]
	i=5
	j=2
	while (i<=12 and j<=9): 
		    Array[i]=data_mapped[j]
		    i+=1
		    j+=1
	for i in range(12):
        	print str(Array[i]) + "\t",
	print str(Array[12])
