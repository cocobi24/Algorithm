# https://www.acmicpc.net/problem/1343

s = input().replace('XXXX','AAAA').replace('XX','BB')
if 'X' in s :
    print(-1, end='')
else :
    print(s, end='')