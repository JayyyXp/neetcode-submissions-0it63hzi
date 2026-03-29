class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        if not s or not t:
            return ""

        tCount = Counter(t)
        currWindow = {}
        have, need = 0, len(tCount)
        res = ""
        resLen = float('inf')
        l = 0

        for r in range(len(s)):
            letter = s[r]
            if letter in tCount:
                currWindow[letter] = currWindow.get(letter, 0) + 1
                if currWindow[letter] == tCount[letter]:
                    have += 1

            while have == need:
                # Found a valid window
                if (r - l + 1) < resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1

                # Try to contract the window
                if s[l] in tCount:
                    currWindow[s[l]] -= 1
                    if currWindow[s[l]] < tCount[s[l]]:
                        have -= 1
                l += 1

        return res
