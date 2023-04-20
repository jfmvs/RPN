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

scan(pilha)

if pilha != -1:
    for token in reversed(pilha):
        token.info()
    print(f'Saída: {calculo(pilha)[0].value}')
