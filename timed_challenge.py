# Selected question from timed_challenge.txt:
# 13. Balanced Symbols
# Check if the brackets in a string are balanced.
# Input: "{[()]}"
# Output: True
# Input: "{[(])}"
# Output: False
#
# Use a stack to check whether every closing bracket matches the most recent
# unmatched opening bracket.

def balanced_symbols(text):
    if not isinstance(text, str):
        return False

    stack = []
    matching = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for character in text:
        if character in "([{":
            stack.append(character)
        elif character in ")]}":
            if not stack or stack.pop() != matching[character]:
                return False

    return len(stack) == 0


# Tests, including normal cases and edge cases.
if __name__ == "__main__":
    test_cases = [
        ("{[()]}", True),
        ("{[(])}", False),
        ("", True),
        ("()", True),
        ("((()))", True),
        ("([{}])", True),
        ("(", False),
        ("]", False),
        ("hello", True),
        ("abc(def[ghi]{jkl})", True),
        (123, False),          # wrong data type
        (None, False),         # wrong data type
    ]

    for value, expected in test_cases:
        result = balanced_symbols(value)
        print(f"{value!r} -> {result} (expected {expected})")
