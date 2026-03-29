class Solution:
    def totalFruit(self, fruits: List[int]) -> int:


        fruit1 = -1
        fruit2 = -1
        fruit1last = -1
        fruit2last = -1

        ans = 0
        l = 0
        for r in range(len(fruits)):
            if fruit1 == -1:
                fruit1 = fruits[r]
                fruit1last = r
              
            elif fruit2 == -1 and fruits[r] != fruit1:
                fruit2 = fruits[r]
                fruit2last = r
              
            elif fruits[r] == fruit1:
                fruit1last = r
            elif fruits[r] == fruit2:
                fruit2last = r
            else:
                # record ans between r-1 and ll
                #print(fruits[l:r+1])
                
                if fruit1last < fruit2last:
                    l = fruit1last + 1 
                    fruit1 = fruits[r]
                    fruit1last = r
                else:
                    l = fruit2last + 1 
                    fruit2 = fruits[r]
                    fruit2last = r
            ans = max(ans, r-l+1)
        return ans 