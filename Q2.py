idade = int(input("Idade do nadador: "))

if idade < 5:
    print("Categoria Infantil")
if idade >= 5 and idade < 10:
    print("Categoria Juvenil")
if idade >= 10 and idade < 16:
    print("Categoria Adolescente")
if idade >= 16 and idade < 25:
    print("Categoria Adulto")
if idade >= 25:
    print("Categoria Senior")