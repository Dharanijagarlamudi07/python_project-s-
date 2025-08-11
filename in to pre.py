def is_operator(c):
    return c in ['+', '-', '*', '/', '^']

def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    return 0

def infix_to_prefix(expression):
    # Reverse the infix expression
    expression = expression[::-1]
    
    # Replace ( with ) and vice versa
    expression = ''.join(['(' if ch == ')' else ')' if ch == '(' else ch for ch in expression])

    stack = []
    result = []

    for ch in expression:
        if ch.isalnum():  # Operand
            result.append(ch)
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # Remove '('
        elif is_operator(ch):
            while (stack and precedence(ch) < precedence(stack[-1]) or
                   (ch == '^' and stack and precedence(ch) == precedence(stack[-1]))):
                result.append(stack.pop())
            stack.append(ch)

    # Pop remaining operators from stack
    while stack:
        result.append(stack.pop())

    # Reverse result to get prefix
    return ''.join(result[::-1])

# Example usage
infix_expr = "(A+B)C-(D-E)(F+G)"
prefix_expr = infix_to_prefix(infix_expr)
print("Prefix Expression:", prefix_expr)