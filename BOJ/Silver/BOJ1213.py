# https://www.acmicpc.net/problem/1213

import sys
from collections import Counter
word = sorted(list(input()))
count = Counter(word)

odd, mid, answer = 0, '', ''
for i in count:
    if count[i] % 2 != 0:
        odd += 1
        mid += i

        if odd > 1:
            print("I'm Sorry Hansoo")
            sys.exit(0)

    for _ in range(count[i]//2):
        answer += i

print(answer + answer[::-1] if odd == 0 else answer + mid + answer[::-1])