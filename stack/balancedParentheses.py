

def chkBalancedParanthesis(expr):

    s = []
    opens = ['{', '(', '[']

    for c in expr:
        if c in opens:
            s.append(c)
        else:
            try:
                if c == ']':
                    if s.pop() == '[':
                        continue
                elif c == ')':
                    if s.pop() == '(':
                        continue
                elif c == '}':
                    if s.pop() == '{':
                        continue
            except IndexError as ex:
                return False
    return len(s) == 0

if __name__ == '__main__':
    expr = "{()}[]"

    if (chkBalancedParanthesis(expr)):
        print('Balanced')
    else:
        print('Unbalanced')