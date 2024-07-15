# https://www.acmicpc.net/problem/2789

import re
str = input()
reg = re.compile('[CAMBRIDGE]')
answer = reg.sub('', str)
print(answer)