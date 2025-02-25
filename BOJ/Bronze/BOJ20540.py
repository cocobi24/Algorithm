# https://www.acmicpc.net/problem/20540

mbti = list(input().rstrip())
def getMbti(mbti):
    m = 'E' if mbti[0] == 'I' else 'I'
    b = 'N' if mbti[1] == 'S' else 'S'
    t = 'F' if mbti[2] == 'T' else 'T'
    i = 'P' if mbti[3] == 'J' else 'J'
    return m + b + t + i
print(getMbti(mbti))