# https://neetcode.io/problems/binary-search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)
        mid = end // 2
        while start < end:
            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                end = mid
            else:
                start = mid + 1
            mid = (start + end) // 2
        return -1