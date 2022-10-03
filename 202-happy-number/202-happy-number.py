class Solution:
    def isHappy(self, num: int) -> bool:
        def next_happy_number(n: int) -> int:
            n = str(n)
            next_n = 0
            for char in n:
                next_n += int(char) ** 2
            return next_n

        slow = fast = num
        is_happy = True
        while fast != 1:
            slow = next_happy_number(slow)
            fast = next_happy_number(next_happy_number(fast))

            if fast == slow and fast != 1:
                is_happy = False
                break

        return is_happy