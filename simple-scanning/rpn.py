# Description: Reverse Polish Notation Calculator
from Token import Token
from TokenType import TokenType


file_name = str(input('Enter file name: '))

expression = []

with open(file_name) as f:
    expression = f.read().splitlines()


def convert_expression_to_tokens(expression):
    tokens = []
    for item in expression:
        tokens.append(Token(item))
    return tokens


def operate_tokens(token1, token2, operator):
    if operator.type == TokenType.PLUS:
        return token1 + token2
    elif operator.type == TokenType.MINUS:
        return token1 - token2
    elif operator.type == TokenType.MUL:
        return token1 * token2
    elif operator.type == TokenType.DIV:
        return token1 / token2
    else:
        raise ValueError(f'Invalid operator: {operator}')


def rpn(tokens):
    stack = []
    for token in tokens:
        if token.type != TokenType.INT:
            if (len(stack) < 2):
                raise ValueError(
                    f'Invalid expression: {[token.lexeme for token in tokens]}')
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operate_tokens(operand1, operand2, token)
            stack.append(result)
        else:
            stack.append(float(token.lexeme))
    return stack.pop()


tokens = convert_expression_to_tokens(expression)
result = rpn(tokens)
print(result)
