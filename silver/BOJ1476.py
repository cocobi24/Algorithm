# https://www.acmicpc.net/problem/1476

E, S, M = map(int, input().split())
e, s, m, year = 1, 1, 1, 1

while True :
    if e == E and s == S and m == M :
        print(year)
        break

    e = e+1 if e < 15 else 1
    s = s + 1 if s < 28 else 1
    m = m + 1 if m < 19 else 1
    year += 1