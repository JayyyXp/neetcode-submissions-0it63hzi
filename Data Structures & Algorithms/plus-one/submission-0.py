class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 10 and carry == 0:
                return digits
            new = digits[i] + carry
            carry = (new // 10)
            digits[i] = new % 10
            #print(digits[i], carry)
        if carry > 0:
            return [carry] + digits
        return digits

            
