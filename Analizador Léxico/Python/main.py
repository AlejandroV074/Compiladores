import shlex

def lexer(expression):
    lexer = shlex.shlex(expression)
    lexer.wordchars += '.,-=' 
    lexer.quotes = '' 
    lexer.whitespace_split = True  
    tokens = list(lexer)
    analyzed_tokens = []

    for token in tokens:
        if token.isdigit(): 
            analyzed_tokens.append(("Número entero", token))
        elif token in ['if', 'else', 'for', 'while', 'def', 'return']:  
            analyzed_tokens.append(("Palabra reservada", token))
        elif token in ['+', '-', '*', '/', '=', '==', '!=', '>', '<', '>=', '<=']:  
            analyzed_tokens.append(("Símbolo", token))
        else:
            analyzed_tokens.append(("Identificador", token)) 

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
            tokens = lexer(texto)
            print("\nResultado del análisis léxico:")
            for token_type, token_value in tokens:
                print(f"Tipo: {token_type}, Valor: {token_value}")
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
