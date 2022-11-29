import sys
import ply.lex as lex

# Analizador Léxico: C#
# Grupo 1:
#   => Kevin Isaac Chevez Coronel
#   => Guillermo Alejandro Veintimilla Altamirano
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
    "break" : "BREAK",      "float": "FLOAT_TYPE",      "double": "DOUBLE_TYPE",    "int" : "INT_TYPE",
    "char" : "CHAR_TYPE",   "bool" : "BOOL_TYPE",       "string": "STRING_TYPE",    "ref" : "REF",
    #Palabras Reservadas para las funciones (para su uso en reglas semánticas)
    "Stack": "STACK",        "ToUpper":"TO_UPPER",       "Push": "PUSH",             "Add" : "ADD",
    "List":"LIST",          "Pop":"POP",                "Queue": "QUEUE"

}
# --------------------------------------------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Tokens ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
tokens = [
    # Simbolos / Caracteres Especiales
    "DOS_PUNTOS",
    "OP_TERNARIO",
    "C_IDENT_TEXTUAL",
    "C_CADENA_INTERPOLADA",
    "END_OF_LINE",
    "PAR_IZQ",
    "PAR_DER",
    "LLAVE_IZQ",
    "LLAVE_DER",
    "COR_IZQ",
    "COR_DER",
    "PUNTO",
    "COMA",
    "COMILLA_DOBLE",
    "COMILLA_SIMPLE",
    # Tipos de datos        # Grupo
    "FLOAT",                # Veintimilla
    "DOUBLE",               # Veintimilla
    "STRING",               # Chevez
    "INT",                  # Chevez
    "BOOL",                 # Reyes
    "CHAR",                 # Reyes
    #Operadores aritmenticos
    "SUMA",
    "RESTA", 
    "MULTIPLICACION", 
    "DIVISION", 
    "MODULO", 
    #Operadores logicos
    "SIMPLE_AND", 
    "SIMPLE_OR", 
    "IR", 
    "NOR", 
    "NEGACION", 
    "AND", 
    "OR", 
    #Incremento y decremento
    "INCREMENTO", 
    "DECREMENTO", 
    #Shift
    "SHIFT_MENOR", 
    "SHIFT_MAYOR", 
    #Relacional
    "IGUAL_IGUAL", 
    "NO_IGUAL", 
    "MENOR_QUE", 
    "MENOR_O_IGUAL_QUE", 
    "MAYOR_QUE", 
    "MAYOR_O_IGUAL_QUE",
    #Asignacion 
    "IGUAL", 
    "AUMENTADO", 
    "DECREMENTADO", 
    "MULTIPLICADO_POR", 
    "DIVIDIDO_POR", 
    "MODULO_DE",
    "AND_EQUAL",
    "OR_EQUAL",
    "EXC_OREQUAL",
    "RIGHTSHIFT_EQUAL",
    "LEFTSHIFT_EQUAL",
    "NULL_EQUAL",
    "LAMBDA",
    #Tokens para las funciones (para su uso en reglas semánticas)
    "CONSOLE_READLINE",
    "CONSOLE_WRITELINE",
    # IDENTIFICADOR
    "IDENTIFICADOR",
] + list(reserved.values())
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#~~~~~~~~~~~~~~~~~~ Expresiones Regulares usando funciones para tokens complejos ~~~~~~~~~~~~~~~~~~~
# -------------------------------------------- VEINTIMILLA ----------------------------------------------
def t_FLOAT(t):
  r'\d+\.(\d){1,7}(f|F){1}'
  t.value = float(t.value[:-1])
  return t

def t_DOUBLE(t):
  r'\d+\.(\d){1,15}(d|D)?'
  t.value = float(t.value[:-1])
  return t
# --------------------------------------------------------------------------------------------------

# -------------------------------------------- CHEVEZ -----------------------------------------------
def t_INT(t):
  r'\d+'
  t.value = int(t.value)    
  return t

# --------------------------------------------------------------------------------------------------

# ----------------------------------------- REYES --------------------------------------------------
def t_CONSOLE_READLINE(t):
    r"Console\.ReadLine"
    return t
def t_CONSOLE_WRITELINE(t):
    r"Console\.WriteLine"
    return t
def t_BOOL(t):
    r'(true|false)'
    t.value = True if (t.value == "true") else False
    return t
def t_CHAR(t):
    r"'[^']'"
    return t

def t_IDENTIFICADOR(t):
    r'(@)?[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, "IDENTIFICADOR")
    return t
# --------------------------------------------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#~~~~~~~~~~~~~~~~~~~~~~~ Expresiones regulares para tokens simples (Simbolos) ~~~~~~~~~~~~~~~~~~~~~~
# -------------------------------------------- CHEVEZ ----------------------------------------------
t_STRING = r'".*"'
t_COMILLA_DOBLE = r'\"'
t_COMILLA_SIMPLE = r'\''
# --------------------------------------------------------------------------------------------------

# -------------------------------------------- REYES -----------------------------------------------
t_SUMA = r"\+"
t_DOS_PUNTOS = ":"
t_AND_EQUAL= r'&='
t_OR_EQUAL=r'\|='
t_EXC_OREQUAL= r'\^='
t_NULL_EQUAL= r"\?\?="
t_LEFTSHIFT_EQUAL=r"<<="
t_RIGHTSHIFT_EQUAL=r">>="
t_LAMBDA=r"=>"
t_OP_TERNARIO=r"\?"
t_C_IDENT_TEXTUAL=r"@"
t_C_CADENA_INTERPOLADA=r"\$"
t_END_OF_LINE = r";"
t_PAR_IZQ=r"\("
t_PAR_DER=r"\)"
t_LLAVE_IZQ=r"\{"
t_LLAVE_DER=r"\}"
t_COR_IZQ=r"\["
t_COR_DER=r"\]"
t_PUNTO=r"\."
t_COMA=r","
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
  resp = ''
  for tok in lexer:
    resp+=(str(tok)+"\n")
    print(tok)
  return resp
'''
def showMenuAnalizadorLexico():
    print(
        "\nAnalizador Lexico\n"+
        " 1. Archivo de prueba Chevez\n"+
        " 2. Archivo de prueba Reyes\n"+
        " 3. Archivo de prueba Veintimilla\n"+
        " 4. Consola\n"+
        " 9. Salir"
    )
    rutaFileTest = ""
    resp_opcion = input("Digite una opcion para hacer las pruebas: ")
    if(resp_opcion == "1"):
        rutaFileTest = "G1_C#/tests/analizador_lexico/testChevez.txt"
    elif(resp_opcion == "2"):
        rutaFileTest = "G1_C#/tests/analizador_lexico/testReyes.txt"
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
    " 1. Analizador Lexico\n"+
    " 2. Analizador Sintactico\n"+
    " 3. Analizador Semantico\n"+
    " 9. Salir"
)
resp_modo = input("Digite una opción: ")
if(resp_modo == "1"):
    showMenuAnalizadorLexico()
elif(resp_modo == "2"):
    showMenuAnalizadorSintactico()
elif(resp_modo == "3"):
    showMenuAnalizadorSemantico()
else:
    print("Vuelva pronto! :)")
    sys.exit(-1)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''