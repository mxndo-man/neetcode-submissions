class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set()
        uni = set(nums)
        if len(uni) == len(nums):
            return False 
        return True 