punctuators = [';', ',', ':', '[', ']', '{', '}', '(', ')']
operators = ['*', '/', '%', '+', '-', '<', '>', '&', 'or',
             'not', '>=', '<=', '!=', '==', '++', '+=', '=', '\\']
keywords = ['boolean', 'char', 'float', 'int', 'string', 'agar', 'warna', 'elif', 'torna,''jabtak', 'ke liye',
            'private', 'protected', 'public', 'static', 'class', 'naya', 'khaali', 'dar-amad', 'tawseeh',
            'supar', 'wapis', 'and', 'or', 'not']


def split_and_read_file(filename):
    characters = []  # List to store the lexemes
    character_count = 0  # Counter for total characters appended
    inside_comment = False  # Flag to track if inside a comment
    current_lexeme = ''  # Variable to store the current lexeme

    with open(filename, 'r') as file:
        current_char = file.read(1)  # Read the first character from the file

        while current_char:  # Continue reading until end of file
            dot_count = 0

            if inside_comment:
                if current_char == '\n':  # If inside a comment, ignore characters until newline
                    inside_comment = False
                current_char = file.read(1)  # Read the next character
                continue

            elif current_char.isspace():  # If the character is whitespace
                if current_lexeme:  # If there are previous characters, append the current lexeme
                    characters.append(current_lexeme)
                    character_count += len(current_lexeme)
                    current_lexeme = ''  # Reset the current lexeme
                # Append the whitespace character
                characters.append(current_char)
                character_count += 1
                current_char = file.read(1)  # Read the next character
                continue

            elif current_char in punctuators:  # If the character is a punctuator
                if current_lexeme:  # If there are previous characters, append the current lexeme
                    characters.append(current_lexeme)
                    character_count += len(current_lexeme)
                    current_lexeme = ''  # Reset the current lexeme
                characters.append(current_char)
                character_count += 1
                current_char = file.read(1)  # Read the next character
                continue

            elif current_char in operators:  # If the character is an operator
                if current_lexeme:  # If there are previous characters, append the current lexeme
                    characters.append(current_lexeme)
                    character_count += len(current_lexeme)
                    current_lexeme = ''  # Reset the current lexeme

                token = current_char
                i = character_count  # Track the index of the current character

                # Concatenate consecutive operators
                while current_char := file.read(1):
                    if token + current_char in operators:
                        token += current_char
                    else:
                        break

                characters.append(token)
                character_count += len(token)
                continue

            elif current_char == '\n':  # If the character is a newline
                if current_lexeme:  # If there are previous characters, append the current lexeme
                    characters.append(current_lexeme)
                    character_count += len(current_lexeme)
                    current_lexeme = ''  # Reset the current lexeme
                characters.append(current_char)  # Append the newline character
                character_count += 1
                current_char = file.read(1)  # Read the next character
                continue

            # If the character is an alphabetic character or underscore
            elif current_char.isalpha() or current_char == '_':
                if current_lexeme and not current_lexeme.isdigit():  # If there are previous characters and not a digit
                    characters.append(current_lexeme)
                    character_count += len(current_lexeme)
                    current_lexeme = ''  # Reset the current lexeme

                current_lexeme += current_char
                current_char = file.read(1)  # Read the next character

                while current_char.isalpha() or current_char == '_':
                    current_lexeme += current_char
                    current_char = file.read(1)  # Read the next character

                continue

            # If the character is a hash (#) indicating a comment
            elif current_char == '#':
                inside_comment = True
                current_char = file.read(1)  # Read the next character
                continue
            elif current_char.isdigit():  # If the character is a digit or a decimal point

                if current_lexeme:  # If there are previous characters, append the current lexeme
                    characters.append(current_lexeme)
                    character_count += len(current_lexeme)
                    current_lexeme = ''  # Reset the current lexeme

                if current_char == '.':
                    dot_count += 1

                    current_lexeme += current_char
                    current_char = file.read(1)  # Read the next character

                    while current_char.isdigit():
                        current_lexeme += current_char
                        current_char = file.read(1)  # Read the next character

                else:
                    print(current_char, "  ", dot_count, "  ", current_lexeme)

                    current_lexeme += current_char
                    current_char = file.read(1)  # Read the next character

                    while (current_char.isdigit() or current_char == '.'):
                        if current_char == '.':
                            if dot_count == 1:
                                characters.append(current_lexeme)
                                character_count += len(current_lexeme)
                                current_lexeme = ''
                                print(current_char, "  ", dot_count,
                                      "  ", current_lexeme)
                                break

                            dot_count += 1
                            current_lexeme += current_char
                            # Read the next character
                            current_char = file.read(1)
                        else:
                            current_lexeme += current_char
                            # Read the next character
                            current_char = file.read(1)

                continue

            current_lexeme += current_char
            current_char = file.read(1)  # Read the next character

    if current_lexeme:
        characters.append(current_lexeme)

    return characters


