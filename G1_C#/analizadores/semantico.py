from analizadores.sintactico import *

# String de errores
errores_semantico = []

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Cuerpo semantico ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def p_body(p):
    """body : semantica_lista_add
    | semantica_casting_float_to_int
    | semantica_stack
    | add_queue END_OF_LINE
    | cast_float_to_int END_OF_LINE
    | to_upper_case END_OF_LINE
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
  'add_queue : CHAR_TYPE'

def p_to_upper_case(p):
  'to_upper_case : CHAR_TYPE'
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
def p_push_stack(p):
  'add_stack : stack_push'

def p_pop_stack(p):
  'pop_stack : stack_pop'

def p_operacionesStack(p):
  '''operacionesStack : add_stack END_OF_LINE pop_stack END_OF_LINE
                      | add_stack END_OF_LINE
                      | pop_stack END_OF_LINE
  '''
# --------------------------------------------------------------------------------------------------




# ----------------------------------------- VEINTIMILLA --------------------------------------------
# Ecribir sus reglas semanticas
'''def p_semantica_lista(p):
  'semantica_lista : lista END_OF_LINE lista_add END_OF_LINE'
'''

def p_semantica_lista_add(p):
  'semantica_lista_add : lista_add END_OF_LINE'

def p_lista_add(p):
  'lista_add : add_lista'

def p_semantica_casting_float_to_int(p):
  'semantica_casting_float_to_int : FLOAT_TYPE IDENTIFICADOR IGUAL FLOAT END_OF_LINE cast_float_int'

def p_cast_float_int(p):
  'cast_float_int : cast_float_to_int'
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