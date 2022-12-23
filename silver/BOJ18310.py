# https://www.acmicpc.net/problem/18310

n = int(input())
homes = sorted(list(map(int, input().split())))
if (n % 2) == 0 :
    print(homes[(n//2)-1])
else :
    print(homes[(n // 2)])