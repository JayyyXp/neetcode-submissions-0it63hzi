class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # ------  --------
        #    --------
        #
        # HALF
        # ------   --------
        #    -----
        # HALF
        # ------   --------
        #         -----
        # OK
        # -------   --------
        #  ----
        if len(intervals) == 0:
            return [newInterval]
        if intervals[-1][1] < newInterval[0]:
            return intervals + [newInterval]
        if newInterval[1] < intervals[0][0] :
            return [newInterval] + intervals

        niS, niE = newInterval
        niSTaken, niETaken = False, False
        niSTakenIdx, niETakenIdx = 0,0
        res = []
        for i, (iS, iE) in enumerate(intervals):
            if iS <= niS and niE <= iE:
                return intervals
            elif iS <= niS <= iE:
                niSTaken = True
                niSTakenIdx = i
                res.append([iS, max(iE, niE)])
            elif iS <= niE <= iE:
                niETaken = True
                niETakenIdx = i
                res.append([min(iS,niS), iE])
            else:
                res.append([iS,iE])
        takenCount = sum([niSTaken, niETaken])
        print(res, niSTakenIdx, niETakenIdx)
        if takenCount == 1:
            return res
        if takenCount == 2:
            newInt = [res[niSTakenIdx][0], res[niETakenIdx][1]]
            print(newInt)
            newInt = res[:niSTakenIdx] + [newInt] + res[niETakenIdx+1:]  
            print('final',newInt)
            return newInt
        res1 = []
        for i in range(1, len(res)):
            f = res[i-1]
            s = res[i]
            if takenCount == 0 and f[1] < niS and niE < s[0]:
                res1.append(f)
                res1.append(newInterval)
                res1.append(s)
                return res1 + res[i+1:] 
            else:
                res1.append(f)
        print(res1)
        return [newInterval]



        
