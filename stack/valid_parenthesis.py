from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        # Try brute force
        bracket_dict = {"(":")", "[":"]", "{":"}"}
        stack = deque()

        for bracket in s:
            if bracket in bracket_dict.keys():
                stack.append(bracket)
            else:
                if not stack:
                    return False
                opening_bracket = stack.pop()
                if bracket_dict[opening_bracket] != bracket:
                    return False
        return not stack