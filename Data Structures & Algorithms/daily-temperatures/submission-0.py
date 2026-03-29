class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        for i in range(len(temperatures)):
            currTemp = temperatures[i]
            addDefault = True
            for j in range(i+1, len(temperatures)):
                nxtTemp = temperatures[j]
                if nxtTemp > currTemp:
                    ans.append(j-i)
                    addDefault = False
                    break
            if addDefault:
                ans.append(0)        
            
        return ans