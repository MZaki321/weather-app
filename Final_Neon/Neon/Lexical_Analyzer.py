import re
import Word_Breaker

# Main code
Digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Assign_Operators = ['+=', '-=', '*=', '/=', '%=', '=']
Multiplicative_Operators = ['*', '/', '%']
Addictive_Operators = ['+', '-']
Relational_Operators = ['<', '>', '>=', '<=']
Logical_Operators = ['and', 'or', 'not']
Dot_Operator = ['.']
Punctuator = [';', ',', '\n', ':', '[', ']', '{', '}', '(', ')', '\t']
Equality_Operators = ['!=', '==']
Date_Types = ['int', 'float', 'char', 'double', 'string', 'bool']
Access_Modifiers = ['public', 'private', 'protected', 'default']
Inheritance_Related = ['virtual', 'override']
keywords = ['abstract', 'assert', 'break', 'case', 'catch', 'class', 'continue', 'const', 'do', 'else',
            'enum', 'exports', 'extend', 'final', 'finally', 'for', 'goto', 'if', 'implements', 'import', 'instanceof',
            'interface', 'module', 'native', 'new', 'package', 'requires', 'return', 'static', 'strictfp', 'super', 'switch',
            'synchronized', 'this', 'throw', 'throws', 'transient', 'try', 'var', 'void', 'volatile', 'while']
keywords.extend(Date_Types)
keywords.extend(Access_Modifiers)
keywords.extend(Inheritance_Related)




special = ['\\n', '\\t', '\\b', '\\r', '\\a', '\\f', '\\v']

# For Creating Tokens
class Token:
    Name = None
    Value = ""
    Line_no = None


def tokenizer(test_file):
    tokens = []
    line_no = 1
    string = file_read(test_file)
    words = Word_Breaker.word_break(string)

    for word in words:
        token = Token()
        if '\n' in word:
            line_no += 1
        if word[0] == '_':
            if re.fullmatch(r"(^[^\d\W]\w*\Z)", word):
                token.Name = 'ID'
                token.Value = word
                token.Line_no = line_no
                print("0 ", token.Value)
                tokens.append(token)
            else:
                token.Name = 'Invalid Lexeme'
                token.Value = word
                token.Line_no = line_no
                print("1 ", token.Value)

                tokens.append(token)

        # For Checking Alphabets
        if alphabet(word[0]):
            if re.fullmatch(r"(^[^\d\W]\w*\Z)", word):
                token.Value = word
                if belongs_to_keyword(word):
                    if word in Date_Types:
                        token.Name = 'Date Type'
                    elif word in Access_Modifiers:
                        token.Name = 'Access Modifier'
                    elif word in Inheritance_Related:
                        token.Name = 'Inheritance Operator'
                    else:
                        token.Name = 'Keyword'

                elif word in Word_Breaker.Separator:
                    if word == '\n':
                        pass
                    else:
                        if word in Assign_Operators:
                            token.Name = "Assignment Operator"
                        elif word in Multiplicative_Operators:
                            token.Name = "Multiplicative Operator"
                        elif word in Addictive_Operators:
                            token.Name = "Addictive Operator"
                        elif word in Relational_Operators:
                            token.Name = "Relational Operator"
                        elif word in Equality_Operators:
                            token.Name = "Equality Operator"
                        elif word in Logical_Operators:
                            token.Name = "Logical Operator"
                        elif word in Dot_Operator:
                            token.Name = "Dot Operator"
                        elif word in Punctuator:
                            token.Name = "Punctuator"
                        else:
                            token.Name = word

                else:
                    token.Name = 'Identifier'

                token.Line_no = line_no
                print("3 ", token.Value)
                tokens.append(token)
            else:
                token.Name = 'Invalid Lexeme'
                token.Value = word
                token.Line_no = line_no
                print("4 ", token.Value)

                tokens.append(token)

        # For Checking Separators(Operators and Punctuator)


        # For Checking Numeric Values
        if numeric(word[0]) or ((word[0] == '+' or word[0] == '-') and (word not in Word_Breaker.Separator)):
            if word.isnumeric():
                token.Name = "int"
                token.Value = word
                token.Line_no = line_no
                print("5 ", token.Value)

                tokens.append(token)
            elif re.fullmatch(r"([+|-][0-9][.][0-9]+)|([0-9][.][0-9]+)", word):
                token.Name = "float"
                token.Value = word
                token.Line_no = line_no
                # print("6 ", token.Value)

                tokens.append(token)
            else:
                token.Name = 'Invalid Lexeme'
                token.Value = word
                token.Line_no = line_no
                # print("7 ", token.Value)

                tokens.append(token)


        if word[0] in Word_Breaker.quotes:
            if re.fullmatch(r"[\w\W]*", word[1:-1]):
                if len(word) == 3 or (len(word) == 4 and word[1:-1] in special):
                    token.Name = "char"
                    token.Value = word[1:-1]
                    token.Line_no = line_no
                    # print("9 ", token.Value)

                    tokens.append(token)

                else:
                    token.Name = "string"
                    token.Value = word[1:-1]
                    token.Line_no = line_no
                    # print("10 ", token.Value)

                    tokens.append(token)

    print_result(tokens)


def alphabet(char):
    if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
        if char in Word_Breaker.Punctuator:
            return False
        return True


def numeric(char):
    if char in Digits:
        return True


def belongs_to_keyword(word):
    if word in keywords:
        return True
    return False


def file_read(file):
    with open(file, 'r') as test_file:
        data = test_file.read()
    return data


def print_result(tokens):
    for token in tokens:
        print("Line No: " + str(token.Line_no) + ", Type: " + str(token.Name) + ", Value: " + str(token.Value))