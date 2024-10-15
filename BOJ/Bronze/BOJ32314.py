# https://www.acmicpc.net/problem/32314

tree = int(input())
w, v = map(int, input().split())
print(1 if w // v >= tree else 0)