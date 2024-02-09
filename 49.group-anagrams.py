class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mem = {}
        for s in strs:
            chars = list(s)
            chars.sort()
            sorted_s = str(''.join(chars))
            if not mem.get(sorted_s):
                mem[sorted_s] = []
            mem[sorted_s].append(s)

        return list(mem.values());
            
        
