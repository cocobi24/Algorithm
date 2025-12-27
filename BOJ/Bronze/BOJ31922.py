# https://www.acmicpc.net/problem/31922

prize = list(map(int, input().split()))
print(max(prize[0] + prize[2], prize[1]))