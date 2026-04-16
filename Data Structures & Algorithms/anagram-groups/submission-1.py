from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            temp_key = [0]*26
            for c in s:
                temp_key[ord(c) - ord('a')] +=1
            res[tuple(temp_key)].append(s)
        return list(res.values())