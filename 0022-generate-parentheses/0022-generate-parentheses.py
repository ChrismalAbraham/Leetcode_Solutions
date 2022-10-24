class Solution:
    def generateParenthesis(self, num: int) -> List[str]:
        class ParanthesisString():
            def __init__(self, string="", num_open=0, num_closed=0):
                self.string = string
                self.open_paran = num_open
                self.closed_paran = num_closed
       
        def all_valid_paranthesis(num, res, curr_ps):
            if curr_ps.open_paran == num and curr_ps.closed_paran == num:
                res.append(curr_ps.string)
            else:
                if curr_ps.open_paran < num:
                    all_valid_paranthesis(num, res, ParanthesisString(
                        curr_ps.string + '(', curr_ps.open_paran + 1, curr_ps.closed_paran))
                if curr_ps.closed_paran < curr_ps.open_paran:
                    all_valid_paranthesis(num, res, ParanthesisString(
                        curr_ps.string + ')', curr_ps.open_paran, curr_ps.closed_paran + 1))
        res = []
        all_valid_paranthesis(num, res, ParanthesisString())
        return res
    
    
    
#         res = []
#         queue = deque()
#         queue.append(ParanthesisString())
#         while queue:
#             curr = queue.popleft()
#             if curr.open_paran == num and curr.closed_paran == num:
#                 res.append(curr.string)

#             else:
#                 if curr.open_paran < num:
#                     queue.append(ParanthesisString(
#                         curr.string + '(', curr.open_paran + 1, curr.closed_paran))

#                 if curr.closed_paran < curr.open_paran:
#                     new_string = curr.string + ')'
#                     queue.append(ParanthesisString(
#                         curr.string + ')' , curr.open_paran, curr.closed_paran + 1))

#         return res