# https://www.acmicpc.net/problem/4884

import sys
input = sys.stdin. readline

while True:
    G, T, A, D = map(int, input().split())
    if G == -1:
        break

    preliminary = T * (T - 1) // 2 * G
    tournament = G * A + D
    X, Y, Z = 0, 0, 1
    while tournament > Z:
        X += Z
        Z *= 2

    X += preliminary
    Y += Z - tournament
    answer = f"{G}*{A}/{T}+{D}={X}+{Y}"

    print(answer)