deposito = float(input("Deposito: R$"))
txJuros = float(input("Taxa de juros (%/mes): "))
periodo = int(input("Periodo (meses): "))
acrescimo = float(input("Acrescimo mensal: R$"))

txJuros = txJuros/100

montante = deposito*(1+txJuros)+acrescimo
if periodo == 0:
    montante = 0
else:
    for i in range(0,(periodo-1)):
        montante = montante*(1+txJuros)+acrescimo

rendimento = montante - deposito - (acrescimo*periodo)
print("\nRendimento: R$%.2f"%rendimento)
print("Montante: R$%.2f"%montante)
