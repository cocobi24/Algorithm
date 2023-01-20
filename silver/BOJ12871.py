# https://www.acmicpc.net/problem/12871

import math

s = input()
t = input()
lcm = math.lcm(len(s), len(t))
s = lcm//len(s) * s
t = lcm//len(t) * t

if s == t :
    print(1)
else :
    print(0)