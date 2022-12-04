# https://www.acmicpc.net/problem/1453

n = int(input())
refuse = 0
num_list = list(map(int, input().split()))
seat_list = list()

for x in num_list :
    if x not in seat_list :
        seat_list.append(x)
    else :
        refuse += 1

print(refuse, end="")