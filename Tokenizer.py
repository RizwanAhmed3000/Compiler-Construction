import re


class Token:
    def _init_(self, category, value, line_number):
        self.category = category
        self.value = value
        self.line_number = line_number


class Lexer:
    def _init_(self, filename):
        self.filename = filename
        self.line_number = 1

    def tokenize(self):
        tokens = []

        with open(self.filename, 'r') as file:
            for line in file:
                tokens.extend(self._tokenize_line(line))

        return tokens

    def _tokenize_line(self, line):
        line_tokens = []
        position = 0

        patterns = [
            (r'\binterface\b', 'CP'),
            (r'[a-zA-Z_][a-zA-Z0-9_]*', 'ID'),
            (r'\d+\.\d+', 'VP'),
            (r'\d+', 'VP'),
            (r'(\+{2}|\+=)', 'OP'),
            (r'([+*/%<>=&]|>=|<=|!=|==)', 'OP'),
            (r'[();,.]', 'P'),
            (r'[\[\]{}/]', 'P'),
            (r'"[^"\\](?:\\.[^"\\])*"', 'STR'),
            (r"'[^'\\](?:\\.[^'\\])*'", 'STR'),
            (r'\\', 'ESCAPED'),
            (r'\n', 'LN'),
            (r'\S', 'UNKNOWN')
        ]

        while position < len(line):
            matched = False
            for pattern, category in patterns:
                match = re.match(pattern, line[position:])
                if match:
                    value = match.group()
                    line_tokens.append(
                        Token(category, value, self.line_number))
                    position += len(value)
                    matched = True
                    break

            if not matched:
                position += 1

        return line_tokens


# Usage example
filename = 'hello.txt'

lexer = Lexer(filename)
tokens = lexer.tokenize()

for token in tokens:
    print(
        f"Category: {token.category}\tValue: {token.value}\tLine Number: {token.line_number}")
