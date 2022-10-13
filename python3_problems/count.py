#!/usr/bin/env python3
# EAA 10.12.2022

import sys 

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

print(list(range(num1, num2)))

for num in range(num1, num2):
	if num%2 != 0:
		print(num)
