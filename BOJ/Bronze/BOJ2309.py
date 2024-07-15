# https://www.acmicpc.net/problem/2309

dwarfs = []
answer = 0

for i in range(9) :
    dwarfs.append(int(input()))

allDwarf = sum(dwarfs)

for i in range(8) :
    for j in range(1, 9) :
        if sum(dwarfs) - (dwarfs[i] + dwarfs[j]) == 100 :
            checkOne = dwarfs[i]
            checkTwo = dwarfs[j]
            break

dwarfs.remove(checkOne)
dwarfs.remove(checkTwo)
print( '\n'.join(map(str, sorted(dwarfs))) )