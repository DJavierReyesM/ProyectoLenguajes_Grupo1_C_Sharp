import sys
import ply.lex as lex

# Analizador Léxico: C#
# Grupo 1:
#   => Kevin Isaac Chevez Coronel
#   => Guillermo Alejandro Veintimiila Altamirano
#   => Diego Javier Reyes Medranda

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Palabras reservadas ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# -------------------------------------------- CHEVEZ ----------------------------------------------
reserved = {
    "default": "DEFAULT",   "null": "NULL",             "where": "WHERE",           "byte": "BYTE",
    "class": "CLASS",       "new": "NEW",               "struct": "STRUCT",         "case": "CASE",
    "const": "CONST",       "do": "DO",                 "NULL": "NULL_VAL",         "switch": "SWITCH",
    "typeof": "TYPEOF",     "while": "WHILE",           "continue": "CONTINUE",     "else": "ELSE",
    "finally": "FINALLY",   "for": "FOR",               "in": "IN",                 "object": "OBJECT",
    "private": "PRIVATE",   "protected": "PROTECTED",   "public": "PUBLIC",         "return": "RETURN",
    "this": "THIS",         "void": "VOID",             "global": "GLOBAL",         "let": "LET",
    "on": "ON",             "orderby": "ORDERBY",       "var": "VAR",               "when": "WHEN",
}
# --------------------------------------------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Tokens ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
tokens = [
    # Simbolos
    "DOS_PUNTOS",

    # Tipos de datos        # Grupo
    "FLOAT",                # Veintimilla
    "DOUBLE",               # Veintimilla
    "STRING",               # Chevez
    "INT",                  # Chevez

    #Operadores aritmenticos
    "SUMA",
    "RESTA", 
    "MULTIPLICACION", 
    "DIVISION", 
    "MODULO", 
    "SIMPLE_AND", 
    "SIMPLE_OR", 
    "IR", 
    "NOR", 
    "NEGACION", 
    "AND", 
    "OR", 
    "INCREMENTO", 
    "DECREMENTO", 
    "SHIFT_MENOR", 
    "SHIFT_MAYOR", 
    "IGUAL_IGUAL", 
    "NO_IGUAL", 
    "MENOR_QUE", 
    "MENOR_O_IGUAL_QUE", 
    "MAYOR_QUE", 
    "MAYOR_O_IGUAL_QUE", 
    "IGUAL", "AUMENTADO", 
    "DECREMENTADO", 
    "MULTIPLICADO_POR", 
    "DIVIDIDO_POR", 
    "MODULO_DE",
    "IDENTIFICADOR",

] + list(reserved.values())
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#~~~~~~~~~~~~~~~~~~ Expresiones Regulares usando funciones para tokens complejos ~~~~~~~~~~~~~~~~~~~
# -------------------------------------------- VEINTIMILLA ----------------------------------------------
def t_FLOAT(t):
  r'\d+\.(\d){1,7}(f|F){1}'
  t.value = reserved.get(t.value, "FLOAT")
  return t

def t_DOUBLE(t):
  r'\d+\.(\d){1,15}(d|D)?'
  t.value = reserved.get(t.value, "DOUBLE")
  return t
# --------------------------------------------------------------------------------------------------

# -------------------------------------------- CHEVEZ -----------------------------------------------
def t_INT(t):             
  r'\d+'
  t.value = int(t.value)    
  return t

# --------------------------------------------------------------------------------------------------

# ----------------------------------------- REYES --------------------------------------------
def t_IDENTIFICADOR(t):
    r'(@)?[a-zA-Z_][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, "IDENTIFICADOR")
    return t
# --------------------------------------------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#~~~~~~~~~~~~~~~~~~~~~~~ Expresiones regulares para tokens simples (Simbolos) ~~~~~~~~~~~~~~~~~~~~~~
# -------------------------------------------- CHEVEZ ----------------------------------------------
t_STRING = r'".*"'

# --------------------------------------------------------------------------------------------------

# -------------------------------------------- REYES -----------------------------------------------
t_SUMA = r"\+"
t_DOS_PUNTOS = ":"

# --------------------------------------------------------------------------------------------------

