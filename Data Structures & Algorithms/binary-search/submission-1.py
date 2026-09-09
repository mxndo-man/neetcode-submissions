class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1  

        while left <= right:
            midPoint =  (left+right)//2
            if nums[midPoint] == target:
                return midPoint
            elif target > nums[midPoint]:
                left = midPoint + 1
            else:
                right = midPoint - 1

        return -1
            
        