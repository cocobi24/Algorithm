# https://www.acmicpc.net/problem/9733

import sys
input = sys.stdin
temp = ""
works_dic = {}
prior_list = ["Re", "Pt", "Cc", "Ea", "Tb", "Cm", "Ex"]

for s in input :
    temp += s.rstrip()
    temp += " "

works = temp.split()
cnt = len(works)

for work in works :
    if work not in works_dic :
        works_dic[work] = 1
    else :
        works_dic[work] += 1

for i in prior_list :
    if i in works_dic :
        target = works_dic[i]
        print(i, target, format(target/cnt, '.2f'))
    else :
        print(i, 0, format(0.00, '.2f'))
print("Total", cnt, format(1.00, '.2f'))