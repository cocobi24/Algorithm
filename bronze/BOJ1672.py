# https://www.acmicpc.net/problem/1672

N = int(input())
arr = list(input().rstrip())
base = {
    'A':{'A':'A', 'G':'C', 'C':'A', 'T':'G'},
    'G':{'A':'C', 'G':'G', 'C':'T', 'T':'A'},
    'C':{'A':'A', 'G':'T', 'C':'C', 'T':'G'},
    'T':{'A':'G', 'G':'A', 'C':'G', 'T':'T'}
}

answer = arr
while len(answer) > 1 :
    answer.append(base[answer.pop()][answer.pop()])

print(*answer)