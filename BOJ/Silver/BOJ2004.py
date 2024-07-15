# https://www.acmicpc.net/problem/2004

n, m = map(int, input().split())

def count_num(x, n):
    count = 0
    while x >= n:
        x = x // n
        count += x
    return count

count_two = count_num(n, 2) - count_num(n-m, 2) - count_num(m, 2)
count_five = count_num(n, 5) - count_num(n-m, 5) - count_num(m, 5)
print(min(count_two, count_five))