# https://www.acmicpc.net/problem/2720

import sys
input = sys.stdin.readline
n = int(input())
coin = [25, 10, 5, 1]

for i in range(n) :
    coins = {25: 0, 10: 0, 5: 0, 1: 0}
    money = int(input())
    for j in range(4) :
        answer = money // coin[j]
        coins[coin[j]] = answer
        money = money % coin[j]
        print(coins[coin[j]], end=" ")
    print()