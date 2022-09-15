class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ref_set = set()
        for num in nums:
            if num in ref_set:
                return True
            else:
                ref_set.add(num)
        return False