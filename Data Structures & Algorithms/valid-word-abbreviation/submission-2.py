class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        i = 0
        j = 0
        
        while j < len(word) and i < len(abbr):
            if abbr[i].isdigit():
                num = []
                while i < len(abbr) and abbr[i].isdigit():
                    num.append(abbr[i])
                    i += 1
                if num[0] == "0":
                    return False
                j += int("".join(num))
            else:
                if abbr[i] == word[j]:
                    i += 1
                    j += 1
                else:
                    print(abbr[i], word[j])
                    return False
        return j == len(word) and len(abbr) == i