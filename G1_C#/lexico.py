import ply.lex as lex

# Analizador Léxico: C#
# Grupo 1:
#   => Kevin Isaac Chevez Coronel
#   => Guillermo Alejandro Veintimiila Altamirano
#   => Diego Javier Reyes Medranda

# Palabras reservadas
reserved = {
  'true': 'TRUE',
  'false': 'FALSE',
}

# Tokens
tokens = [
    "DOS_PUNTOS",
    "FLOAT", "SUMA", "RESTA", "MULTIPLICACION", "DIVISION", "MODULO", "SIMPLE_AND", "SIMPLE_OR", "IR", "NOR", "NEGACION", "AND", "OR",
    "DOUBLE", "INCREMENTO", "DECREMENTO", "SHIFT_MENOR", "SHIFT_MAYOR", "IGUAL_IGUAL", "NO_IGUAL", "MENOR_QUE", "MENOR_O_IGUAL_QUE", "MAYOR_QUE", "MAYOR_O_IGUAL_QUE", "IGUAL", "AUMENTADO", "DECREMENTADO", "MULTIPLICADO_POR", "DIVIDIDO_POR", "MODULO_DE",
] + list(reserved.values())
# Expresiones Regulares / Funciones

# Expresiones regulares para tokens simples (Simbolos)
t_SUMA = r'\+'
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
t_NO_IGUAL = r'!='
t_MENOR_QUE = r'<'
t_MENOR_O_IGUAL_QUE = r'<='
t_MAYOR_QUE = r'>'
t_MAYOR_O_IGUAL_QUE = r'>='
t_IGUAL = r'='
t_AUMENTADO = r'\+='
t_DECREMENTADO = r'-='
t_MULTIPLICADO_POR = r'\*='
t_DIVIDIDO_POR = r'/='
t_MODULO_DE = r'%='











#Fin de seccion de simbolos

t_DOS_PUNTOS = ":"
# Conteo de Lineas
def t_newline(t):
  r'\n+'
  t.lexer.lineno += t.value.count('\n')
# Token de "ignorar"
t_ignore = ' \t'
t_ignore_SingleLineComments = r'//.*'
# Toke de error
def t_error(t):
    print("Caracter no permitido: '%s'" %t.value[0])
    t.lexer.skip(1)

def t_FLOAT(t):
  r'\d+\.(\d){1,7}(f|F){1}'
  t.value = float(t.value)
  return t

def t_DOUBLE(t):
  r'\d+\.(\d){1,15}(\s|d|D){1}'
  t.value = float(t.value)
  return t

lexer = lex.lex()

print('Analizador Léxico: C#'+"\n")

content = ':::'

#file_source = open("source.txt")
#content = file_source.read()
lexer.input(content)
for token in lexer:
  print(f'>> Valor del Token: {token.value}')
  print(token)
  print("\n")
#file_source.close()

print("\nFin del programa")
