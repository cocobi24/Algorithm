# https://www.acmicpc.net/problem/28445

color = set()
father = list(map(str, input().rstrip().split()))
mather = list(map(str, input().rstrip().split()))

def getColor():
  color.add(f"{father[0]} {father[0]}")
  color.add(f"{father[0]} {father[1]}")
  color.add(f"{father[0]} {mather[0]}")
  color.add(f"{father[0]} {mather[1]}")
  color.add(f"{mather[0]} {mather[0]}")
  color.add(f"{mather[0]} {mather[1]}")
  color.add(f"{mather[0]} {father[0]}")
  color.add(f"{mather[0]} {father[1]}")

getColor()
father.reverse()
mather.reverse()
getColor()

print(*sorted(color), sep='\n')