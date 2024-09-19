# https://www.acmicpc.net/problem/11387

input = [list(map(int, input().split())) for _ in range(4)]
cri, pabu = input[0], input[1]
cri_weapon, pabu_weapon = input[2], input[3]
cri_swap = [cri[i] - cri_weapon[i] + pabu_weapon[i] for i in range(5)]
pabu_swap = [pabu[i] - pabu_weapon[i] + cri_weapon[i] for i in range(5)]

def getPower(lst):
  return (lst[0]) * \
          (100 + lst[1]) * \
          (100 * (100 - min(lst[2], 100)) + min(lst[2], 100) * (lst[3])) * (100 + lst[4])

def comparePower(l1, l2):
    print(0 if l1 == l2 else '-' if l1 > l2 else '+')

comparePower(getPower(cri), getPower(cri_swap))
comparePower(getPower(pabu), getPower(pabu_swap))