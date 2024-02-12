class Solution(object):

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_counts = {}
        for c in t:
            if t_counts.get(c) == None:
                t_counts[c] = 0
            t_counts[c] += 1

        substr_counts = {}
        l = 0
        have = 0
        need = len(t_counts.keys())
        min_substr = ""
        for r in range(len(s)):
            if substr_counts.get(s[r]) == None:
                substr_counts[s[r]] = 0
            substr_counts[s[r]] += 1

            if t_counts.get(s[r]) != None and substr_counts[s[r]] == t_counts[s[r]]:
                have += 1

            while have == need:
                if have == need and (
                    len(min_substr) == 0 or r - l + 1 < len(min_substr)
                ):
                    min_substr = s[l : r + 1]
                substr_counts[s[l]] -= 1
                if t_counts.get(s[l]) != None and substr_counts[s[l]] < t_counts[s[l]]:
                    have -= 1
                l += 1

        return min_substr
