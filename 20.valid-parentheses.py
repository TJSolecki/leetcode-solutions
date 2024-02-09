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
        for char in s:
            if char in parenMap.keys():
                stack.append(char)
            else:
                if stack[len(stack) - 1] == parenMap[char]:
                    stack.pop()
                else:
                    return False
        return True
