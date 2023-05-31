punctuators = [';', ',', ':', '[', ']', '{', '}', '(', ')']
operators = ['*', '/', '%', '+', '-', '<', '>', '&', 'or', 'not', '>=', '<=', '!=', '==', '++', '+=', '=','\\']
keywords = ['boolean','char','float','int','string','agar','warna','elif','torna,''jabtak','ke liye',
                'private','protected','public','static','class','naya','khaali','dar-amad','tawseeh',
                'supar','wapis','and','or','not']


def split_and_read_file(filename):
    characters = []  # List to store the lexemes
    character_count = 0  # Counter for total characters appended
    inside_comment = False  # Flag to track if inside a comment
    current_lexeme = ''  # Variable to store the current lexeme

    with open(filename, 'r') as file:
        current_char = file.read(1)  # Read the first character from the file

        while current_char:  # Continue reading until end of file
            dot_count=0
            
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
                characters.append(current_char)  # Append the whitespace character
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

            elif current_char.isalpha() or current_char == '_':  # If the character is an alphabetic character or underscore
                if current_lexeme and not current_lexeme.isdigit():  # If there are previous characters and not a digit
                    characters.append(current_lexeme)
                    character_count += len(current_lexeme)
                    current_lexeme = ''  # Reset the current lexeme

                current_lexeme += current_char
                current_char = file.read(1)  # Read the next character
                
                while current_char.isalpha()  or current_char == '_':
                    current_lexeme += current_char
                    current_char = file.read(1)  # Read the next character

                continue

            elif current_char == '#':  # If the character is a hash (#) indicating a comment
                inside_comment = True
                current_char = file.read(1)  # Read the next character
                continue
            elif current_char.isdigit( ) :  # If the character is a digit or a decimal point
                
                if current_lexeme:  # If there are previous characters, append the current lexeme
                    characters.append(current_lexeme)
                    character_count += len(current_lexeme)
                    current_lexeme = ''  # Reset the current lexeme
                
                if current_char == '.'  :
                    dot_count+=1
                           
                    current_lexeme += current_char
                    current_char = file.read(1)  # Read the next character
                    
                    while current_char.isdigit():
                        current_lexeme += current_char
                        current_char = file.read(1)  # Read the next character


                else:
                    print(current_char,"  ",dot_count,"  ",current_lexeme)
                        
                    current_lexeme += current_char
                    current_char = file.read(1)  # Read the next character

                    while (current_char.isdigit() or current_char == '.')  :
                        if current_char == '.':
                            if dot_count==1:
                                characters.append(current_lexeme)
                                character_count += len(current_lexeme)
                                current_lexeme = ''
                                print(current_char,"  ",dot_count,"  ",current_lexeme)
                                break
                                
                            
                            dot_count+=1
                            current_lexeme += current_char
                            current_char = file.read(1)  # Read the next character
                        else:
                            current_lexeme += current_char
                            current_char = file.read(1)  # Read the next character

                continue

            current_lexeme += current_char
            current_char = file.read(1)  # Read the next character

    if current_lexeme:
        characters.append(current_lexeme)

    return characters


filename = 'hello.txt'
lexemes = split_and_read_file(filename)
print(lexemes)