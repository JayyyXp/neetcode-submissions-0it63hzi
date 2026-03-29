class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        print(s1, s2, s3)
        if s3 == "":
            return s1 == "" and s2 == ""

        if len(s1) > 0 and s1[0] == s3[0]:
            if self.isInterleave(s1[1:], s2, s3[1:]):
                return True
        if len(s2) > 0 and s2[0] == s3[0]:
            if self.isInterleave(s1, s2[1:], s3[1:]):
                return True
        return False


        