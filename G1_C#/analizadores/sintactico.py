import sys
import ply.yacc as yacc
from analizadores.lexico import tokens

# String de errores
errores_sintactico = []

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Cuerpo sintáctico ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def p_body(p):
  '''body : asignacion END_OF_LINE
  | comparacion
  | estructura_control
  | estructura_datos
  | expresion END_OF_LINE
  | salida_entrada END_OF_LINE
  | funcion
  | declaracion END_OF_LINE
  | empty
  | funciones_estructura_datos_lista END_OF_LINE
  | funciones_estructura_datos END_OF_LINE
  | lambda_exp
  | body body
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
def p_ftipo(p):
    '''ftipo : valor_tipo
                   | VOID
    '''

def p_valor_tipo(p):
  '''valor_tipo : CHAR_TYPE
  | FLOAT_TYPE
  | DOUBLE_TYPE
  | INT_TYPE
  | BOOL_TYPE
  | STRING_TYPE
  '''

def p_valor_tipo_inicializador(p):
    '''valor_tipo_inicializador : FLOAT_TYPE
    | DOUBLE_TYPE
    | STRING_TYPE
    | INT_TYPE
    | BOOL_TYPE
    | CHAR_TYPE
    | IDENTIFICADOR'''

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

def p_operacion_string(p):
    '''operacion_string : STRING SUMA STRING
    | STRING SUMA IDENTIFICADOR
    | IDENTIFICADOR SUMA STRING
    | IDENTIFICADOR SUMA IDENTIFICADOR'''

def p_termino(p):
  '''termino : termino operador_aritmentico factor
    | factor
  '''

def p_factor(p):
  '''factor : numero
    | PAR_IZQ expresion_operacion_aritmetica PAR_DER
  '''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Formas de asignación ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# -------------------------------------------- REYES -----------------------------------------------

def p_empty(p):
  'empty : END_OF_LINE'

def p_asignacion(p):
  '''asignacion : asignacionSimple
                | asignacionCompuesta
                | asignacionClase
                | asignacionEstructuraD
                | asignacionNull
                | asignacionIndex
                | asignacionRef
   '''
def p_asignacionSimple(p):
  '''asignacionSimple : IDENTIFICADOR IGUAL valor
                      | IDENTIFICADOR IGUAL expresion
                      | IDENTIFICADOR IGUAL salida_tres
                      | IDENTIFICADOR IGUAL index
  '''
def p_asignacionNull(p):
    'asignacionNull : IDENTIFICADOR IGUAL NULL'

def p_asignacionClase(p):
    '''asignacionClase : IDENTIFICADOR IGUAL NEW IDENTIFICADOR PAR_IZQ PAR_DER'''


def p_asignacionEstructuraD(p):
    '''asignacionEstructuraD : IDENTIFICADOR IGUAL asignacionPila
                            | IDENTIFICADOR IGUAL asignacionQueue
                            | IDENTIFICADOR IGUAL asignacionList
    '''

def p_asignacionPila(p):
    'asignacionPila : NEW STACK tipoLista PAR_IZQ PAR_DER'

def p_asignacionQueue(p):
    'asignacionQueue : NEW QUEUE tipoLista PAR_IZQ PAR_DER'

def p_asignacionList(p):
    'asignacionList : NEW LIST tipoLista PAR_IZQ PAR_DER'

def p_asignacionIndex(p):
    '''asignacionIndex : index IGUAL index
                       | index IGUAL valor
    '''

def p_index(p):
    '''index : IDENTIFICADOR COR_IZQ INT COR_DER
            | IDENTIFICADOR COR_IZQ IDENTIFICADOR COR_DER
    '''

def p_asignacionRef(p):
    '''asignacionRef : IDENTIFICADOR IGUAL REF IDENTIFICADOR
                    | IDENTIFICADOR IGUAL REF index
    '''

def p_asignacionCompuesta(p):
  '''asignacionCompuesta : asignacionCompuesta_Logic
                        | asignacionCompuesta_Number
                        | asignacionCompuesta_Null
                        | asignacionCompuesta_Shift
  '''
def p_asignacionCompuesta_Logic(p):
  '''asignacionCompuesta_Logic : IDENTIFICADOR operadoresCompuestosLogic BOOL
                               | IDENTIFICADOR operadoresCompuestosLogic expresion_condicional
                               | IDENTIFICADOR operadoresCompuestosLogic IDENTIFICADOR
                               | IDENTIFICADOR operadoresCompuestosLogic INT
  '''

def p_asignacionCompuesta_Number(p):
  '''asignacionCompuesta_Number : IDENTIFICADOR operadoresCompuestosNumber numero
                                | IDENTIFICADOR operadoresCompuestosNumber expresion_operacion_aritmetica
                                | IDENTIFICADOR operadoresCompuestosNumber IDENTIFICADOR
  '''

def p_asignacionCompuesta_Null(p):
    '''asignacionCompuesta_Null : IDENTIFICADOR NULL_EQUAL valor
                                | IDENTIFICADOR NULL_EQUAL expresion
                                | IDENTIFICADOR NULL_EQUAL asignacionPila
                                | IDENTIFICADOR NULL_EQUAL asignacionQueue
                                | IDENTIFICADOR NULL_EQUAL asignacionList'''

def p_asignacionCompuesta_Shift(p):
    '''asignacionCompuesta_Shift : IDENTIFICADOR operadoresCompuestosShift IDENTIFICADOR
                                | IDENTIFICADOR operadoresCompuestosShift INT
    '''

def p_operadoresCompuestosNumber(p):
  ''' operadoresCompuestosNumber : AUMENTADO
                          | DECREMENTADO
                          | MULTIPLICADO_POR
                          | DIVIDIDO_POR
                          | MODULO_DE
  '''
def p_operadoresCompuestosLogic(p):
  ''' operadoresCompuestosLogic : AND_EQUAL
                                | OR_EQUAL
                                | EXC_OREQUAL
  '''

def p_operadoresCompuestosShift(p):
    '''operadoresCompuestosShift : LEFTSHIFT_EQUAL
                                | RIGHTSHIFT_EQUAL
    '''

def p_declaracion(p):
  '''declaracion : valor_tipo IDENTIFICADOR
                 | declaracionEstructuraD
                 | declaracionAsignacion
                 | declaracionClase
                 | declaracionNull
  '''

def p_declaracionNull(p):
    'declaracionNull : valor_tipo OP_TERNARIO IDENTIFICADOR'

def p_declaracionClase(p):
    'declaracionClase : IDENTIFICADOR IDENTIFICADOR'

def p_declaracionAsignacion(p):
  ''' declaracionAsignacion : valor_tipo asignacionSimple
                            | declaracionClase IGUAL NEW IDENTIFICADOR PAR_IZQ PAR_DER
                            | declaracionClase IGUAL NULL
                            | declaracionClase IGUAL IDENTIFICADOR
                            | declaracionNull IGUAL valor
                            | declaracionNull IGUAL expresion
                            | declaracionNull IGUAL NULL
                            | declaracionEstructuraD IGUAL NULL
                            | REF valor_tipo asignacionRef
                            | REF IDENTIFICADOR asignacionRef
                            | REF declaracionEstructuraD asignacionRef

  '''
def p_declaracionEstructuraD(p):
    '''declaracionEstructuraD : declaracionList
                              | declaracionQueue
                              | declaracionPila
    '''

def p_declaracionList(p):
    'declaracionList : LIST tipoLista IDENTIFICADOR'

def p_declaracionQueue(p):
    'declaracionQueue : QUEUE tipoLista IDENTIFICADOR'

def p_declaracionPila(p):
    'declaracionPila : STACK MENOR_QUE valor_tipo_inicializador MAYOR_QUE IDENTIFICADOR'

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
  '''while : while_normal
           | while_do
  '''

def p_while_normal(p):
    '''while_normal : WHILE PAR_IZQ expresion_condicional PAR_DER LLAVE_IZQ body_while LLAVE_DER'''

def p_while_do(p):
    '''while_do : DO LLAVE_IZQ body_while LLAVE_DER WHILE PAR_IZQ expresion_condicional PAR_DER END_OF_LINE'''

def p_body_while(p):
    '''body_while : asignacion END_OF_LINE
                  | declaracion END_OF_LINE
                  | salida_entrada END_OF_LINE
                  | BREAK END_OF_LINE
                  | CONTINUE END_OF_LINE
                  | asignacion END_OF_LINE body_while
                  | declaracion END_OF_LINE body_while
                  | salida_entrada END_OF_LINE body_while
                  | BREAK END_OF_LINE body_while
                  | CONTINUE END_OF_LINE body_while

    '''
# --------------------------------------------------------------------------------------------------




# -------------------------------------------- CHEVEZ ----------------------------------------------
def p_switch_case(p):
  'switch_case : SWITCH PAR_IZQ valor PAR_DER LLAVE_IZQ casos LLAVE_DER'

def p_casos(p):
  '''casos : CASE valor DOS_PUNTOS body_case BREAK END_OF_LINE
  | CASE valor DOS_PUNTOS BREAK END_OF_LINE
  | CASE valor DOS_PUNTOS body_case BREAK END_OF_LINE casos
  | CASE valor DOS_PUNTOS BREAK END_OF_LINE casos
  '''
def p_body_case(p):
  '''body_case : asignacion END_OF_LINE
  | declaracion END_OF_LINE
  | comparacion END_OF_LINE
  | salida_entrada END_OF_LINE
  | asignacion END_OF_LINE body_case
  | declaracion END_OF_LINE body_case
  | salida_entrada END_OF_LINE body_case
  | comparacion END_OF_LINE body_case
  '''
# --------------------------------------------------------------------------------------------------




# ----------------------------------------- VEINTIMILLA --------------------------------------------
# ----------------------------------------------Estructura de control For --------------------------------------------------------- # 
def p_for(p):
    'for : FOR PAR_IZQ forInicializador END_OF_LINE forCondicion END_OF_LINE forIterador PAR_DER LLAVE_IZQ body LLAVE_DER'


# Seccion iterador

def p_forIterador(p):
    'forIterador : IDENTIFICADOR operadorForIteracion'


def p_operadorForIteracion(p):
    '''operadorForIteracion : INCREMENTO 
                            | DECREMENTO'''

# ------------------------------------------- #
# Seccion condicion

def p_forCondicion(p):
    'forCondicion : IDENTIFICADOR operador_condicional valorForCondicion'


def p_valorForCondicion(p):
    '''valorForCondicion : FLOAT
            | DOUBLE
            | INT
            | IDENTIFICADOR'''

# ------------------------------------------- #
# Seccion inicializador

def p_forInicializador(p):
    '''forInicializador : tipoDatoForInicializador IDENTIFICADOR IGUAL valorForInicializador
                    | IDENTIFICADOR IGUAL valorForInicializador'''



def p_tipoDatoForInicializador(p):
    '''tipoDatoForInicializador : FLOAT_TYPE
                        | DOUBLE_TYPE
                        | INT_TYPE'''


def p_valorForInicializador(p):
    '''valorForInicializador : FLOAT
            | DOUBLE
            | INT
            | IDENTIFICADOR'''
    
# ------------------------------------------- #
# ---------------------------------------------- Fin Estructura de control For --------------------------------------------------------- # 
# --------------------------------------------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Estructuras de datos ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def p_estructura_datos(p):
  '''estructura_datos : lista
                      | pila
  '''
# ----------------------------------------- VEINTIMILLA --------------------------------------------
def p_lista(p):
    'lista : LIST tipoLista IDENTIFICADOR IGUAL NEW LIST tipoLista PAR_IZQ PAR_DER END_OF_LINE'

def p_tipoLista(p):
    'tipoLista : MENOR_QUE valor_tipo_inicializador MAYOR_QUE'

def p_funciones_estructura_datos_lista(p):
  'funciones_estructura_datos_lista : add_lista'

def p_add_lista(p):
  'add_lista : IDENTIFICADOR PUNTO ADD PAR_IZQ valor PAR_DER'

# --------------------------------------------------------------------------------------------------
# ----------------------------------------- REYES --------------------------------------------
def p_pila(p):
    'pila : STACK MENOR_QUE valor_tipo_inicializador MAYOR_QUE IDENTIFICADOR IGUAL NEW STACK MENOR_QUE valor_tipo_inicializador MAYOR_QUE PAR_IZQ PAR_DER END_OF_LINE'

def p_funciones_estructura_datos(p):
    '''funciones_estructura_datos : stack_push
                                  | stack_pop
    '''

def p_stack_push(p):
    '''stack_push : IDENTIFICADOR PUNTO PUSH PAR_IZQ valor PAR_DER
                  | IDENTIFICADOR PUNTO PUSH PAR_IZQ NEW IDENTIFICADOR PAR_IZQ PAR_DER PAR_DER
    '''

def p_stack_pop(p):
    '''stack_pop : IDENTIFICADOR PUNTO POP PAR_IZQ PAR_DER'''
# --------------------------------------------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Tipos de expresiones ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# -------------------------------------------- CHEVEZ ----------------------------------------------
def p_expresion(p):
  '''expresion : expresion_operacion_aritmetica
  | expresion_condicional
  '''

def p_expresion_operacion_aritmetica(p):
  '''expresion_operacion_aritmetica : expresion_operacion_aritmetica operador_aritmentico termino
  | numero operador_aritmentico expresion_operacion_aritmetica
  | numero operador_aritmentico numero
  | numero operador_aritmentico IDENTIFICADOR
  | IDENTIFICADOR operador_aritmentico numero
  | IDENTIFICADOR operador_aritmentico IDENTIFICADOR
  | termino
  '''

def p_expresion_condicional(p):
  '''expresion_condicional : numero operador_condicional numero
  | IDENTIFICADOR operador_condicional IDENTIFICADOR
  | IDENTIFICADOR operador_condicional numero
  | numero operador_condicional IDENTIFICADOR
  '''
# --------------------------------------------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Imprimir e ingresar datos por teclado ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ----------------------------------------- VEINTIMILLA --------------------------------------------
def p_salida_entrada(p):
  '''salida_entrada : salida_uno
                    | salida_dos
                    | salida_tres'''


def p_salida_uno(p):
    '''salida_uno : CONSOLE_WRITELINE PAR_IZQ STRING PAR_DER
                    | CONSOLE_WRITELINE PAR_IZQ operacion_string PAR_DER
                    | CONSOLE_WRITELINE PAR_IZQ IDENTIFICADOR PAR_DER'''

def p_salida_dos(p):
    '''salida_dos : CONSOLE_WRITELINE PAR_IZQ C_CADENA_INTERPOLADA STRING PAR_DER'''

def p_salida_tres(p):
    'salida_tres : CONSOLE_READLINE PAR_IZQ PAR_DER'

# --------------------------------------------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Tipos de definición de funciones ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def p_funcion(p):
  '''funcion : funcion_tipo_uno
             | funcion_tipo_tres
  '''
# ----------------------------------------- VEINTIMILLA --------------------------------------------
def p_funcion_tipo_uno(p):
  'funcion_tipo_uno : modificador_acceso VOID IDENTIFICADOR PAR_IZQ PAR_DER LLAVE_IZQ body LLAVE_DER'

# --------------------------------------------------------------------------------------------------

# ----------------------------------------- REYES --------------------------------------------
def p_funcion_tipo_tres(p):
  'funcion_tipo_tres : modificador_acceso VOID IDENTIFICADOR PAR_IZQ parametrosF PAR_DER LLAVE_IZQ bodyF LLAVE_DER'

def p_parametrosF(p):
  '''parametrosF : declaracion
                 | declaracion COMA parametrosF
  '''

def p_bodyF(p):
    '''bodyF : asignacion END_OF_LINE
            | declaracion END_OF_LINE
            | salida_entrada END_OF_LINE
            | asignacion END_OF_LINE bodyF
            | declaracion END_OF_LINE bodyF
            | salida_entrada END_OF_LINE bodyF'''

def p_lambda_exp(p):
    'lambda_exp : lambdaArg LAMBDA lambdaCuerpo'

def p_lambdaArg(p):
    '''lambdaArg : PAR_IZQ PAR_DER
            | PAR_IZQ lambdaParametrosUno PAR_DER
            | PAR_IZQ lambdaParametrosDos PAR_DER
            | IDENTIFICADOR
    '''
def p_lambdaParametrosUno(p):
    '''lambdaParametrosUno : valor_tipo IDENTIFICADOR
                        | valor_tipo IDENTIFICADOR COMA lambdaParametrosUno
    '''
def p_lambdaParametrosDos(p):
    '''lambdaParametrosDos : IDENTIFICADOR
                        |  IDENTIFICADOR COMA lambdaParametrosDos
    '''

def p_lambdaCuerpo(p):
    '''lambdaCuerpo : expresion
                    | salida_uno
                    | salida_dos
    '''
# --------------------------------------------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




# Regla de error para errores en la sintaxis
def p_error(p):
  if p:
    print(f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}")
    errores_sintactico.append(f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}\n")
    parser.errok()
  else:
    print("Error de sintaxis Fin de Linea")
    errores_sintactico.append("Error de sintaxis Fin de Linea\n")
 
# Build the parser
parser = yacc.yacc()

# Funcion que valida la regla sintactica
def validaReglaSintactica(s):
  errores_sintactico.clear()
  gram = parser.parse(s)
  resp = ''
  if gram is None:
    print(f"Linea: {str(resp)} | Info: No hay errores!")
    resp += (f"Linea: {str(resp)} | Info: No hay errores!"+"\n")
  else:
    print(f"Linea: {str(resp)} | Info: {str(gram)}")
    resp += (f"Linea: {str(resp)} | Info: {str(gram)}" + "\n")

  return resp if len(errores_sintactico) == 0 else ''

# while True:
#   try:
#     s = input('calc > ')
#   except EOFError:
#     break
#   if not s: continue
#   validaRegla(s)

#Main Ejecutable
# print(
#     "\nAnalizador Sintactico\n"+
#         " 1. Archivo de prueba Chevez\n"+
#         " 2. Archivo de prueba Reyes\n"+
#         " 3. Archivo de prueba Veintimilla\n"+
#         " 9. Salir"
# )
# rutaFileTest = ""
# resp_opcion = input("Digite una opcion para hacer las pruebas: ")
# if(resp_opcion == "1"):
#     rutaFileTest = "G1_C#/tests/analizador_sintactico/testChevez.txt"
# elif(resp_opcion == "2"):
#     rutaFileTest = "G1_C#/tests/analizador_sintactico/testReyes.txt"
# elif(resp_opcion == "3"):
#     rutaFileTest = "G1_C#/tests/analizador_sintactico/testVeintimilla.txt"
# elif(resp_opcion == "4"):
#     rutaFileTest = "consola"
# else:
#     print("Vuelva pronto! :)")
#     sys.exit(-1)
# if(rutaFileTest != ""):
#     # Build the parser
#     file = open(rutaFileTest)
#     content = file.read()
#     lines = 0
#     for item in content.splitlines():
#         lines += 1
#         if item:
#             validaRegla(item)
