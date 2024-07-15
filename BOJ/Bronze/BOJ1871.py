# https://www.acmicpc.net/problem/1871

n = int(input())

for _ in range(n) :
    front, rear = input().split("-")
    a, b = 0, int(rear)

    for i in range(3) :
        a += (ord(front[i])-65) * 26**(2-i)

    number = abs(a - b)
    print("nice" if number <= 100 else "not nice")