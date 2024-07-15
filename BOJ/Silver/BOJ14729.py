# https://www.acmicpc.net/problem/14729

import sys
input=sys.stdin.readline
n=int(input().rstrip())
result=sorted(float(input().rstrip()) for _ in range(7))

i=0
while i<n-7:
    result.append(float(input().rstrip()))
    result.sort()
    result.pop()
    i=i+1


for i in result:
    print('{:.3f}'.format(i))