class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # str1 is always longer
        if len(str2) > len(str1):
            str1, str2 = str2,str1

        for i in range(len(str2)-1,-1,-1):
            if str1[:i+1] == str2[:i+1]:
                commonLen = i+1
                commonStr = str1[:i+1]
                if (
                    (commonStr * (len(str2) // commonLen)) == str2 and
                    (commonStr * (len(str1) // commonLen)) == str1 
                ): 
                    return commonStr
        return ""


        