# ----------------------------------------- VEINTIMILLA --------------------------------------------
t_RESTA = r'\-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_MODULO = r'\%'
t_SIMPLE_AND = r'&'
t_SIMPLE_OR = r'\|'
t_IR = r'\^'
t_NOR = r'\!'
t_NEGACION = r'\~'
t_AND = r'&&'
t_OR = r'\|\|'
t_INCREMENTO = r'\+\+'
t_DECREMENTO = r'\-\-'
t_SHIFT_MENOR = r'<<'
t_SHIFT_MAYOR = r'>>'
t_IGUAL_IGUAL = r'=='
t_NO_IGUAL = r'\!\='
t_MENOR_QUE = r'<'
t_MENOR_O_IGUAL_QUE = r'<='
t_MAYOR_QUE = r'>'
t_MAYOR_O_IGUAL_QUE = r'>='
t_IGUAL = r'='
t_AUMENTADO = r'\+='
t_DECREMENTADO = r'\-='
t_MULTIPLICADO_POR = r'\*='
t_DIVIDIDO_POR = r'/='
t_MODULO_DE = r'\%='
# --------------------------------------------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Conteo de Lineas ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def t_newline(t):
    r"\n+"
    t.lexer.lineno += t.value.count("\n")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Token de "ignorar" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
t_ignore = " \t"
t_ignore_SingleLineComments = r"//.*"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TokeN de error ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def t_error(t):
    print("Caracter no permitido: '%s'" % t.value[0])
    t.lexer.skip(1)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PROGRAMA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
lexer = lex.lex()
def getTokens(lexer):
  tokens = []
  for tok in lexer:
    tokens.append(tok)
    print(tok)
  return tokens

def showMenuAnalizadorLexico():
    print(
        "\nAnalizador Lexico\n"+
        "Digite una opcion para hacer las pruebas\n"+
        "\t1. Archivo de prueba Chevez\n"+
        "\t2. Archivo de prueba Reyes\n"+
        "\t3. Archivo de prueba Veintimilla\n"+
        "\t4. Consola\n"+
        "\t9. Salir"
    )
    rutaFileTest = ""
    resp_opcion = input(" >> ")
    if(resp_opcion == "1"):
        rutaFileTest = "./tests/analizador_lexico/testChevez.txt"
    elif(resp_opcion == "2"):
        rutaFileTest = "./tests/analizador_lexico/testReyes.txt"
    elif(resp_opcion == "3"):
        rutaFileTest = "G1_C#/tests/analizador_lexico/testVeintimilla.txt"
    elif(resp_opcion == "4"):
        rutaFileTest = "consola"
    else:
        print("Vuelva pronto! :)")
        sys.exit(-1)

    if(rutaFileTest == "consola"):
        linea=" "
        print("\nIngrese los valores a probar por consola. (ctrl+c pasa salir)")
        while linea!="":
            linea=input(">> ")
            lexer.input(linea)
            getTokens(lexer)
    elif(rutaFileTest != ""):
        file = open(rutaFileTest)
        cadena = file.read()
        file.close()
        lexer.input(cadena)
        getTokens(lexer)

def showMenuAnalizadorSintactico():
    print("Opps, no tenemos esa funcionalidad aún, intentelo luego. ;)")
    sys.exit(-1)

def showMenuAnalizadorSemantico():
    print("Opps, no tenemos esa funcionalidad aún, intentelo luego. ;)")
    sys.exit(-1)

#Main Ejecutable
print(
    "\nProyecto Analizador lexico, sintactico y semantico en C#\n"+
    "Grupo 1 - Pruebas\n"+
    "Digite una opción:\n"+
    "\t1. Analizador Lexico\n"+
    "\t2. Analizador Sintactico\n"+
    "\t3. Analizador Semantico\n"+
    "\t9. Salir"
)
resp_modo = input(" >> ")
if(resp_modo == "1"):
    showMenuAnalizadorLexico()
elif(resp_modo == "2"):
    showMenuAnalizadorSintactico()
elif(resp_modo == "3"):
    showMenuAnalizadorSemantico()
else:
    print("Vuelva pronto! :)")
    sys.exit(-1)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
