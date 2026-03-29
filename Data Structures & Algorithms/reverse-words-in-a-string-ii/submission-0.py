class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        N = len(s)
        j = 0
        for k, i in zip(range(N), reversed(range(N))):
            if s[i] == " ":
                j += 1
                s[i] = [s[i], j, k]
                j += 1
            else:
                s[i] = [s[i], j, k]
        print(s)
        s.sort(key=lambda x: (x[1], -x[2]))
        print(s)
        for i in range(N):
            s[i] = s[i][0]