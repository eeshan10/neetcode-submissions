import operator
import numpy as np
import math
import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a / b)
        }

        for el in tokens:
            if el not in operations:
                stack.append(int(el))
            else:
                second_integer = stack.pop()   # right operand
                first_integer = stack.pop()    # left operand
                result = operations[el](first_integer, second_integer)
                stack.append(result)

        return stack[-1]

        