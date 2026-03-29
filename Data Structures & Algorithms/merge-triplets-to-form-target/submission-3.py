class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        if len(triplets) == 1:
            return triplets[0] == target

        for i in range(3):
            minI = float('inf')
            found = False
            counter = {}
            #print("target", target[i])
            for triplet in triplets:
                #print("triplet[i]",triplet[i])
                minI = min(minI, triplet[i])
                if target[i] == triplet[i]:
                    found = True
                counter[triplet[i]] = counter.get(triplet[i], 0) + 1 
            #print("minI", minI)
            if not found or (minI == target[i] and counter[minI] == 1):
                print(found)
                return False
        return True