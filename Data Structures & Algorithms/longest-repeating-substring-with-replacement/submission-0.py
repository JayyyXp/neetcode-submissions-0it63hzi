class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 1
        ans = 0
        
        while r < len(s)+1:
            window = s[l:r]
            subSC = {}
            for letter in window:
                if letter in subSC:
                    subSC[letter] += 1
                else:
                    subSC[letter] = 1
            cand = sum(sorted(subSC.values())[:-1])
            print(window, cand)
            if cand <= k:
                ans = max(ans, len(window))
                r += 1
            else:
                l += 1
        return ans
