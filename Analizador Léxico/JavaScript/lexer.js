const readline = require('readline');

function lexer(expression) {
    const integerPattern = /\b\d+\b/g;
    const reservedWords = /\b(if|else|for|while|def|return)\b/g;
    const symbols = /[+\-*/=><]=?/g;
    const whitespace = /\s+/g;

    let tokens = expression.split(whitespace);
    let analyzedTokens = [];

    tokens.forEach(token => {
        if (token.match(integerPattern)) { 
            analyzedTokens.push({ type: "Número entero", value: token });
        } else if (token.match(reservedWords)) { 
            analyzedTokens.push({ type: "Palabra reservada", value: token });
        } else if (token.match(symbols)) { 
            analyzedTokens.push({ type: "Símbolo", value: token });
        } else {
            analyzedTokens.push({ type: "Identificador", value: token });
        }
    });

    return analyzedTokens;
}

function main() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    console.log("Bienvenido al Analizador Léxico");

    rl.question("\nMenú:\n1. Digitar texto\n2. Salir\nSeleccione una opción: ", (opcion) => {
        if (opcion === "1") {
            rl.question("Por favor, ingrese el texto a analizar: ", (texto) => {
                let tokens = lexer(texto);

                console.log("\nResultado del análisis léxico:");
                tokens.forEach(token => {
                    console.log(`Tipo: ${token.type}, Valor: ${token.value}`);
                });

                rl.close();
            });
        } else if (opcion === "2") {
            console.log("¡Hasta luego!");
            rl.close();
        } else {
            console.log("Opción inválida. Por favor, seleccione una opción válida.");
            rl.close();
        }
    });
}

main();
