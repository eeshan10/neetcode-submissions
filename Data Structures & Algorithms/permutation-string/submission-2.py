class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr_s1 = [0]*26
        for el in s1:
            arr_s1[ord(el) - ord('a')] +=1
        for i in range(len(s2)):
            arr_s2 = [0]*26
            win = s2[i : i+len(s1)]
            for el in win:
                arr_s2[ord(el) - ord('a')] +=1
            if arr_s2 == arr_s1:
                return True
        return False
        # window = set()
        # s1_set = set(s1)
        # max_length = 0
        # l = 0
        # r = len(s1_set)
        # print(r)
        # for l in range(len(s2)):
        #     print(s2[l: l+r])
        #     if set(s2[l: l+ r]) == s1_set:
        #         return True
        # return False
        