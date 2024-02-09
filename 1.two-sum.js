/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const mem = new Map();
    for (const [index, num] of nums.entries()) {
        const complement = target - num;
        if (Array.from(mem.keys()).includes(complement)) {
            return [mem.get(complement), index];
        }
        mem.set(num, index);
    }
};
