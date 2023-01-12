# https://www.acmicpc.net/problem/5026

n = int(input())

for _ in range(n) :
    exam = input()
    if '+' in exam :
        a, b = map(int, exam.split('+'))
        print(a+b)
    else :
        print("skipped")