# https://www.acmicpc.net/problem/13235

s = input().rstrip()
l = len(s)
l2 = l//2
true = 'true'
false = 'false'

if l == 1:
    print(true)
elif l % 2 == 0:
    print(true if s[0:l2] == s[l2:l][::-1] else false)
else:
    print(true if s[0:l2] ==  s[l2+1:l] else false)
