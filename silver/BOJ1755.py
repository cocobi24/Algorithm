# https://www.acmicpc.net/problem/1755

num = {
    1 : 'one'
    , 2 : 'two'
    , 3 : 'three'
    , 4 : 'four'
    , 5 : 'five'
    , 6 : 'six'
    , 7 : 'seven'
    , 8 : 'eight'
    , 9 : 'nine'
    , 0 : 'zero'
}

alpha = {v: k for k, v in num.items()}

m, n = map(int, input().split())
num_list = [str(i) for i in range(m,n+1)]
temp = []
answer = []

for n in num_list :
    s = ''
    for c in list(n) :
        s += num[int(c)] + ' '
    s = s.rstrip()
    temp.append((s))

temp = sorted(temp)

for s in temp :
    n = ''
    for c in s.split(' ') :
        n += str(alpha[c])
    answer.append((n))

l = len(answer)
for i in range(l) :
    if i > 0  and i % 10 == 0 :
        print()
    print(answer[i], end=' ')