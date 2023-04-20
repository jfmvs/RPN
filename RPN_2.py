def operando(x,y,z):
    if z == "+":
        return x + y
    elif z == "-":
        return x - y
    elif z == "*":
        return x * y
    elif z == '/':
        return x / y

resultado = 0
first = False
second = False
resultado = [0,0,0,0]
previous = False
class Token:
    def __init__(self,type,value):
        self.type = type
        self.value = value
    def info(self):
        print(f'Token[type={self.type},lexeme={self.value}]')
error = False
with open('teste.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        try:
            linha = int(linha)
            linha_ = Token('NUM',linha)
            linha_.info()
            if not first:
                resultado[0] = linha
                first = True
            elif not second:
                resultado[1] = linha
                second = True
        except ValueError:
            linha = str(linha)
            if linha in ['+','-','/','*']:
                if linha == '+':
                    linha_ = Token('PLUS',linha)
                elif linha == '-':
                    linha_ = Token('MINUS',linha)
                elif linha == '/':
                    linha_ = Token('SLASH',linha)
                elif linha == '*':
                    linha_ = Token('STAR',linha)
                linha_.info()
                if (first and second):
                    if not previous:
                        resultado[2] = operando(resultado[0],resultado[1],linha)
                        previous = True
                        first = False
                        second = False
                    else:
                        resultado[3] = operando(resultado[0],resultado[1],linha)
                        first = False
                        second = False 
                elif first:
                    resultado[2] = operando(resultado[0],resultado[2],linha)
                    first = False
                else:
                    resultado[2] = operando(resultado[2],resultado[3],linha)
            else:
                print(f'Error: Unexpected character: {linha}')
                error = True
                break

if not error:
    print(f'Saída: {resultado[2]}')