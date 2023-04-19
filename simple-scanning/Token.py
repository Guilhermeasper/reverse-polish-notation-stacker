from TokenType import TokenType


class Token:

    def __init__(self, token_type: TokenType, token_value: str):

        self.type = token_type
        self.lexeme = token_value

    def __str__(self):

        return f"Token [type={self.type.name}, lexeme={self.lexeme}]"
