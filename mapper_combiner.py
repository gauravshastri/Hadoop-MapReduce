#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import datetime
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
	year, month, day = (int(x) for x in date.split('-'))
	ans=datetime.date(year, month, day)
	print ans.strftime("%A")+"\t"+cost

