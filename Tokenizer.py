punctuators = [';', ',', ':', '[', ']', '{', '}', '(', ')']
operators = ['*', '/', '%', '+', '-', '<', '>', '&', 'or',
             'not', '>=', '<=', '!=', '==', '++', '+=', '=', '\\']
keywords = ['boolean', 'char', 'float', 'int', 'string', 'if', 'else', 'elif', 'break', 'jabtak', 'ke liye',
            'private', 'protected', 'public', 'static', 'class', 'new', 'empty', 'dar-amad', 'tawseeh',
            'supar', 'return', 'and', 'or', 'not']


def split_and_read_file(filename):
    lexemes = []  # List to store the lexemes
    line_number = 1  # Track the line number

    with open(filename, 'r') as file:
        source_code = file.read()  # Read the entire source code from the file

    current_position = 0  # Track the current position in the source code

    while current_position < len(source_code):
        current_char = source_code[current_position]

        if current_char.isspace():
            if current_char == '\n':
                line_number += 1
            current_position += 1
            continue

        if current_char in punctuators:
            lexemes.append((current_char, "Punctuator", line_number))
            current_position += 1
            continue

        if current_char in operators:
            token = current_char
            while current_position + 1 < len(source_code):
                next_char = source_code[current_position + 1]
                if token + next_char in operators:
                    token += next_char
                    current_position += 1
                else:
                    break
            lexemes.append((token, "Operator", line_number))
            current_position += 1
            continue

        if current_char.isalpha() or current_char == '_':
            current_lexeme = ''
            while current_position < len(source_code) and (source_code[current_position].isalnum() or source_code[current_position] == '_'):
                current_lexeme += source_code[current_position]
                current_position += 1
            lexeme_type = "Keyword" if current_lexeme in keywords else "Identifier"
            lexemes.append((current_lexeme, lexeme_type, line_number))
            continue

        if current_char.isdigit():
            current_lexeme = ''
            while current_position < len(source_code) and (source_code[current_position].isdigit() or source_code[current_position] == '.'):
                current_lexeme += source_code[current_position]
                current_position += 1
            if current_lexeme.count('.') <= 1:
                lexeme_type = "Float" if '.' in current_lexeme else "Integer"
                lexemes.append((current_lexeme, lexeme_type, line_number))
            else:
                lexemes.append((current_lexeme, "Invalid Number", line_number))
            continue

        current_position += 1

    return lexemes


filename = 'hello.txt'
lexemes = split_and_read_file(filename)

# Print lexemes with their type, name, and line number
for lexeme in lexemes:
    name, lexeme_type, line_number = lexeme
    print(f"Lexeme: {name}\tType: {lexeme_type}\tLine: {line_number}")
