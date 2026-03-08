# https://www.acmicpc.net/problem/34813

s = input().rstrip()
ctg = {
    'F' : 'Foundation',
    'C' : 'Claves',
    'V' : 'Veritas',
    'E' : 'Exploration'
}
key = s[0]
print(ctg[key])