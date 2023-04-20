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
    return

def calculo(lista):
    n = 0
    while len(lista) > 1:
        if lista[n].type != 'NUM':
            if lista[n+1].type != 'NUM':
                n += 1
                continue
            else:
                resultado = operando(lista[n+2].value,lista[n+1].value,lista[n].value)
                lista[n] = Token('NUM',resultado)
                lista.pop(n+1)
                lista.pop(n+1)
                n = 0
    return lista[0].value


with open('teste.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        pilha.insert(0,linha)
print('Arquivo lido')
print(pilha)

tokens = scan(pilha)

if tokens != -1:
    print('Tokens criados')

    print(f'Saída: {calculo(pilha)}')
