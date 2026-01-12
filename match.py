def adicao(a1,a2):
    return a1 + a2

def multi(m1,m2):
    return m1 * m2

n1=float(input("Digite o primeiro número: "))
n2=float(input("Digite o segundo número: "))

opcao=input("Escolha a opção, A:Adição; M:Multiplicação: ")

if opcao == "A":
    resultado = adicao(n1, n2)
    print("Resultado da adição:", resultado)
elif opcao == "M":
    resultado = multi(n1, n2)
    print("Resultado da multiplicação:", resultado)
else:
    print("Opção Inválida")