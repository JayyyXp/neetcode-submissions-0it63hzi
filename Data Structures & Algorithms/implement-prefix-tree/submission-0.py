class PrefixTree:

    def __init__(self):
        self.words = set()
        self.pt = {}
        

    def insert(self, word: str) -> None:
        self.words.add(word)
        for i in range(len(word)):
            if word[0:i+1] in self.pt:
                self.pt[word[0:i+1]].append(word)
            else:
                self.pt[word[0:i+1]] = [word]


    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.pt
        