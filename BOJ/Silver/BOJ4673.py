# https://www.acmicpc.net/problem/4673

constructors = []
nums = [i for i in range(1, 10000)]

def d(n) :
    num = n
    temp = list(str(n))
    for cnt in temp :
        num += int(cnt)
    return num

for i in range(1, 10000) :
    constructor = d(i)
    constructors.append(constructor)

answer = list(map(str, sorted(set(nums) - set(constructors))))
print('\n'.join(answer), end='')
