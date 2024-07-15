# https://www.acmicpc.net/problem/2941

s = input()
word = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in word :
    s = s.replace(i, "W")

print(len(s))