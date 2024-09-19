# https://www.acmicpc.net/problem/24936

n = int(input())
record = list(map(int, input().split()))

unique = set()
total = sum(record)
for i in range(n):
  unique.add(total - record[i])
unique = sorted(unique)
print(len(unique))
print(*unique)