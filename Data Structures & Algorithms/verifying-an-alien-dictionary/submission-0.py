class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderDict = []

        for i, word1 in enumerate(words):
            for j in range(i+1, len(words)):
                word2 = words[j]
                if word1[:len(word2)] == word2:
                    print(len(word1), len(word2))
                    return False

                #if len(word1) > len(word2):
                for k in range(len(word1)):
                    if word1[k] != word2[k]:
                        orderDict.append([word1[k],word2[k]])
                        break
        for l1,l2 in orderDict:
                i1, i2 = -1, -1
                for i,c in enumerate(order):
                    if c == l1:
                        i1 = i
                    if c == l2:
                        i2 = i
                if i1 > i2:
                    print(l1,l2)
                    return False
        return True