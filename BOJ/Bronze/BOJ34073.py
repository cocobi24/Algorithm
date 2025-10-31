# https://www.acmicpc.net/problem/34073
  
N = int(input())
message = input().rstrip().split()
message = list(map(lambda x: x + "DORO", message))
print(*message, sep=' ')