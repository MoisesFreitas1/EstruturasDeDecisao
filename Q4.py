codigo = int(input("Codigo: "))
preco = float(input("Preco: R$"))

if preco<100:
    novoPreco = preco*1
if preco>=100 and preco<500:
    novoPreco = preco*0.9
if preco>=500:
    novoPreco = preco*0.8

desconto = preco - novoPreco

print("\nDesconto: R$%.2f"%desconto)
print("Novo Preco: R%.2f"%novoPreco)
