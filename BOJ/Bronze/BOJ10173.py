# https://www.acmicpc.net/submit/10173

import sys
input = sys.stdin.readline

while True:
  line = input().rstrip()
  if line == "EOI":
    break
  line = [l.upper() for l in line.split()]
  print('Found' if 'NEMO' in ''.join(line) else 'Missing')