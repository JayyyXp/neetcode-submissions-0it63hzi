class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        x = 0
        for n in nums:
            x ^= n
        print(x)
        lowbit = x & (-x)

        a = 0
        b = 0
        for n in nums:
            if (n & lowbit) == 0:
                a ^= n
            else:
                b ^= n
        print(a, b)
        return [a, b]