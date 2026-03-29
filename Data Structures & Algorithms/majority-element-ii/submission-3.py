class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1, num2, cnt1, cnt2 = 0, 0, 0, 0

        for n in nums:
            if n == num1:
                cnt1 += 1
            elif n == num2:
                cnt2 += 1
            elif cnt1 == 0:
                num1 = n
                cnt1 = 1
            elif cnt2 == 0:
                num2 = n
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        cnt1, cnt2 = 0, 0
        for n in nums:
            if n == num1:
                cnt1 += 1
            elif n == num2:
                cnt2 += 1
        print(num1, num2)
        print(cnt1, cnt2)
        res = []
        if cnt1 > (len(nums) // 3):
            res.append(num1)
        if cnt2 > (len(nums) // 3):
            res.append(num2)
        return res