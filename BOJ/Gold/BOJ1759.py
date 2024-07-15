# https://www.acmicpc.net/problem/1759

L, C = map(int, input().split())
c_list = sorted(map(str, input().split()))
vowel = ['a', 'e', 'i', 'o', 'u']

def check(arr):
    v_count, c_count = 0, 0
    for i in arr:
        if i in vowel:
            v_count += 1
        else:
            c_count += 1

    if v_count >= 1 and c_count >= 2:
        return True
    return False

def combination(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i in range(len(arr)):
        for rest in combination(arr[i+1:], n-1):
            result.append([arr[i]] + rest)
    return result

for answer in combination(c_list, L) :
    if check(answer):
        print("".join(answer))
