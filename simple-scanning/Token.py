from TokenType import TokenType
import re


class Token:

    def __init__(self, token_value: str):

        self.type = Token.tokenTypeByRegex(token_value)
        self.lexeme = token_value

    def __str__(self):
        return f"Token [type={self.type.name}, lexeme={self.lexeme}]"

    @staticmethod
    def tokenTypeByRegex(token_value: str):
        OPERATOR_TOKEN_TYPE_MAP = {
            '+': TokenType.PLUS,
            '-': TokenType.MINUS,
            '*': TokenType.MUL,
            '/': TokenType.DIV,
        }
        number_regex = r'^\d+$'
        operator_regex = r'^[+\-*/]$'
        if re.match(number_regex, token_value):
            return TokenType.INT
        elif re.match(operator_regex, token_value):
            return OPERATOR_TOKEN_TYPE_MAP[token_value]
        else:
            raise ValueError(f'Invalid token: {token_value}')
