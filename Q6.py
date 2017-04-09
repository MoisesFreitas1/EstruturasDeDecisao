preco = float(input("Preco: "))
print("Condicao de Pagamento")
print("1 - À vista em dinheiro ou cheque")
print("2 - À vista no cartão de crédito")
print("3 - Em 2x")
print("4 - Em 3x")
opcao = int(input("Opcao: "))
if opcao == 1:
    novoPreco = preco*0.8
    print("Novo Preco: R$%.2f"%novoPreco)
else:
    if opcao == 2:
        novoPreco = preco*0.9
        print("Novo Preco: R$%.2f" % novoPreco)
    else:
        if opcao == 3:
            novoPreco = preco
            print("Novo Preco: R$%.2f" % novoPreco)
        else:
            if opcao == 4:
                novoPreco = preco*1.05
                print("Novo Preco: R$%.2f" % novoPreco)
            else:
                print("Opcao invalida!")