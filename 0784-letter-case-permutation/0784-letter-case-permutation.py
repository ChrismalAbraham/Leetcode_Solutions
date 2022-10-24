class Solution:
    def letterCasePermutation(self, arr: str) -> List[str]:
        def is_letter(char: str) -> bool:
            if char.isalpha():
                return True
            return False

        def switch_case(char: str) -> str:
            if char.islower():
                return char.upper()
            return char.lower()

        res = [arr]
        pos_of_char = []
        for i, char in enumerate(arr):
            if is_letter(char):
                pos_of_char.append(i)

        for index_of_char in pos_of_char:
            len_permutations = len(res)
            for j in range(len_permutations):
                new_permutation = list(res[j])
                new_permutation[index_of_char] = switch_case(
                    new_permutation[index_of_char])
                res.append("".join(new_permutation))

        return res