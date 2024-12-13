class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '{': '}',
            '(': ')',
            '[': ']'
        }
        order = ['']
        for letter in s:
            if letter not in brackets.keys() and letter != order[-1]:
                return False
            if letter == order[-1]:
                order.pop()
            elif brackets[letter]:
                order.append(brackets[letter])
            else:
                return False
        if len(order) != 1:
            return False
        return True


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False