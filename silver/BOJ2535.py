# https://www.acmicpc.net/problem/2535

n = int(input())
student = list(list(map(int,input().split())) for _ in range(n))
student = sorted(student, key = lambda x : x[2], reverse=True)

print(student[0][0], student[0][1])
print(student[1][0], student[1][1])

if student[0][0] == student[1][0] :
    for i in range(2, n) :
        if student[i][0] != student[0][0] :
            print(student[i][0], student[i][1])
            break
else :
    print(student[2][0], student[2][1])