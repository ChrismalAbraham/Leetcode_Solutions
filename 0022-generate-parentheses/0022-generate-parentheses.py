class Solution:
    def generateParenthesis(self, num: int) -> List[str]:
        class ParanthesisString():
            def __init__(self, string="", num_open=0, num_closed=0):
                self.string = string
                self.open_paran = num_open
                self.closed_paran = num_closed
                
        res = []
        queue = deque()
        queue.append(ParanthesisString())
        while queue:
            curr = queue.popleft()
            if curr.open_paran == num and curr.closed_paran == num:
                res.append(curr.string)

            else:
                if curr.open_paran < num:
                    queue.append(ParanthesisString(
                        curr.string + '(', curr.open_paran + 1, curr.closed_paran))

                if curr.closed_paran < curr.open_paran:
                    queue.append(ParanthesisString(
                        curr.string + ')', curr.open_paran, curr.closed_paran + 1))

        return res