import ply.yacc as yacc
from analizador_lexico import tokens

def p_program(p):
    '''program : statements'''
    p[0] = p[1]

def p_statements(p):
    '''statements : statement
                  | statements statement'''
    if len(p) > 2:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''statement : function_definition
                 | assignment
                 | if_statement
                 | expression_statement
                 | print_statement'''

def p_function_definition(p):
    '''function_definition : PALABRA_RESERVADA IDENTIFICADOR SIMBOLO_ESPECIAL '(' parameters ')' SIMBOLO_ESPECIAL ':' statements
                           | PALABRA_RESERVADA IDENTIFICADOR SIMBOLO_ESPECIAL '(' ')' SIMBOLO_ESPECIAL ':' statements'''

def p_parameters(p):
    '''parameters : IDENTIFICADOR
                  | IDENTIFICADOR SIMBOLO_ESPECIAL ',' parameters'''

def p_assignment(p):
    '''assignment : IDENTIFICADOR OPERADOR expression'''

def p_if_statement(p):
    '''if_statement : PALABRA_RESERVADA expression SIMBOLO_ESPECIAL ':' statements
                    | PALABRA_RESERVADA expression SIMBOLO_ESPECIAL ':' statements else_block'''

def p_else_block(p):
    '''else_block : PALABRA_RESERVADA ':' statements'''

def p_expression_statement(p):
    '''expression_statement : expression'''

def p_expression(p):
    '''expression : expression OPERADOR expression
                  | NUMERO
                  | IDENTIFICADOR
                  | IDENTIFICADOR SIMBOLO_ESPECIAL '(' parameters ')' '''

def p_print_statement(p):
    '''print_statement : PALABRA_RESERVADA SIMBOLO_ESPECIAL '(' expression ')' '''

def p_error(p):
    if p:
        print("Error sintáctico en '%s'" % p.value)
    else:
        print("Error sintáctico: Token inesperado al final del archivo")

parser = yacc.yacc()
