from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordlist: list[str]) -> int:
        if endWord not in wordlist:
            return 0

        wordlist.append(beginWord)
        neighbors = defaultdict(list)

        for word in wordlist:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]
                neighbors[pattern].append(word)

        visited = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1 :]
                    for neighbor in neighbors[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
            res += 1

        return 0
