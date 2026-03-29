class WordDictionary:

    def __init__(self):
        self.map = {}    

    def addWord(self, word: str) -> None:
        self.map[word] = []

        dotWords = self.dot_variations(word)
        #print(dotWords)
        for dotWord in dotWords:
            if dotWord in self.map:
                self.map[dotWord].append(word)
            else:
                self.map[dotWord] = [word]
            self.map[word].append(dotWord)


    def dot_variations(self, word):
        ans = []
        def dfs(idx, dotWord):
            if idx > len(word) - 1:
                ans.append(dotWord)
                return
            dfs(idx + 1, dotWord + '.')
            dfs(idx + 1, dotWord + word[idx])

        dfs(0, '')
        return ans
    
    def search(self, word: str) -> bool:
        return word in self.map
        
