# https://www.acmicpc.net/problem/26264

N = int(input())
memo = input().rstrip()
b = memo.count('b')
s = memo.count('s')

if b > s:
    print("bigdata?")
elif s > b:
    print("security!")
else:
    print("bigdata? security!")