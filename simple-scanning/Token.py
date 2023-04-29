from TokenType import TokenType


class Token:

    def __init__(self, token_value: str):

        self.type = self.tokenTypeByRegex(token_value)
        self.lexeme = token_value

    def __str__(self):
        return f"Token [type={self.type.name}, lexeme={self.lexeme}]"

    def tokenTypeByRegex(self, token_value: str):
        number_regex = r'^\d+$'
        operator_regex = r'^[+\-*/]$'
        if re.match(number_regex, token_value):
            return TokenType.INT
        elif re.match(operator_regex, token_value):
            return TokenType.OPERATOR
        else:
            raise ValueError(f'Invalid token: {token_value}')
