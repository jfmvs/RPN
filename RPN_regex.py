import re

dicio = {'+':'PLUS','-':'MINUS','/':'SLASH','*':'STAR'}
pilha = []

class Token:
    def __init__(self,type,value):
        self.type = type
        self.value = value
    def info(self):
        print(f'Token[type={self.type},lexeme={self.value}]')

def operando(x,y,z):
    if z == "+":
        return x + y
    elif z == "-":
        return x - y
    elif z == "*":
        return x * y
    elif z == '/':
        return x / y
 
def scan(source):
    for j in range(len(source)):
        if (source[j].isdigit()) or (source[j] in dicio.keys()):
            if source[j] in dicio.keys():
                source[j] = Token(dicio[source[j]],source[j])
            else:
                source[j] = Token('NUM',int(source[j]))
        else:
            print('Error: Unexpected character: ',source[j])
            return -1
    return source

def scan_regex(source):
    tokens = []
    regex = r"\d+|[+\-*/]"
    for token in source:
        padrao = re.match(regex,token)
        if padrao:
            if token.isdigit():
                tokens.append(Token('NUM', int(token)))
            else:
                tokens.append(Token(dicio[token], token))
        else:
            print('Error: Unexpected character: ',token)
            return -1
    return tokens

def calculo(lista):
    while len(lista) > 1:
        if lista[0].type != 'NUM':
            if lista[1].type != 'NUM':
                lista = lista[:1] + calculo(lista[1:])
            else:
                if lista[2].type == 'NUM':
                    resultado = operando(lista[2].value,lista[1].value,lista[0].value)
                    lista[0] = Token('NUM',resultado)
                    lista.pop(1)
                    lista.pop(1)
                else:
                    lista = lista[:2] + calculo(lista[2:])
        else:
            return lista
    return lista

with open('Calc1.stk', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        pilha.insert(0,linha)

tokens = scan_regex(pilha)

if tokens != -1:
    for token in reversed(tokens):
        token.info()
    print(f'Saída: {calculo(tokens)[0].value}')