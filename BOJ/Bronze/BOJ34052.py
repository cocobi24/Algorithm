# https://www.acmicpc.net/problem/34052

run = [int(input()) for _ in range(4)]
print("Yes" if sum(run) + 300 <= 1800 else "No")