import re
Texto = "texto qualquer   123 "

#re.compile(r'Expressão Regular')
Expressao = re.compile(r'[a-z]*')

#re.match(r'Expressão Regular',Texto)
Resultado =re.search(r'[a-z]*',Texto)
#OU
Resultado = Expressao.match(Texto)
print(Resultado)

#re.search(r'Expressão Regular',Texto)
Resultado =re.search(r'texto q',Texto)
print(Resultado)

#re.fullmatch(r'Expressão Regular',Texto) -> se String Inteira Bater
Resultado =re.fullmatch(r'texto qualquer   123 ',Texto)
print(Resultado)

#re.split(r'Expressão Regular',Texto, maxsplit = 0 ) 
Resultado =re.split(r' ',Texto, 2)
print(Resultado)

#re.findall(r'Expressão Regular',Texto ) 
Resultado =re.findall(r'[0-9]{3}',Texto)
print(Resultado)


#- FLAGS -#

#re.A
#re.ASCII      -> Faça \w, \W, \b, \B, \d, \De execute \sa \S correspondência somente ASCII em vez da correspondência Unicode completa.

#re.DEBUG

#re.I
#re.IGNORECASE -> Ignora a diferença entre letras maiusculas e minusculas 

#re.L
#re.LOCALE

#re.M
#re.MULTILINE -> Pega o texto todo, não só uma linha

#re.S
#re.DOTALL    -> Faz com que a expressão regular ' . ' seja até mesmo para quebra de linha 

#re.X
#re.VERBOSE  -> Faz com que possamos quebrar a linha da expresão regular
