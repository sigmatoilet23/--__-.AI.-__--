"""Atribuição de dados a variáveis, ficando automaticamente
declaradas"""
i=90
f=1.5
c=2+3j
disc="APIB"
l=True
d = [1.5,12,"AIB"]
e=(7,"Classif",19.6)
cc={l,2,3,4,5,6}
dic={l:'decimo',2:'decimo primeiro',3:'decimo segundo'}
"""Utilização da função Type na determinação do tipo de dado de
cada variável"""
td=type(i)
print(td)
td=type(f)
print(td)
print(type(c))
st=type(disc)
print(st)
print(type(l))
print(type(d))
print(type(e))
print(type(cc))
print(type(dic))
print("---------------")
"""Utilização da função Type na determinação do tipo de dado de
cada valor"""
st=type (3.14)
print(st)
print(type (9999))