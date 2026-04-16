class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([char.lower() for char in s if char.isalnum()])
        left_index = 0 
        right_index = len(s) -1
        while left_index < right_index:
            if s[left_index] != s[right_index]:
                return False
            left_index += 1
            right_index -=1
        return True

        