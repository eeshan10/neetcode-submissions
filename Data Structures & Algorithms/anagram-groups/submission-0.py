from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_list = defaultdict(list)
        for s in strs:
            sorteds = ''.join(sorted(s))
            final_list[sorteds].append(s)
        return  list(final_list.values())