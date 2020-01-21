

def chkBalancedParanthesis(expr):

    s = []
    opens = ['{', '(', '[']

    for c in expr:
        if c in opens:
            s.append(c)
        else:
            if c == ']':
                if s.pop() == '[':
                    continue
                else:
                    return False
            elif c == ')':
                if s.pop() == '(':
                    continue
                else:
                    return False
            elif c == '}':
                if s.pop() == '{':
                    continue
                else:
                    return False
            else:
                return False
    return True

if __name__ == '__main__':
    expr = "{()}[]"

    if (chkBalancedParanthesis(expr)):
        print('Balanced')
    else:
        print('Unbalanced')