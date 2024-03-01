def get_index(char):
    return ord(char) - ord("a")


class Trie(object):

    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isCompleteWord = False

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        if not word:
            self.isCompleteWord = True
            return
        char = word[0]
        if self.children[get_index(char)] != None:
            self.children[get_index(char)].insert(word[1:])
        else:
            self.children[get_index(char)] = Trie()
            self.children[get_index(char)].insert(word[1:])

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if not word:
            return self.isCompleteWord
        char = word[0]
        child_of_char = self.children[get_index(char)]
        if child_of_char != None:
            return child_of_char.search(word[1:])
        else:
            return False

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        if not prefix:
            return True
        char = prefix[0]
        child_of_char = self.children[get_index(char)]
        if child_of_char != None:
            return child_of_char.startsWith(prefix[1:])
        else:
            return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
