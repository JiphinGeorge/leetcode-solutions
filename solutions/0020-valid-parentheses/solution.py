class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        typeMap = {'}':'{', ']':'[', ')':'('}
        for i in s:
            if i in ['{','[','(']:
                stack.append(i)
            else:
                if not stack:
                    return False
                elif stack[-1] == typeMap[i]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        return False
