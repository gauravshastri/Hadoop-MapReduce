#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip, identity, username, time1, time2, method, page, protocol, status, size = data
	print ip+"\t1"

