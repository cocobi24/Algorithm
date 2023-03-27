# https://www.acmicpc.net/problem/4796

i = 1
while True :
    L, P, V = map(int, input().split())
    if L == 0 :
        break

    day = (V//P)*L + (V%P)
    if V % P > L:
        day = (V//P*L) + L

    print(f"Case {i}: {day}")
    i += 1