class Solution:
    def alienOrder(self, words: list[str]) -> str:
        adj = {c: set() for word in words for c in word}
        for i in range(len(words) - 1):
            word_1, word_2 = words[i], words[i + 1]
            min_len = min(len(word_1), len(word_2))
            if word_1[:min_len] == word_2[:min_len] and len(word_1) > len(word_2):
                return ""

            for j in range(min_len):
                if word_1[j] != word_2[j]:
                    adj[word_1[j]].add(word_2[j])
                    break

        res = []
        visited = {}  # False = visited, True = in current path

        def dfs(curr: str) -> bool:
            if curr in visited:
                return visited[curr]
            visited[curr] = True
            for neighbor in adj[curr]:
                if dfs(neighbor):
                    return True

            visited[curr] = False
            res.append(curr)
            return False

        for c in adj:
            if dfs(c):
                return ""

        res.reverse()
        return "".join(res)
