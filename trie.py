from collections import deque


class Trie:

    def __init__(self):
        self.graph = {}
        self.is_end = False

    def insert(self, word):
        word = deque([char for char in word])
        self.do_insert(word, self)

    def do_insert(self, word, trie):
        letter = word.popleft()

        if letter not in trie.graph:
            letter_trie = Trie()
            trie.graph[letter] = letter_trie

        letter_trie = trie.graph[letter]

        if len(word) > 0:
            self.do_insert(word, letter_trie)
        else:
            letter_trie.is_end =True

    def search(self, word):
        word = deque(word)
        return self.traverse(word, self, True)

    def traverse(self, word, trie, search=False):
        letter = word.popleft()

        if letter not in trie.graph:
            return False

        letter_trie = trie.graph[letter]

        if len(word) > 0:
            return self.traverse(word, letter_trie, search)
        else:
            if search:
                return letter_trie.is_end
            return True

    def startsWith(self, prefix):
        prefix = deque(prefix)
        return self.traverse(prefix, self)


trie = Trie()
print(trie.insert("apple"))
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
print(trie.insert("app"))
print(trie.search("app"))
