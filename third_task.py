def checking_brackets(s):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    for i in s:
        if i in brackets.values():
            stack.append(i)
        elif i in brackets.keys():
            if not stack or stack.pop() != brackets[i]:
                return False
        else:

            continue

    return not stack




test_cases = ["{}()[]", "{]"]

for i in test_cases:
    result = checking_brackets(i)
    if result:
        print(f'"{i}" -> To\'g\'ri')
    else:
        print(f'"{i}" -> Noto\'g\'ri')
