T = int(input())

for i in range(T) :
    pattern_str = input()
    pattern = ""
    for j in range(len(pattern_str) // 2) :
        if len(pattern_str[:j]) != 0 and pattern_str[:j] == pattern_str[j:j+len(pattern_str[:j])] :
            pattern = pattern_str[:j]
            break
    answer = len(pattern)
    print(f"#{i+1}", answer)