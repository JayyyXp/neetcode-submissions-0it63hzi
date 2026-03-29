class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #for i in range(len(numbers)):
        #    num1 = numbers[i]
        #    for j in range(i + 1, len(numbers)):
        #        num2 = numbers[j]

        #        if num1 + num2 == target:
        #            return [i+1, j+1]

        l, r = 0, len(numbers) - 1

        while l < r:

            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l +=1
            else:
                return [l+1, r+1] 