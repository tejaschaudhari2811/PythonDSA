class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.word_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        current = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if not current.child[index]:
                current.child[index] = TrieNode()
            current = current.child[index]
        current.word_end = True
    
    def search(self, key: str):
        current = self.root
        for letter in key:
            index = ord(letter) - ord('a')
            if not current.child[index]:
                return False
            else:
                current = current.child[index]
        return True
    

trie = Trie()
trie.insert("Tejas")
print(trie.search("Tejas"))