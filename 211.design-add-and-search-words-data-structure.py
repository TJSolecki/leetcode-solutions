class TrieNode:
    def __init__(self):
        self.children = {}
        self.isCompleted = False

    def search(self, word):
        if not len(word):
            return self.isCompleted

        curr = self
        char = word[0]
        if curr.children.get(char):
            return curr.children[char].search(word[1:])
        elif char == ".":
            result = False
            for key in curr.children.keys():
                result = result or curr.children[key].search(word[1:])
            return result

        return False


class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        while word:
            char = word[0]
            if not curr.children.get(char):
                curr.children[char] = TrieNode()
                curr = curr.children[char]
            else:
                curr = curr.children[char]
            word = word[1:]

        curr.isCompleted = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return self.root.search(word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
