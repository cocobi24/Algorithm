# https://www.acmicpc.net/problem/32778

s = input().rstrip()

if '(' in s:
    idx = s.index('(')
    print(s[:idx-1])
    print(s[idx+1:len(s)-1])
else:
    print(s, '-', sep='\n')