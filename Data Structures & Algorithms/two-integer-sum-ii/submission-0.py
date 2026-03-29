class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):
            num1 = numbers[i]
            for j in range(i + 1, len(numbers)):
                num2 = numbers[j]

                if num1 + num2 == target:
                    return [i+1, j+1]