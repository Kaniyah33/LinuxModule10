#!/bin/bash
import sys

n = int(sys.argv[1])
result = ''
string = sys.stdin.readline()
for i in string:    
    i = i.upper()
    if i.isalpha() == True:
      result += (chr((ord(i) + n - 65) % 26 + 65))
result = [result[i:i+5] for i in range(0, len(result), 5)]
result = ' '.join(result)
result = [result[i:i+60] for i in range(0, len(result), 60)]
result = '\n'.join(result)
print(result)
