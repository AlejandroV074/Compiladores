from ply import lex

tokens = (
    'IDENTIFICADOR',
    'NUMERO',
    'OPERADOR',
    'SIMBOLO_ESPECIAL',
    'PALABRA_RESERVADA',
    'CADENA',
)

t_NUMERO = r'\d+'
t_OPERADOR = r'[+\-*/=]'
t_SIMBOLO_ESPECIAL = r'[(),:]'
t_CADENA = r'\"[^\"]*\"'

t_ignore = ' \t'

def t_error(t):
    print("Carácter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

reserved = {
    'print': 'PALABRA_RESERVADA',
    'if': 'PALABRA_RESERVADA',
    'else': 'PALABRA_RESERVADA',
    'while': 'PALABRA_RESERVADA',
    'for': 'PALABRA_RESERVADA',
    'class': 'PALABRA_RESERVADA',
    'int': 'PALABRA_RESERVADA',
    'try': 'PALABRA_RESERVADA',
    'except': 'PALABRA_RESERVADA',
    'None': 'PALABRA_RESERVADA',
    'and': 'PALABRA_RESERVADA',
    'or': 'PALABRA_RESERVADA',
    'import': 'PALABRA_RESERVADA',
    'as': 'PALABRA_RESERVADA',
    'def': 'PALABRA_RESERVADA',
    'return': 'PALABRA_RESERVADA',
}

tokens += tuple(reserved.values())

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

def main():
    print("Bienvenido al Analizador Léxico")
    while True:
        print("\nMenú:")
        print("1. Digitar texto")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            texto = input("Por favor, ingrese el texto a analizar: ")
            tokens = analizador_lexico(texto)
            print("\nSeparación de tokens:")
            for token_type, token_value in tokens:
                print(f"{token_type}: {token_value}")
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
