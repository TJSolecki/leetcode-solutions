    const map = {
        "}": "{",
        "]": "[",
        ")": "(",
    };
/**
 * @param {string} s
 * @return {boolean}
 */
    var isValid = function(s) {
        const stack = [];
        for (const char of s) {
            if (Object.values(map).includes(char)) {
                stack.push(char);
            }
            else {
                if (stack.pop() !== map[char]) {
                    return false
                }
            }
        }
        return stack.length === 0;
    };
