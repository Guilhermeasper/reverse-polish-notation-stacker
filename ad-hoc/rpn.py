# Description: Reverse Polish Notation Calculator

file_name = str(input('Enter file name: '))

expression = []

with open(file_name) as f:
    expression = f.read().splitlines()


def rpn_calc(expression):
    stack = []
    for item in expression:
        if item == '+':
            stack.append(stack.pop() + stack.pop())
        elif item == '-':
            stack.append(stack.pop() - stack.pop())
        elif item == '*':
            stack.append(stack.pop() * stack.pop())
        elif item == '/':
            stack.append(stack.pop() / stack.pop())
        else:
            stack.append(float(item))
    return stack.pop()


print(f'Resultado: {int(rpn_calc(expression))}')
