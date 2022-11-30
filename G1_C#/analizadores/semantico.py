from analizadores.sintactico import *
from analizadores.lexico import tokens

# String de errores
errores_semantico = []

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Cuerpo semantico ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def p_body(p):
    """body : semantica_lista_add
    | semantica_casting_float_to_int
    | semantica_stack
    | add_queue
    | cast_float_to_int END_OF_LINE
    | to_upper_case
    """
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Terminales ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# De ser necesario
p_valor
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Reglas semanticas ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# -------------------------------------------- CHEVEZ ----------------------------------------------
# Ecribir sus reglas semanticas
def p_add_queue(p):
  '''add_queue : asignacion_int_cola
    | encolar_int
    | asignacion_int_cola encolar_int
    | asignacion_string_cola
    | encolar_string
    | asignacion_string_cola encolar_string
  '''

def p_asignacion_int_cola(p):
  'asignacion_int_cola : QUEUE MENOR_QUE INT_TYPE MAYOR_QUE IDENTIFICADOR IGUAL NEW QUEUE MENOR_QUE INT_TYPE MAYOR_QUE PAR_IZQ PAR_DER END_OF_LINE'

def p_encolar_int(p):
  'encolar_int : IDENTIFICADOR PUNTO ENQUEUE PAR_IZQ INT PAR_DER END_OF_LINE'

def p_asignacion_string_cola(p):
  'asignacion_string_cola : QUEUE MENOR_QUE STRING_TYPE MAYOR_QUE IDENTIFICADOR IGUAL NEW QUEUE MENOR_QUE STRING_TYPE MAYOR_QUE PAR_IZQ PAR_DER END_OF_LINE'

def p_encolar_string(p):
  'encolar_string : IDENTIFICADOR PUNTO ENQUEUE PAR_IZQ STRING PAR_DER END_OF_LINE'

def p_to_upper_case(p):
  '''to_upper_case : asignacion_string
    | str_to_upper_case
    | asignacion_string str_to_upper_case
    | asignacion_string str_to_upper_case to_upper_case
  '''
def p_str_to_upper_case(p):
  'str_to_upper_case : IDENTIFICADOR PUNTO TO_UPPER PAR_IZQ PAR_DER END_OF_LINE'

def p_asignacion_string(p):
  'asignacion_string : STRING_TYPE IDENTIFICADOR IGUAL STRING END_OF_LINE'
# --------------------------------------------------------------------------------------------------




# -------------------------------------------- REYES -----------------------------------------------
# Ecribir sus reglas semanticas

#Regla semantica para añadir y eliminar elementos de una pila
# Se creo la sgte regla tentativa para ver si es posible usarla en la sustentación
'''
def p_semantica_stack(p):
  'semantica_stack : declaracionPila END_OF_LINE IDENTIFICADOR IGUAL asignacionPila END_OF_LINE operacionesStack
                    | pila operacionesStack'
'''
def p_semantica_stack(p):
  'semantica_stack : operacionesStack'

def p_operacionesStack(p):
  '''operacionesStack : push_pop_stack
  '''

def p_push_pop_stack(p):
  '''push_pop_stack : asignacion_int_stack
                | push_stack_int
                | asignacion_int_stack push_stack_int
                | asignacion_float_stack
                | push_stack_float
                | asignacion_float_stack push_stack_float
                | pop_stack_int
                | pop_stack_float
                | asignacion_int_stack push_stack_int pop_stack_int
                | asignacion_float_stack push_stack_float pop_stack_float
                | asignacion_int_stack pop_stack_int
                | asignacion_float_stack pop_stack_float

  '''

def p_asignacion_int_stack(p):
  '''asignacion_int_stack : STACK MENOR_QUE INT_TYPE MAYOR_QUE IDENTIFICADOR IGUAL NEW STACK MENOR_QUE INT_TYPE MAYOR_QUE PAR_IZQ PAR_DER END_OF_LINE'''

