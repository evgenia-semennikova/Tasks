def pop(stack):
    if stack:
        return stack.pop()
    else:
        return 'empty'


def is_correct(line):
    stack = []
    opened = ('(', '[', '{')
    pairs = (['(', ')'], ['[', ']'], ['{', '}'])
    for s in line:
        if s in opened:
            stack.append(s)
        else:
            if [pop(stack), s] not in pairs:
                    return 'Incorrect'
    if stack:
        return 'Incorrect'
    else:
        return 'Correct'


def main():
    line = input()
    print(is_correct(line))


if __name__ == "__main__":
          main()

