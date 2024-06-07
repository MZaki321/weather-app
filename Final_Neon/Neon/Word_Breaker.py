import Lexical_Analyzer

Punctuator = [';', ',', '\n', ':', '[', ']', '{', '}', '(', ')', '\t']
Operator = ['and', 'or', 'not', '*', '/', '%', '+', '-', '<', '>', '>=', '<=', '!=', '==', '.', '+=', '-=', '*=', '/=',
            '%=', '=']

Separator = []
Separator.extend(Punctuator)
Separator.extend(Operator)

dot = '.'
space = ' '
quotes = ['"', "'"]
comments = ['/*', '*/']
file = open("Test_File.txt")
result = []


def addResult(a):
    if a != '\t':
        result.append(a)


def word_break(string):
    lexeme = ''
    i = 0
    dots = 0

    while i < len(string):
        char = string[i]

        # Checking if it is a Comment
        if char == '/' and string[i + 1] == '*':
            char += string[i + 1]
            i += 1

        # Checking for the Comments
        if char in comments:
            if i == len(string):
                break
            lexeme += char
            i += 1
            char = string[i]
            while comments[1] not in lexeme:
                lexeme += char
                if i == len(string) - 1:
                    break
                i += 1
                char = string[i]
            if i == len(string):
                addResult(lexeme)
                break
            char = string[i]
            addResult(lexeme)
            lexeme = ''

        # Checking for the Quotes
        if char in quotes:
            quote_ip = char
            if char == '\n':
                break
            lexeme += char
            i += 1
            char = string[i]
            while char != quote_ip:
                if char == '\n':
                    break
                lexeme += char
                i += 1
                char = string[i]
            if char == '\n':
                addResult(lexeme)
                lexeme = ''

        # Checking for the Spaces
        if char != space:
            lexeme += char

        if i == len(string) - 1:
            if (char == space) or (char in Separator) or (lexeme in Separator):
                if lexeme != '':
                    addResult(lexeme)
                    lexeme = ''
            else:
                addResult(lexeme)
                lexeme = ''

        if i + 1 < len(string):
            next_char = string[i + 1]
            pre_char = string[i - 1]

            if (next_char == '=') and (char in Separator):
                lexeme += next_char
                i += 1

            if next_char == dot:
                dots += 1
                i += 1
                char = string[i]
                next_char = string[i + 1]

                if Lexical_Analyzer.alphabet(next_char) or len(lexeme) != 1 or next_char in Separator:
                    addResult(lexeme)
                    lexeme = ''
                if dots > 0:
                    lexeme += char
            if (string[i + 1] == space) or (string[i + 1] in Separator) or (lexeme in Separator):
                if char == '+' or char == '-':
                    if pre_char == '=' or pre_char == space or pre_char in Operator:
                        if string[i + 1] != space:
                            i = i + 1
                            char = string[i]
                            lexeme += char
                            while char not in Separator and string[i + 1] not in Separator and string[i + 1] != space:
                                i = i + 1
                                char = string[i]
                                lexeme += char
                if (lexeme != '') and (dot not in lexeme):
                    addResult(lexeme)
                    lexeme = ''

            if next_char == ';' and lexeme:
                addResult(lexeme)
                lexeme = ''
            if char == dot and len(lexeme) == 1 and Lexical_Analyzer.alphabet(next_char):
                addResult(lexeme)
                lexeme = ''
        i = i + 1
    print(result)
    return result