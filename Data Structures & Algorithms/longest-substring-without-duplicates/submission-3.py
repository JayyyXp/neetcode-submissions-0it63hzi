class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        ans = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                print(s[i:j+1])
                if len(s[i:j+1]) == len(set(s[i:j+1])):
                    ans = max(ans, len(s[i:j+1]))
        return ans 

            