class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        num_freq = defaultdict(int)
        for num in nums:
            num_freq[num] += 1
        nums.sort(key = lambda x: (num_freq[x], -x))
        return nums