class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        cache = {}

        def is_palindrome(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(l: int, r: int) -> int:
            if l > r:
                return 0
            if (l, r) in cache:
                return cache[(l, r)]
            
            count = 0
            if is_palindrome(l, r):
                count += 1
            count += dfs(l + 1, r)     # move left boundary forward
            count += dfs(l, r - 1)     # move right boundary backward
            count -= dfs(l + 1, r - 1) # remove double count of middle part
            cache[(l, r)] = count
            return count

        return dfs(0, n - 1)