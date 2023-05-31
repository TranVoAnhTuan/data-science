from typing import List
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(s):
            count = 0
            for i in s:
                if i == '(':
                    count += 1
                elif i == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0
        level = {s}
        while True:
            valid = []
            for s in level:
                if is_valid(s):
                    valid.append(s)
            if valid:
                return valid
            nextValid = set()
            for s in level:
                for i in range(len(s)):
                    if s[i] in ('(',')'):
                        nextValid.add(s[:i]+s[i+1:])
            level = nextValid
if __name__ == '__main__':
    s = "()())()"
    res = Solution()
    print(res.removeInvalidParentheses(s))