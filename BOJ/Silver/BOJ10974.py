# https://www.acmicpc.net/problem/10974

n = int(input())
arr = [i for i in range(1, n+1)]

temp = [0] * n
check = [0] * n

def perm(idx) :
    if idx == n :
        print(*temp)
    else :
        for i in range(n) :
            if check[i] == 0 :
                temp[idx] = arr[i]
                check[i] = 1
                perm(idx+1)
                check[i] = 0

perm(0)