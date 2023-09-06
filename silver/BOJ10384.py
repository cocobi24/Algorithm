# https://www.acmicpc.net/problem/10384

import sys
input = sys.stdin.readline
T = int(input())
print_list = ["Not a pangram", "Pangram!", "Double pangram!!", "Triple pangram!!!"]

for i in range(T):
    alphabet = [0] * 26
    words = list(input().rstrip())
    for word in words:
        if word.isalpha() :
            idx = ord(word.upper()) - 64
            alphabet[idx-1] += 1
    print(f"Case {i+1}: {print_list[min(alphabet)]}")