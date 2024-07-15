# https://www.acmicpc.net/problem/2671

import re
stirng = input()
pattern = re.compile('(100+1+|01)+')
isSubmarine = pattern.fullmatch(stirng)
print('SUBMARINE' if isSubmarine else 'NOISE')