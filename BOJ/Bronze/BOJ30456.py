# https://www.acmicpc.net/problem/30456

from itertools import product

def get_digit_root(n):
    while n >= 10:
        product = 1
        while n > 0:
            product *= n % 10
            n //= 10
        n = product
    return n

N, L = map(int, input().split())
if N == 0:
    print( '10' + '0' * (L - 2))
else:
    for comb in product(range(1, 10), repeat=L):
        num = int(''.join(map(str, comb)))
        if get_digit_root(num) == N:
            print( ''.join(map(str, comb)))
            exit()