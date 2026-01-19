# https://www.acmicpc.net/problem/15184

s = input().rstrip()
s = s.upper()

for i in range(97, 123):
    target = chr(i).upper()
    cnt = s.count(target)
    print(target,'|', '*' * cnt)