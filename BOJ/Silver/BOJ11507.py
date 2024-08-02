# https://www.acmicpc.net/problem/11507

s = input().strip()
lost = set()
cards = [13] * 4
def lost_count(t):
  if t == "P":
    cards[0] -= 1
  elif t == "K":
    cards[1] -= 1
  elif t == "H":
    cards[2] -= 1
  else:
    cards[3] -= 1

for i in range(0, len(s), 3):
  card = s[i:i+3]
  if card not in lost:
    lost.add(card)
    lost_count(card[0])
  else:
    print("GRESKA")
    exit()
print(*cards)