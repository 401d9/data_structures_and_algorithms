
def multi_bracket_validation(str_list):
    stack = []

    pairs = {')': '(', '}': '{', ']': '['}

    for char in str_list:

        if char in pairs.values():
            stack.append(char)

        if char in pairs.keys():
            if pairs.get(char) == stack[-1]:
                stack.pop(-1)

            else:
                return False

    if len(stack) > 0:
        return False
    else:
        return True


sample1 = '(', ')'
sample2 = '{', '(', '[', ']', ')', '}'
broke1 = '(', '[', ')', ']'
broke2 = '(', '[', '{', '}', ']'

print(multi_bracket_validation(broke2))
