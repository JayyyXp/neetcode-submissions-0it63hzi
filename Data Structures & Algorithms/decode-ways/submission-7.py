class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        
        def helper(index):
            # Base cases
            if index == len(s):
                return 1  # Empty string has 1 way to decode (end of valid sequence)
            
            # Leading zero can't be decoded
            if s[index] == '0':
                return 0
                
            # Check cache
            if index in cache:
                return cache[index]
            
            # Try single digit
            result = helper(index + 1)
            
            # Try two digits if possible
            if index + 1 < len(s) and int(s[index:index+2]) <= 26:
                result += helper(index + 2)
                
            cache[index] = result
            return result
            
        return helper(0)