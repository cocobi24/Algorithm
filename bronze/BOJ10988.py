# https://www.acmicpc.net/problem/10988

str = input()
reverStr = list(str)
reverStr.reverse()
reverStr = ''.join(reverStr)

if str == reverStr :
    print(1)
else :
    print(0)