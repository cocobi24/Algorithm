# https://leetcode.com/problems/happy-number

class Solution(object):
  def isHappy(self, n):
    """
    :type n: int
    :rtype: bool
    """
    num_list = set()
    while True:
      if n == 1 or n in num_list:
        break
      num_list.add(n)
      ns = list(str(n))
      n = sum(map(lambda x: int(x)**2, ns))

    return True if n == 1 else False