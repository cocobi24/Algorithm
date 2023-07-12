# https://www.acmicpc.net/problem/4159

import sys
input = sys.stdin.readline

while True:
    T = int(input())

    if T == 0:
        break

    route_list = []
    for _ in range(T):
        route_list.append((int(input())))
    route_list.sort()

    if (route_list[0] > 200) or (1422 - route_list[T-1 ] > 100):
        print("IMPOSSIBLE")
        continue
        
    interval_list = []
    for i in range(1, T):
        interval_list.append(route_list[i] - route_list[i-1])

    over_list = list(filter(lambda x : x > 200, interval_list))
    print("POSSIBLE" if len(over_list) == 0 else "IMPOSSIBLE")