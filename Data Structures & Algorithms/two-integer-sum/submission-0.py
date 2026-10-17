class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapN = {}
        for pos, num in enumerate(nums):
            if target - num in mapN:
                return [mapN[target-num], pos]
            mapN[num] = pos