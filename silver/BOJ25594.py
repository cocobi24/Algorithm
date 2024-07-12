# https://www.acmicpc.net/problem/25594

hg = {
  'a': 'aespa',     'b': 'baekjoon',  'c': 'cau',   'd': 'debug',   'e': 'edge',    'f': 'firefox',
  'g': 'golang',    'h': 'haegang',   'i': 'iu',    'j': 'java',    'k': 'kotlin',  'l': 'lol',
  'm': 'mips',      'n': 'null',      'o': 'os',    'p': 'python',  'q': 'query',   'r': 'roka',
  's': 'solvedac',  't': 'tod',       'u': 'unix',  'v': 'virus',   'w': 'whale',   'x': 'xcode',
  'y': 'yahoo',     'z': 'zebra',
}

msg = input().rstrip()
idx = 0
ans = []
while idx < len(msg):
  l = len(hg[msg[idx]])

  if msg[idx:idx+l] == hg[msg[idx]]:
    ans.append(msg[idx])
    idx += l
  else:
    ans = 'ERROR!'
    break

if ans != 'ERROR!':
  ans = f"It's HG!\n{''.join(ans)}"
print(ans)