import ply.yacc as yacc
from lexico import tokens

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Cuerpo sintáctico ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def p_body(p):
  '''body : asignacion END_OF_LINE
  | comparacion
  | estructura_control
  | estructura_datos
  | expresion
  | salida_entrada
  | funcion
  | declaracion END_OF_LINE
  | empty
  '''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Terminales ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def p_valor(p):
  '''valor : CHAR
  | numero
  | BOOL
  | STRING
  | IDENTIFICADOR
  '''

def p_numero(p):
  '''numero : FLOAT
  | DOUBLE
  | INT
  '''

def p_valor_tipo(p):
  '''valor_tipo : CHAR_TYPE
  | FLOAT_TYPE
  | DOUBLE_TYPE
  | INT_TYPE
  | BOOL_TYPE
  | STRING_TYPE
  | VOID
  '''

def p_modificador_acceso(p):
  '''modificador_acceso : PRIVATE
  | PROTECTED
  | PUBLIC
  '''

def p_operador_realacional(p):
  '''operador_realacional : IGUAL_IGUAL
  | NO_IGUAL 
  | MENOR_QUE
  | MENOR_O_IGUAL_QUE
  | MAYOR_QUE
  | MAYOR_O_IGUAL_QUE
  '''

def p_operador_aritmentico(p):
  '''operador_aritmentico : SUMA
  | RESTA
  | MULTIPLICACION
  | DIVISION
  | MODULO
  '''

def p_operador_condicional(p):
  '''operador_condicional : IGUAL_IGUAL
  | NO_IGUAL
  | MENOR_QUE
  | MENOR_O_IGUAL_QUE
  | MAYOR_QUE
  | MAYOR_O_IGUAL_QUE
  '''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Formas de asignación ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# -------------------------------------------- REYES -----------------------------------------------

def p_empty(p):
  'empty : END_OF_LINE'

def p_asignacion(p):
  '''asignacion : asignacionSimple
   '''
def p_asignacionSimple(p):
  '''asignacionSimple : IDENTIFICADOR IGUAL valor
                      | IDENTIFICADOR IGUAL expresion
  '''

def p_declaracion(p):
  'declaracion : valor_tipo IDENTIFICADOR'

def p_declaracionAsignacion(p):
  ''' declaracion : valor_tipo asignacion

  '''

'''
Declaración a preguntar en un futuro:

def p_declaracion(p):
  'declaracion : valor_tipo declaracionComponente'
  
def p_declaracionComponente(p):
  declaracionComponente : IDENTIFICADOR
                           | IDENTIFICADOR COMA declaracionComponente
                           | asignacionSimple
                           | asignacionSimple COMA declaracionComponente
'''

# --------------------------------------------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Comparaciones ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# -------------------------------------------- CHEVEZ ----------------------------------------------
def p_comparacion(p):
  'comparacion : valor operador_realacional valor'
# --------------------------------------------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Estructuras de control ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def p_estructura_control(p):
  '''estructura_control : while
  | switch_case
  | for
  '''

# -------------------------------------------- REYES -----------------------------------------------
def p_while(p):
  'while : IGUAL'
# --------------------------------------------------------------------------------------------------




# -------------------------------------------- CHEVEZ ----------------------------------------------
def p_switch_case(p):
  'switch_case : IGUAL'
# --------------------------------------------------------------------------------------------------




# ----------------------------------------- VEINTIMILLA --------------------------------------------
def p_for(p):
  'for : IGUAL'
# --------------------------------------------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Estructuras de datos ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def p_estructura_datos(p):
  'estructura_datos : IGUAL'
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Tipos de expresiones ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# -------------------------------------------- CHEVEZ ----------------------------------------------
def p_expresion(p):
  '''expresion : expresion_operacion_aritmetica
  | expresion_condicional
  '''

def p_expresion_operacion_aritmetica(p):
  '''expresion_operacion_aritmetica : numero operador_aritmentico numero
  | IDENTIFICADOR operador_aritmentico IDENTIFICADOR
  '''

def p_expresion_condicional(p):
  '''expresion_condicional : numero operador_condicional numero
  | IDENTIFICADOR operador_condicional IDENTIFICADOR
  '''
# --------------------------------------------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Imprimir e ingresar datos por teclado ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ----------------------------------------- VEINTIMILLA --------------------------------------------
def p_salida_entrada(p):
  'salida_entrada : IGUAL'
# --------------------------------------------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Tipos de definición de funciones ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def p_funcion(p):
  'funcion : IGUAL'
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




# Regla de error para errores en la sintaxis
def p_error(p):
  if p:
    print(f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}")
    parser.errok()
  else:
    print("Error de sintaxis Fin de Linea")
 
# Build the parser
parser = yacc.yacc()

def validaRegla(s):
  result = parser.parse(s)
  print(result)

while True:
  try:
    s = input('calc > ')
  except EOFError:
    break
  if not s: continue
  validaRegla(s)