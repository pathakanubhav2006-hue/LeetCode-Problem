class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        n = len(A)
        seen = [0] * (n + 1)
        common = 0
        result = []

        for i in range(n):
            a = A[i]
            b = B[i]

            seen[a] += 1
            if seen[a] == 2:
                common += 1

            seen[b] += 1
            if seen[b] == 2:
                common += 1

            result.append(common)

        return result
                

        