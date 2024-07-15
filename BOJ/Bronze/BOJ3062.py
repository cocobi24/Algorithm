# https://www.acmicpc.net/problem/3062

T = int(input())

for _ in range(T) :
    n = int(input())
    revers_n = int(str(n)[::-1])
    sum_n = n + revers_n
    revser_sum = int(str(sum_n)[::-1])
    print("YES" if sum_n == revser_sum else "NO")