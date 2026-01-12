codigo_ascii = int(input("Digite um código ASCII entre 33 e 126: "))

if 33 <= codigo_ascii <= 126:
    print(chr(codigo_ascii))
else:
    print("Indicou um código inválido.")
