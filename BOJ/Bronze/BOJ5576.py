# https://www.acmicpc.net/problem/5576

team_a = sorted([int(input()) for _ in range(10)])
team_b = sorted([int(input()) for _ in range(10)])
print(sum(team_a[-3::]), sum(team_b[-3::]))