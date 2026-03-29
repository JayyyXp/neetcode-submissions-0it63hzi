class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            if word1[:len(word2)] == word2:
                print(len(word1), len(word2))
                return False

            #if len(word1) > len(word2):
            for k in range(len(word1)):
                if word1[k] != word2[k]:
                    i1 = order_index[word1[k]] 
                    i2 = order_index[word2[k]]
                    if i1 > i2:
                        return False
                    break
        return True