class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '{': '}',
            '(': ')',
            '[': ']'
        }
        order = ['']
        print(s)
        for letter in s:
            print('char')
            print(letter)
            print('order')
            print(order)
            if letter not in brackets.keys() and letter != order[-1]:
                return False
            if letter == order[-1]:
                print('a')
                order.pop()
            elif brackets[letter]:
                print('b')
                order.append(brackets[letter])
            else:
                return False
        return True
