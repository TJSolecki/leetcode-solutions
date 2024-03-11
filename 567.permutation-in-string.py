from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        char_counts = {}
        for c in s1:
            char_counts[c] = (char_counts.get(c) or 0) + 1

        current_counts = defaultdict(int)
        r = len(s1) - 1
        satisfied = 0
        for i in range(len(s1) - 1):
            curr = s2[i]
            current_counts[curr] += 1
            if current_counts.get(curr) == char_counts.get(curr):
                satisfied += 1
        while r < len(s2):
            curr = s2[r]
            current_counts[curr] += 1
            if current_counts.get(curr) == char_counts.get(curr):
                satisfied += 1

            if satisfied == len(char_counts.keys()):
                return True

            left_curr = s2[r - len(s1) + 1]
            if current_counts.get(left_curr) == char_counts.get(left_curr):
                satisfied -= 1
            current_counts[left_curr] -= 1

            r += 1

        return False
