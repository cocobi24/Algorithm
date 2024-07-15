# https://www.acmicpc.net/problem/16466

N = int(input())
A = set(map(int,input().split()))
seat_list = set(i for i in range(1,1000001))
print(min(seat_list - A))