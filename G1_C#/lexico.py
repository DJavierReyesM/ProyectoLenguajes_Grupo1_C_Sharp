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
    "DOS_PUNTOS"
] + list(reserved.values())
# Expresiones Regulares / Funciones

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