filename = 'hello.txt'
lexemes = split_and_read_file(filename)
print(lexemes)
# ============================================
punctuators = [';', ',', ':', '[', ']', '{', '}', '(', ')']
operators = ['*', '/', '%', '+', '-', '<', '>', '&', 'or',
             'not', '>=', '<=', '!=', '==', '++', '+=', '=', '\\']
keywords = ['boolean', 'char', 'float', 'int', 'string', 'agar', 'warna', 'elif', 'torna', 'jabtak', 'ke liye',
            'private', 'protected', 'public', 'static', 'class', 'naya', 'khaali', 'dar-amad', 'tawseeh',
            'supar', 'wapis', 'and', 'or', 'not']


def split_and_read_file(filename):
    lexemes = []  # List to store the lexemes
    line_number = 1  # Track the line number
    character_count = 0  # Counter for total characters appended

    with open(filename, 'r') as file:
        current_char = file.read(1)  # Read the first character from the file

        while current_char:  # Continue reading until end of file
            dot_count = 0

            if current_char.isspace():  # If the character is whitespace
                if current_char == '\n':  # If the character is a newline
                    line_number += 1
                current_char = file.read(1)  # Read the next character
                continue

            elif current_char in punctuators:  # If the character is a punctuator
                lexemes.append((current_char, "Punctuator", line_number))
                character_count += 1
                current_char = file.read(1)  # Read the next character
                continue

            elif current_char in operators:  # If the character is an operator
                token = current_char
                i = character_count  # Track the index of the current character

                # Concatenate consecutive operators
                while current_char := file.read(1):
                    if token + current_char in operators:
                        token += current_char
                    else:
                        break

                lexemes.append((token, "Operator", line_number))
                character_count += len(token)
                continue

            # If the character is an alphabetic character or underscore
            elif current_char.isalpha() or current_char == '_':
                current_lexeme = ''

                while current_char.isalnum() or current_char == '_':
                    current_lexeme += current_char
                    current_char = file.read(1)  # Read the next character

                if current_lexeme in keywords:
                    lexemes.append((current_lexeme, "Keyword", line_number))
                else:
                    lexemes.append((current_lexeme, "Identifier", line_number))

                continue

            elif current_char.isdigit():  # If the character is a digit or a decimal point
                current_lexeme = ''

                while current_char.isdigit() or current_char == '.':
                    if current_char == '.':
                        if dot_count == 1:
                            lexemes.append(
                                (current_lexeme, "Invalid Number", line_number))
                            break

                        dot_count += 1

                    current_lexeme += current_char
                    current_char = file.read(1)  # Read the next character

                if dot_count == 0:
                    lexemes.append((current_lexeme, "Integer", line_number))
                elif dot_count == 1:
                    lexemes.append((current_lexeme, "Float", line_number))
                else:
                    lexemes.append(
                        (current_lexeme, "Invalid Number", line_number))

                continue

            current_char = file.read(1)  # Read the next character

    return lexemes


filename = 'hello.txt'
lexemes = split_and_read_file(filename)

# Print lexemes with their type, name, and line number
for lexeme in lexemes:
    name, lexeme_type, line_number = lexeme
    print(f"Lexeme: {name}\tType: {lexeme_type}\tLine: {line_number}")
