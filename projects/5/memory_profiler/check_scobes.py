def is_balanced(string: str):
    if not string or len(string) & 1:
        return False

    open_s = "({["
    closed_s = ")}]"
    stack = []

    for char in string:
        if char in open_s:
            stack.append(char)  # Если текущий символ является открывающей скобкой поместите его в массив
        if char in closed_s:
            if not stack:
                return False  # Если символа нет, то нет баланса
            top = stack.pop()  # Если текущий символ является закрывающей скобкой извлечь его из массива
            if (top == '(' and char != ')') or (top == '{' and char != '}' or (top == '[' and char != ']')):
                return False  # Если символ "зеркально" не совпадает, то нет баланса
    return not stack  # Если массив пустой, то есть баланс


if __name__ == '__main__':
    string0 = '{()}'            # balanced
    string1 = '{()}[{}]'        # balanced
    string2 = '{[{}{}]}[()]'    # balanced
    string3 = '{(})'            # not balanced
    string4 = '{[})'            # not balanced
    print('balanced' if is_balanced(string=string3) else 'not balanced')
