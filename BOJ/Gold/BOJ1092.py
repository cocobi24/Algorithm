# https://www.acmicpc.net/problem/1092

n = int(input())
crane = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
cargos = sorted(list(map(int, input().split())), reverse=True)
crane = list(filter(lambda x: x >= cargos[-1], crane))
answer = 0

if len(crane) == 0 :
    print(-1, end='')
else :
    if max(cargos) > max(crane):
        print(-1, end='')
    else :
        while True :
            if len(cargos) == 0 :
                break
            answer += 1
            for i in range(len(crane)) :
                for j in range(len(cargos)) :
                    if crane[i] >= cargos[j] :
                        cargos.pop(j)
                        break
        print(answer, end='')