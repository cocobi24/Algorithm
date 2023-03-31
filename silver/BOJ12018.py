# https://www.acmicpc.net/problem/12018

n, m = map(int, input().split())
req_mileage = []
answer = 0
for _ in range(n) :
    p, l = map(int, input().split())
    mileage_list = sorted(list(map(int, input().split())))
    if l-p > 0 :
        req_mileage.append(1)
    elif l-p == 0 :
        req_mileage.append(mileage_list[0])
    else :
        req_mileage.append(mileage_list[p-l])
req_mileage.sort()

if sum(req_mileage) <= m :
    print(n)
else :
    total = 0
    for i in range(n) :
        total += req_mileage[i]
        answer += 1
        if total > m :
            answer -= 1
            break
    print(answer)