# https://www.acmicpc.net/problem/31394

n = int(input())
scores = [int(input()) for _ in range(n)]

Scholarship = "Common"
if 3 in scores:
    Scholarship = "None"
elif all(mark == 5 for mark in scores):
    Scholarship = "Named"
elif sum(scores) / n >= 4.5:
    Scholarship = "High"
print(Scholarship)