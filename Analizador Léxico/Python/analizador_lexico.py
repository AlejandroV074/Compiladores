from ply import lex
import keyword

tokens = ('IDENTIFICADOR', 'NUMERO', 'OPERADOR', 'SIMBOLO_ESPECIAL', 'CADENA',
          'COMENTARIO', 'PALABRA_RESERVADA')

t_NUMERO = r'\d+'
t_OPERADOR = r'[+\-*/=]'
t_SIMBOLO_ESPECIAL = r'[(),.:\[\]]'
t_CADENA = r'\"[^\"]*\"'
t_ignore = ' \n\r'
t_COMENTARIO = r'\#.*'


def t_error(t):
    print("Carácter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)


reserved = {word: 'PALABRA_RESERVADA' for word in keyword.kwlist}

def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFICADOR')
    return t

lexer = lex.lex()

def analizador_lexico(expression):
    lexer.input(expression)
    analyzed_tokens = []

    for tok in lexer:
        analyzed_tokens.append((tok.type, tok.value))

    return analyzed_tokens
