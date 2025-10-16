# https://www.acmicpc.net/problem/21567

ABC= str(int(input()) * int(input()) * int(input()))
for i in range(10):
    print(ABC.count(f'{i}'))