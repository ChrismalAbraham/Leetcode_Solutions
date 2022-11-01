class Solution:
    def frequencySort(self, string: str) -> str:
        char_freq = defaultdict(int)
        for char in string:
            char_freq[char] += 1

        max_heap = []
        for char, count in char_freq.items():
            heappush(max_heap, (-count, char))

        res = []
        while max_heap:
            count, char = heappop(max_heap)
            count = -count
            for _ in range(count):
                res.append(char)
        return "".join(res)