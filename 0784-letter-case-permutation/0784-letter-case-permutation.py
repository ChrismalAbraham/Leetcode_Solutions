class Solution:
    def letterCasePermutation(self, arr: str) -> List[str]:
        permutations = [arr]
        for i in range(len(arr)):
            if arr[i].isalpha():
                len_permutations = len(permutations)
                for j in range(len_permutations):
                    new_permutation = list(permutations[j])
                    new_permutation[i] = new_permutation[i].swapcase()
                    permutations.append("".join(new_permutation))

        return permutations