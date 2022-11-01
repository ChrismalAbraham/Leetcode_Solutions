from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
# Using a min_heap and a hashmap
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        min_heap = []
        for val, freq in freq_map.items():
            heappush(min_heap, (freq, val))
            if len(min_heap) > k:
                heappop(min_heap)

        res = []
        for i in range(k):
            res.append(heappop(min_heap)[1])
        return res
        
# Using an array and a Hashmap        
#         count = {}
#         freq = [[] for i in range(len(nums) + 1)]
        
#         for num in nums:
#             count[num] = count.get(num, 0) + 1
#         for n, c in count.items():
#             freq[c].append(n)
        
#         response = []
#         for i in range(len(freq) - 1, 0, -1):
#             for num in freq[i]:
#                 response.append(num)
#                 if len(response) == k:
#                     return response
        
        
        