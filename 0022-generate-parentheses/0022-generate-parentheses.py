class Solution:
    def generateParenthesis(self, num: int) -> List[str]:
        
        def all_valid_paranthesis(num, res, p_string, open_paran, closed_paran, index):
            if open_paran == num and closed_paran == num:
                res.append(''.join(p_string))
            else:
                if open_paran < num:
                    p_string[index] = '('
                    all_valid_paranthesis(num, res, p_string,
                                          open_paran + 1, closed_paran, index + 1)
                if closed_paran < open_paran:
                    p_string[index] = ')'
                    all_valid_paranthesis(num, res, p_string,
                                          open_paran, closed_paran + 1, index + 1)
        res = []
        p_string = [0 for x in range(num * 2)]
        all_valid_paranthesis(num, res, p_string, 0, 0, 0)
        return res
    
    
#         class ParanthesisString():
#             def __init__(self, string="", num_open=0, num_closed=0):
#             self.string = string
#             self.open_paran = num_open
#             self.closed_paran = num_closed   
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