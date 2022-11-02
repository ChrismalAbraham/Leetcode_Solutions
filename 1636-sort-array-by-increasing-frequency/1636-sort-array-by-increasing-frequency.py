class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        num_freq = Counter(nums)
        nums.sort(key = lambda x: (num_freq[x], -x))
        return nums