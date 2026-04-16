class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for el in s:
            s_dict[el] = s_dict.get(el, 0) + 1
        for el in t:
            t_dict[el] = t_dict.get(el, 0) + 1
        if s_dict == t_dict:
            return True 
        else:
            return False