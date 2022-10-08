class TrieNode:
    def __init__(self) -> None:
        self.children = [None] * 26
        self.wordStopAt = [False] * 26

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        letterOrder = None
        prev = None
        for letter in word:
            letterOrder = ord(letter) - 97
            if current.children[letterOrder] is None:
                current.children[letterOrder] = TrieNode()
            prev = current
            current = current.children[letterOrder]
        prev.wordStopAt[letterOrder] = True

    def searchRecursive(self, word: str, idx: int, node: TrieNode) -> bool:
        if idx == len(word):
            return False
        letter = word[idx]
        letterOrder = ord(letter) - 97
        if letter == '.':
            if idx == len(word) - 1:
                if node is not None:
                    for item in node.wordStopAt:
                        if item == True:
                            return True
                return False
            for child in node.children:
                if child == None:
                    continue
                found = self.searchRecursive(word, idx + 1, child)
                if found == True:
                    return True
            return False
        else:
            if node.children[letterOrder] is not None:
                if idx == len(word) - 1 and node.wordStopAt[letterOrder]:
                    return True
                return self.searchRecursive(word, idx + 1, node.children[letterOrder])
            return False

    def search(self, word: str) -> bool:
        return self.searchRecursive(word, 0, self.root)


obj = WordDictionary()
words = [
    "bad", "dad", "mad", "apple", "apply", "applying", "application","a"
]
for word in words:
    obj.addWord(word)

tests = [
    (".ad", True), ("..d", True), ("...", True), ("app..", True), ("ap.ly", True),
    ("a.ly", False), ("b.d", True), ("d.b", False), ("...lication", True),
    ("...licatio", False), ("applicationing", False), (".", True), ("a.", False)
]
for word, res in tests:
    print(obj.search(word) == res)

tests = [
    ("bad", True), ("dad", True), ("mad", True), ("mada", False), ("ba", False),
    ("app", False), ("applying", True), ("apply", True), ("appli", False), ("application", True),
    ("a", True)
]
for word, res in tests:
    print(obj.search(word) == res)

["WordDictionary","addWord","addWord","search","search","search","search","search","search"]
[[],["a"],["a"],["."],["a"],["aa"],["a"],[".a"],["a."]]