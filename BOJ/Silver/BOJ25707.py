# https://www.acmicpc.net/problem/25707

n = int(input())
bead = sorted(map(int, input().split()))
print(2 * (bead[-1] - bead[0]))