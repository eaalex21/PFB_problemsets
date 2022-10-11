#!/usr/bin/env python3
# import modules
import sys

practice = 12
print(practice) # check to see if creating variable worked
if practice > 50:
  print('True') 
else:
  print('Not True')

#second if/else
x = 55
print(x) # check variable made 
if x > 0:
  if x <= 50:
    if (x % 2) == 0: 
      print('it is an even number that is smaller than 50')
    else:
      print('it is an odd number that is smaller than 50')
  else:
    print ('Larger than 50')
    if (x % 3) == 0:
      print('it is larger than 50 and divisible by 3')
    else:
      print('it is larger than 50 and not divisible by 3')
elif x == 0:
  print ('0')
else:
  print('Negative')

# third if/else
x = 50
print(x) # check variable made
if x > 0:
  if x <= 50:
    if (x % 2) == 0:
      print('it is an even number that is smaller than 50')
    else:
      print('it is an odd number that is smaller than 50')
  else:
    print ('Larger than 50')
    if (x % 3) == 0:
      print('it is larger than 50 and divisible by 3')
    else:
      print('it is larger than 50 and not divisible by 3')
elif x == 0:
  print ('0')
else:
  print('Negative')

# test numbers using command line example using sys 
test = int(sys.argv[1]) # check variable made
x = test
print("Tested number is", x)
if x > 0:
  if x <= 50:
    if (x % 2) == 0:
      print('it is an even number that is smaller than 50')
    else:
      print('it is an odd number that is smaller than 50')
  else:
    print ('Larger than 50')
    if (x % 3) == 0:
      print('it is larger than 50 and divisible by 3')
    else:
      print('it is larger than 50 and not divisible by 3')
elif x == 0:
  print ('0')
else:
  print('Negative') 
