#!/usr/bin/python

import sys
oldKey = None
HitCount=0
MaxHit=0
Popular=""
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
    thisKey, thisCount = data_mapped
    
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", HitCount
	if HitCount>MaxHit:
		MaxHit=HitCount
		Popular=oldKey
        oldKey = thisKey
	HitCount=0
    oldKey = thisKey
    HitCount+=int(thisCount)
    
    
if oldKey != None:
    print oldKey, "\t", HitCount
    if HitCount>MaxHit:
		MaxHit=HitCount
		Popular=oldKey
print Popular+"\t"+str(MaxHit)
