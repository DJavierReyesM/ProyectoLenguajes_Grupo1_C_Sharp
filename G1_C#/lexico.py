import ply.lex as lex

# Analizador Léxico: C#
# Grupo 1:
#   => Kevin Isaac Chevez Coronel
#   => Guillermo Alejandro Veintimiila Altamirano
#   => Diego Javier Reyes Medranda

# Palabras reservadas
reserved = {
}

# Tokens
tokens = [
    "DOS_PUNTOS",
    "FLOAT",
    "DOUBLE"
] + list(reserved.values())
# Expresiones Regulares / Funciones

# Expresiones regulares para tokens simples (Simbolos)
t_SUMA = r'\+'








































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
