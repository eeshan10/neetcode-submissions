class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        arr_s1 = [0] * 26
        arr_s2 = [0] * 26
        for ch in s1:
            arr_s1[ord(ch) - ord('a')] += 1
        l = 0
        for r in range(len(s2)):
            arr_s2[ord(s2[r]) - ord('a')] += 1

            if r - l + 1 > len(s1):
                arr_s2[ord(s2[l]) - ord('a')] -= 1
                l += 1

            if r - l + 1 == len(s1) and arr_s1 == arr_s2:
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
        