def p_push_stack_int(p):
  'push_stack_int : IDENTIFICADOR PUNTO PUSH PAR_IZQ INT PAR_DER END_OF_LINE'

def p_asignacion_float_stack(p):
  '''asignacion_float_stack : STACK MENOR_QUE FLOAT_TYPE MAYOR_QUE IDENTIFICADOR IGUAL NEW STACK MENOR_QUE FLOAT_TYPE MAYOR_QUE PAR_IZQ PAR_DER END_OF_LINE'''

def p_push_stack_float(p):
  'push_stack_float : IDENTIFICADOR PUNTO PUSH PAR_IZQ FLOAT PAR_DER END_OF_LINE'

def p_pop_stack_int(p):
  'pop_stack_int : INT_TYPE IDENTIFICADOR IGUAL IDENTIFICADOR PUNTO POP PAR_IZQ PAR_DER END_OF_LINE'

def p_pop_stack_float(p):
  'pop_stack_float : FLOAT_TYPE IDENTIFICADOR IGUAL IDENTIFICADOR PUNTO POP PAR_IZQ PAR_DER END_OF_LINE'

# --------------------------------------------------------------------------------------------------




# ----------------------------------------- VEINTIMILLA --------------------------------------------
# Ecribir sus reglas semanticas
def p_semantica_lista_add(p):
  '''semantica_lista_add : asignacion_int_lista
    | add_lista_int
    | asignacion_int_lista add_lista_int
    | asignacion_string_lista
    | add_lista_string
    | asignacion_string_lista add_lista_string
  '''

def p_asignacion_int_lista(p):
  'asignacion_int_lista : LIST MENOR_QUE INT_TYPE MAYOR_QUE IDENTIFICADOR IGUAL NEW LIST MENOR_QUE INT_TYPE MAYOR_QUE PAR_IZQ PAR_DER END_OF_LINE'

def p_add_lista_int(p):
  'add_lista_int : IDENTIFICADOR PUNTO ADD PAR_IZQ INT PAR_DER END_OF_LINE'

def p_asignacion_string_lista(p):
  'asignacion_string_lista : LIST MENOR_QUE STRING_TYPE MAYOR_QUE IDENTIFICADOR IGUAL NEW LIST MENOR_QUE STRING_TYPE MAYOR_QUE PAR_IZQ PAR_DER END_OF_LINE'

def p_add_lista_string(p):
  'add_lista_string : IDENTIFICADOR PUNTO ADD PAR_IZQ STRING PAR_DER END_OF_LINE'



def p_semantica_casting_float_to_int(p):
  'semantica_casting_float_to_int : FLOAT_TYPE IDENTIFICADOR IGUAL FLOAT END_OF_LINE INT_TYPE IDENTIFICADOR END_OF_LINE cast_float_to_int'

def p_cast_float_to_int(p):
  'cast_float_to_int : IDENTIFICADOR IGUAL PAR_IZQ INT_TYPE PAR_DER IDENTIFICADOR END_OF_LINE'
# --------------------------------------------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




# Regla de error para errores en la sintaxis
def p_error(p):
  if p:
    print(f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}")
    errores_semantico.append(f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}\n")
    parser.errok()
  else:
    print("Error de sintaxis Fin de Linea")
    errores_semantico.append("Error de sintaxis Fin de Linea\n")
 
# Build the parser
parser = yacc.yacc()

# Funcion que valida la regla sintactica
def validaReglaSemantica(s):
  errores_semantico.clear()
  gram = parser.parse(s)
  resp = ''
  if gram is None:
    print(f"Linea: {str(resp)} | Info: No hay errores!")
    resp += (f"Linea: {str(resp)} | Info: No hay errores!"+"\n")
  else:
    print(f"Linea: {str(resp)} | Info: {str(gram)}")
    resp += (f"Linea: {str(resp)} | Info: {str(gram)}" + "\n")
  return resp if len(errores_semantico) == 0 else ''