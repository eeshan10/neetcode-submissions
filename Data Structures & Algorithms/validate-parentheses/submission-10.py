class Solution:
    def isValid(self, s: str) -> bool:
        close_dict = {')' : '(', '}' : '{', ']': '['}
        closing_brackets = []
        opening_brackets = []
        for el in s:
            print(el)
            if el in close_dict.keys():
                if opening_brackets and opening_brackets[-1] == close_dict[el]:
                    opening_brackets.pop()
                else:
                    return False
            else:
                opening_brackets.append(el)
        if not opening_brackets:
            return True
        else:
            return False
                
        
        