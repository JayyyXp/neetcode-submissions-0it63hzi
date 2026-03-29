class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        ans = [1] * len(ratings)
        while True:
            canBreak = True
            for i in range(len(ans)):
                left = ratings[i-1] if i-1 > -1 else float('inf')
                right = ratings[i+1] if i+1 < len(ans) else float('inf')
                print(left, ratings[i], right)
                if ratings[i] > left and ans[i] <= ans[i-1]:
                    ans[i] = ans[i-1] +1
                    print('here')
                    canBreak = False
                if ratings[i] > right and ans[i] <= ans[i+1]:
                    print('here')
                    ans[i] = ans[i+1] +1
                    canBreak = False
            if canBreak:
                break
        return sum(ans)

    