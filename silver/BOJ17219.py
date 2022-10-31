# https://www.acmicpc.net/problem/17219

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
sites = {}

for i in range(n) :
    site, pwd = input().rstrip().split()
    sites[site] = pwd

for i in range(m) :
    site = input().rstrip()
    print(sites[site])