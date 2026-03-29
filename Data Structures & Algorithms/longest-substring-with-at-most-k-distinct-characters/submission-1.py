class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        ans = 0 
        l = 0
        counter = collections.defaultdict(int)
    
        for r in range(len(s)):
            counter[s[r]] += 1
            #while l < len(s) and len(counter) > k:
            if len(counter) > k:
                print(counter)
                counter[s[l]] -= 1
                if counter[s[l]] == 0:
                    counter.pop(s[l])
                l += 1
            print(s[l:r+1])
            ans = max(ans, r - l + 1)
        return ans
            