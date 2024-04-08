from analizador_lexico import analizador_lexico
from analizador_sintactico import parser as analizador_sintactico

def main():
    archivo = "texto.txt"
    try:
        with open(archivo, "r") as file:
            texto = file.read()
            print("Análisis léxico:")
            tokens = analizador_lexico(texto)
            for token in tokens:
                if len(token) == 2:
                    token_type, token_value = token
                    print(f"{token_type}: {token_value}")
                else:
                    print(f"Token no válido: {token}")

            print("\nAnálisis sintáctico:")
            tokens_values = [token[1] for token in tokens]
            analizador_sintactico.parse(' '.join(tokens_values))
    except FileNotFoundError:
        print("Archivo no encontrado, asegúrese de que exista un archivo llamado texto.txt")

if __name__ == "__main__":
    main()
