# python3

import unittest

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type

        self.position = position + 1

    def match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False


def program(text):
    balance = None

    opening_brackets_stack = []
    for i, nextb in enumerate(text):
        if nextb == '(' or nextb == '[' or nextb == '{':
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(nextb, i))
        if nextb == ')' or nextb == ']' or nextb == '}':
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                balance = i + 1
                break
            elif opening_brackets_stack[len(opening_brackets_stack) - 1].match(nextb):
                opening_brackets_stack.pop()
            else:
                balance = i + 1
                break
                # Printing answer, write your code here
    if opening_brackets_stack != [] and balance is None:
        balance = opening_brackets_stack.pop().position
    if balance is None:
        return "Success"
    else:
        return str(balance)


class MyTest(unittest.TestCase):

    def testOne(self):
        for x in range(1, 54):
            if x < 10:
                x = str(x)
                x = '0'+x
            else:
                x = str(x)
            print("Test", x, "... ", end="")
            t = open('tests/'+x, 'r')
            a = open('tests/'+x+'.a', 'r')
            self.assertEqual(program(t.readline()), a.readline().rstrip())
            print("successful.")
            t.close()
            a.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
    text = input()
    print(program(text))
