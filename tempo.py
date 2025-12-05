seg=float(input("Digite os segundos: "))
#print(seg>60 and seg<1)
while not(seg < 1 and seg > 60):
    print("Valor inválido! Escolha um valor entre 1 e 60")
    seg=float(input("Digite os segundos: "))

min=float(input("Digite os minutos: "))

#print(min>60 and min<1)
while not(min < 1 and min > 60):
    print("Valor inválido! Escolha um valor entre 1 e 60")
    seg=float(input("Digite os minutos: "))

ho=float(input("Digite as horas: "))
#print(seg>60 and seg<1)
while not(ho < 0 and ho > 23):
    print("Valor inválido! Escolha um valor entre 0 e 23")
    seg=float(input("Digite as horas: "))
    
val=seg + (min*60)+(ho*3600)

print("o total em segundos é: ", val)