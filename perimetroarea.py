from math import pi
raio=float(input("Digite um valor para o raio: "))
perim=2*pi*raio
area=pi*raio*raio
if raio>0:
    print ("O valor do perímetro é:", perim)
    print("O valor da área é:", area)
else:
    print("Erro:A operação não pode ser concluída")