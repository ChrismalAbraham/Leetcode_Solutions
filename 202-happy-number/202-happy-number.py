class Solution:
    def isHappy(self, num: int) -> bool:
        def next_happy_number(n: int) -> int:
            next_n = 0
            while n > 0:
                digit = n % 10
                next_n += digit * digit
                n //= 10
            return next_n

        slow = fast = num
        while True:
            slow = next_happy_number(slow)
            fast = next_happy_number(next_happy_number(fast))
            if slow == fast:
                break
        return slow == 1