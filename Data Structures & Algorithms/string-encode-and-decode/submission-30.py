class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += f"{len(s)}#{s}"

        print(ans)
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        candiLen = ""
        i = 0
        while i < len(s):
            currLet = s[i]
            if currLet != "#":
                candiLen += currLet
                i += 1
            else:
                stringEnd = i+1+int(candiLen)
                ans.append(s[i+1:stringEnd])
                print(ans)
                candiLen = ""
                i = stringEnd

        return ans
