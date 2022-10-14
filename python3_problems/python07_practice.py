#!/usr/bin/env python3
# EAA 10.13.2022

#import packages
import re

# nobody
with open("Python_07_nobody.txt", "r") as py7no_read:
	for line in py7no_read:
		line = line.rstrip()
		for nobody in  re.finditer(r'Nobody', line):
			n1 = nobody.group(0)
			position = nobody.start(0) + 1
			print(n1, position)

# nobody switch with hendrix





			
