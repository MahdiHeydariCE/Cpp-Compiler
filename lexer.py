lexemeBegin = 0
forward = 0
round = 0
keyword = [
    'main',
    'id',
    'num',
    'string',
    'character',
    'int',
    'char',
    'float',
    'double', 
    'void',
    'cin',
    'cout',
    'while',
    'for',
    'if',
    'else',
    'break',
    'return',
]
with open("code.cpp", "r") as f:
    code = f.read() + '$'


def get_next_token():
    global lexemeBegin, forward, round
    if code[forward] == '$':
        return '$'
    if round > 0:
        state = 0
        forward += 1
        lexemeBegin = forward
    elif round == 0:
        state = 0
        forward = 0
        lexemeBegin = forward
        round += 1    
    while True:
        c = code[forward]
        if state == 0:
            if c.isalpha():
                forward += 1
                state = 1
            elif c.isdigit():
                forward += 1
                state = 3
            elif c == '<':
                forward += 1
                state = 12
            elif c == '>':
                forward += 1
                state = 18
            elif c == '=':
                forward += 1
                state = 24
            elif c == '!':
                forward += 1
                state = 27
            elif c == '|':
                forward += 1
                state = 29
            elif c == '&':
                forward +=1
                state = 31
            elif c == '~':
                state = 33
            elif c == '*':
                state = 34
            elif c == '+':
                forward += 1
                state = 35
            elif c == '-':
                forward += 1
                state = 39
            elif c == '/':
                state = 43
            elif c == '%':
                state = 44
            elif c == '^':
                state = 45
            elif c == '[':
                state = 46
            elif c == ']':
                state = 47
            elif c == '{':
                state = 48
            elif c == '}':
                state = 49
            elif c == '(':
                state = 50
            elif c == ')':
                state = 51
            elif c == ',':
                state = 52
            elif c == ';':
                state = 53
            elif c == '"':
                forward += 1
                state = 54
            elif c == ' ' or c == '\r' or c == '\n' or c == '\t':
                forward += 1
                lexemeBegin = forward
            elif c == '$':
                state = 56
            else:
                raise ValueError
        elif state == 1:
            if c.isalpha() or c.isdigit():
                forward += 1
            else:
                state = 2
        elif state == 2:
            forward -= 1
            word = code[lexemeBegin:forward+1]
            if word in keyword:
                return word
            return 'id'
        elif state == 3:
            if c.isdigit():
                forward += 1
            elif code[forward] == '.':
                forward += 1
                state = 4
            elif code[forward] == 'E' or code[forward] == 'e':
                forward += 1
                state = 6
            else:
                state = 10
        elif state == 4:
            if c.isdigit():
                forward += 1
                state = 5
            else:
                raise ValueError
        elif state == 5:
            if c.isdigit():
                forward += 1
            elif code[forward] == 'E' or code[forward] == 'e':
                forward += 1
                state = 6
            else:
                state = 11
        elif state == 6:
            if code[forward] == '+' or code[forward] == '-':
                forward += 1
                state = 7
            elif c.isdigit():
                forward += 1
                state = 8
            else:
                raise ValueError
        elif state == 7:
            if c.isdigit():
                forward += 1
                state = 8
            else:
                raise ValueError
        elif state == 8:
            if c.isdigit():
                forward += 1
            else:
                state == 9
        elif state == 9:
            forward -= 1
            return 'num'
        elif state == 10:
            forward -= 1
            return 'num'
        elif state == 11:
            forward -= 1
            return 'num'
        elif state == 12:
            if c == '<':
                forward += 1
                state = 13
            elif c == '=':
                state = 15
            else:
                state = 17
        elif state == 13:
            if c == '<':
                state = 14
            else:
                state = 16
        elif state == 14:
            return '<<<'
        elif state == 15:
            return '<='
        elif state == 16:
            forward -= 1
            return '<<'
        elif state == 17:
            forward -= 1
            return '<'
        elif state == 18:
            if c == '>':
                forward += 1
                state = 19
            elif c == '=':
                state = 21
            else:
                state = 23
        elif state == 19:
            if c == '>':
                state = 20
            else:
                state = 22
        elif state == 20:
            return '>>>'
        elif state == 21:
            return '>='
        elif state == 22:
            forward -= 1
            return '>>'
        elif state == 23:
            forward -= 1
            return '>'
        elif state == 24:
            if c == '=':
                state = 25
            else:
                state = 26
        elif state == 25:
            return '=='
        elif state == 26:
            forward -= 1
            return '='
        elif state == 27:
            if c == '=':
                state = 28
            else:
                raise ValueError
        elif state == 28:
            return '!='
        elif state == 29:
            if c == '|':
                state = 30
            else:
                raise ValueError
        elif state == 30:
            return '||'
        elif state == 31:
            if c == '&':
                state = 32
            else:
                raise ValueError
        elif state == 32:
            return '&&'
        elif state == 33:
            return '~'
        elif state == 34:
            return '*'
        elif state == 35:
            if c == '+':
                state = 36
            elif c == '=':
                state = 37
            else:
                state = 38
        elif state == 36:
            return '++'
        elif state == 37:
            return '+='
        elif state == 38:
            forward -= 1
            return '+'
        elif state == 39:
            if c == '-':
                state = 40
            elif c == '=':
                state = 41
            else:
                state = 42
        elif state == 40:
            return '--'
        elif state == 41:
            return '-='
        elif state == 42:
            forward -= 1
            return '-'
        elif state == 43:
            return '/'
        elif state == 44:
            return '%'
        elif state == 45:
            return '^'
        elif state == 46:
            return '['
        elif state == 47:
            return ']' 
        elif state == 48:
            return '{'
        elif state == 49:
            return '}'
        elif state == 50:
            return '('
        elif state == 51:
            return ')'
        elif state == 52:
            return ','
        elif state == 53:
            return ';'
        elif state == 54:
            if code[forward] == '"':
                state = 55
            else:
                forward += 1
        elif state == 55:
            return 'string'
        elif state == 56:
            return '$'
