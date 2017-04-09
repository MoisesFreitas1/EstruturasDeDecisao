anoNascimento = int(input("Ano de Nascimento: "))
ano = 2017

idade = ano - anoNascimento

if idade >= 16:
    print("Tem idade para votar")
else:
    print("Nao tem idade para votar")
if idade >= 18:
    print("Pode conseguir a Carteira de Habilitacao")
else:
    print("Nao pode tirar a Cateira de Habilitacao")