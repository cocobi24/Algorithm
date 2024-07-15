# https://www.acmicpc.net/problem/27127

from itertools import permutations

def solve(n):
    digits = '0123456789'
    solutions = []
    for p in permutations(digits, 10):
        A, B, C, D, E, F, G, H, I, J = p
        ABCDE = int(''.join([A, B, C, D, E]))
        FGHIJ = int(''.join([F, G, H, I, J]))
        if ABCDE / FGHIJ == 9:
            solutions.append((ABCDE, FGHIJ))
    solutions.sort()
    return solutions[n-1]

n = int(input())
A, B = solve(n)
A = '0' + str(A) if len(str(A)) == 4 else A
B = '0' + str(B) if len(str(B)) == 4 else B
print(A, B)