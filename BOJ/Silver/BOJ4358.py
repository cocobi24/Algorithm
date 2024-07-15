# https://www.acmicpc.net/problem/4358

import sys
input = sys.stdin
trees = {}
count = 0

for tree in input :
    count += 1
    if tree.rstrip() in trees :
        trees[tree.rstrip()] += 1
    else :
        trees[tree.rstrip()] = 1

trees = sorted(trees.items(), key = lambda x : x[0])

for k, v in trees :
    per = v/count *100
    print(k, format(per, '.4f'))