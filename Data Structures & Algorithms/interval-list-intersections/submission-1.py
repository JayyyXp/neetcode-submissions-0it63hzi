class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        
        i = 0
        j = 0
        ans = []
        while i < len(firstList) and j < len(secondList):
            print(firstList[i], secondList[j])
            if secondList[j][0] <= firstList[i][0] <= secondList[j][1]:
                s = firstList[i][0]
                if firstList[i][1] < secondList[j][1]:
                    e = firstList[i][1]
                    i += 1
                else:
                    e = secondList[j][1]
                    j += 1
                ans.append([s, e])
                print([s, e])
                continue
            
            if firstList[i][0] <= secondList[j][0] <= firstList[i][1]:
                s = secondList[j][0]
                if firstList[i][1] < secondList[j][1]:
                    e = firstList[i][1]
                    i += 1
                else:
                    e = secondList[j][1]
                    j += 1
                ans.append([s, e])
                print([s, e])
                continue
            
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        
        # handle the rest


        return ans  