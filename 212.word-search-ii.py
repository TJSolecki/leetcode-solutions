class TrieNode:
    def __init__(self):
        self.children = {}
        self.isCompleteWord = False

    def insert(self, word):
        curr = self
        while word:
            char = word[0]
            if not curr.children.get(char):
                curr.children[char] = TrieNode()
                curr = curr.children[char]
            else:
                curr = curr.children[char]
            word = word[1:]

        curr.isCompleteWord = True


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        rows, cols = len(board), len(board[0])
        root = TrieNode()
        res = set()
        visited = set()
        for word in words:
            root.insert(word)

        def search_word(trie_node: TrieNode, row, col, word):
            if trie_node.isCompleteWord:
                res.add(word)

            if (
                row < 0
                or col < 0
                or row >= rows
                or col >= cols
                or not trie_node.children.get(board[row][col])
                or (row, col) in visited
            ):
                return

            visited.add((row, col))
            char = board[row][col]
            new_word = word + char
            search_word(trie_node.children[char], row - 1, col, new_word)
            search_word(trie_node.children[char], row + 1, col, new_word)
            search_word(trie_node.children[char], row, col - 1, new_word)
            search_word(trie_node.children[char], row, col + 1, new_word)
            visited.remove((row, col))

        for r in range(rows):
            for c in range(cols):
                search_word(root, r, c, "")

        return list(res)
