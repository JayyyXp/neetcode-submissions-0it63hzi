class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        ans = 0
        #for i in range(len(s)):
        #    for j in range(i, len(s)):
        #        print(s[i:j+1])
        #        if len(s[i:j+1]) == len(set(s[i:j+1])):
        #            ans = max(ans, len(s[i:j+1]))
        #return ans 

        l, r = 0,0
        ans = 0
        while r < len(s):
            if len(s[l:r+1])== len(set(s[l:r+1])):
                ans = max(ans, len(s[l:r+1]))
                r += 1
            else:
                l += 1
        
        return ans
