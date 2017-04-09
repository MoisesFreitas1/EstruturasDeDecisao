custoF = float(input("Custo da Festa: R$"))
pConvite = float(input("Valor do convite: R$"))

nconvites = round(custoF/pConvite)

multi = nconvites * pConvite
if multi < custoF:
    nconvites = nconvites + 1
print(nconvites," convites")