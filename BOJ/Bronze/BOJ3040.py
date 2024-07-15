# https://www.acmicpc.net/problem/3040

dwarf_list = [int(input()) for _ in range(9)]
total = sum(dwarf_list)

flag = 0
for i in range(9) :
    for j in range(i+1, 9):
        a = dwarf_list[i]
        b = dwarf_list[j]
        if total - (a + b) == 100 :
            flag = 1
            break
    if flag == 1 :
        break

dwarf_list.remove(a)
dwarf_list.remove(b)
print(*dwarf_list, sep="\n")