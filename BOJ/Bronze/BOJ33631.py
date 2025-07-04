# https://www.acmicpc.net/problem/33631

Fs, Cs, Es, Bs = map(int, input().split())
Fn, Cn, En, Bn = map(int, input().split())
Q = int(input())

ingredient = [Fs, Cs, Es, Bs]
cookie = 0

def setIngredient(t, a):
    ingredient[t-2] += a
    print(ingredient[t-2])

for _ in range(Q):
    query = input().split()
    type_, amount = int(query[0]), int(query[1])

    if type_ == 1:
        need_f = Fn * amount
        need_c = Cn * amount
        need_e = En * amount
        need_b = Bn * amount

        if ingredient[0] >= need_f and ingredient[1] >= need_c and ingredient[2] >= need_e and ingredient[3] >= need_b:
            ingredient[0] -= need_f
            ingredient[1] -= need_c
            ingredient[2] -= need_e
            ingredient[3] -= need_b
            cookie += amount
            print(cookie)
        else:
            print("Hello, siumii")
    else:
        setIngredient(type_, amount)