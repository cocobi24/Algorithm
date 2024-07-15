# https://www.acmicpc.net/problem/2851

import sys
input = sys.stdin
nums = [int(n.rstrip()) for n in input]
temp_a = 0
temp_b = 0
for n in nums :
    if temp_a >= 100 :
        break
    temp_a += n
    temp_b = temp_a - n

a = abs(temp_a - 100)
b = abs(temp_b - 100)
answer = temp_b if a > b else temp_a
print(answer, end='')