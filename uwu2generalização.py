a=0
b=0

a = int(input("Escolha um número: \n"))
b = int(input("Escolha outro número: \n"))

op_adicao=a+b
op_subtracao=a-b
op_multiplicacao=a
op_divisao=a
op_divisao_int=a//b
op_modulo_div=a%b
op_exponenciacao=a**b
op = str(input("Escolha uma operação:adição, subtração, multiplicação, divisão, divisão inteira, módulo, exponenciação \n"))

if op == "adição":
    print("Adição -> ",a,"+",b, "=" ,op_adicao)
elif op == "subtração":
    print("Subtração-> ",a,"-",b, "=" ,op_subtracao)
elif op == "multiplicação":
    print ("Multiplícação-> ",a,"x" ,b,"=" ,op_multiplicacao)
elif op == "divisão":
    print("Dívisão-> ",a," I ",b,"=",op_divisao)
elif op == "divisão inteira":
    print("Dívisão inteira->",a,"ll",b,"=",op_divisao_int)
elif op == "módulo":
    print("Módulo-> ",a,"%", b, "=" , op_modulo_div)
elif op == "exponenciação":
    print("Exponencíação->",a,"**" ,b,"=" , op_exponenciacao)
else:
    print("Operação inválida")