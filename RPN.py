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
with open('Calc1.stk', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        try:
            linha = int(linha)
            if not first:
                resultado[0] = int(linha)
                first = True
            elif not second:
                resultado[1] = int(linha)
                second = True
        except ValueError:
            linha = str(linha)
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

print(resultado[2])