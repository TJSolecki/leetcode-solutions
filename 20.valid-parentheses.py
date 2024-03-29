class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        parenMap = {
            "[": "]",
            "{": "}",
            "(": ")",
        }
        for c in s:
            if c in parenMap.keys():
                stack.append(c)
            else:
                if len(stack) > 0 and parenMap[stack[-1]] == c:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
