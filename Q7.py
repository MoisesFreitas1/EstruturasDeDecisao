votos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
neleitores = 10
def cls(): print("\n" * 50)

for i in range(0,10):
    print("Eleicao para Prefeito")
    print("1 - Careca")
    print("2 - Ze do Ovo")
    print("3 - Firmino Filho")
    print("4 - Tiririca")
    print("5 - Voto nulo")
    print("6 - Voto em branco")
    opcao = int(input("Voto: "))
    votos[i] = opcao
    cls()

Careca = 0
ZeDoOvo = 0
Firmino = 0
Tiririca = 0
Nulo = 0
Branco = 0
for i in range(0,10):
    if votos[i]==1:
        Careca = Careca+1
    if votos[i]==2:
        ZeDoOvo = ZeDoOvo+1
    if votos[i]==3:
        Firmino = Firmino+1
    if votos[i]==4:
        Tiririca = Tiririca+1
    if votos[i]==5:
        Nulo = Nulo+1
    if votos[i]==6:
        Branco = Branco+1

pCareca = (Careca*100/neleitores)
pZeDoOvo = (ZeDoOvo*100/neleitores)
pFirmino = (Firmino*100/neleitores)
pTiririca = (Tiririca*100/neleitores)
pNulo = (Nulo*100/neleitores)
pBranco = (Branco*100/neleitores)

print("Careca: ", Careca," votos -",pCareca,"%")
print("Ze do Ovo: ", ZeDoOvo," votos -",pZeDoOvo,"%")
print("Firmino Filho: ", Firmino," votos -",pFirmino,"%")
print("Tiririca: ", Tiririca," votos -",pTiririca,"%")
print("Voto nulo: ", Nulo," votos -",pNulo,"%")
print("Voto em branco: ", Branco," votos -",pBranco,"%")