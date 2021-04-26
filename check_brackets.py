# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def find_mismatch(text):
    opening_brackets_stack = []
    mates = {")": "(", "]": "[", "}": "{"}
    for i, char in enumerate(text):
        if char in mates.values():
            opening_brackets_stack.append(Bracket(char, i + 1))

        if char in mates.keys():
            if len(opening_brackets_stack) == 0 or mates[char] != opening_brackets_stack.pop().char:
                return i + 1
    if len(opening_brackets_stack) > 0:
        return opening_brackets_stack.pop().position
    else:
        return 0 

def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch > 0:
        print(mismatch)
    else:
        print("Success")


def test():
    samples = {"}": 1, "[]" : 0, "{}[]" : 0, "[()]" : 0, "(())" : 0, "{[]}()" : 0, "{" : 1, "{[}" : 3, "foo(bar)" : 0, "foo(bar[i)" : 10, "foo(bar": 4}
    for string, expected in samples.items():
        result = find_mismatch(string)
        if result == expected:
            print("passed")
        else:
            print(f"FAILED: expected: {expected}, got: {result}")

if __name__ == "__main__":
#    test()
    main()

