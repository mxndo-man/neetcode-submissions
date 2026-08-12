class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        chunky_map = {}

        for i, num in enumerate(nums):
            chunky = target - num
            if chunky in chunky_map:
                return [chunky_map[chunky],i]
            chunky_map[num] = i

        return []
