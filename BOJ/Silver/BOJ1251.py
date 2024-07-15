# https://www.acmicpc.net/problem/1251

s = input()
word_list = []

for i in range(len(s)-2):
    for j in range(i+1, len(s)-1):
        for k in range(j+1, len(s)):
            word = s[:j][::-1] + s[j:k][::-1] + s[k:][::-1]
            word_list.append(word)

answer = min(word_list)
print(answer)