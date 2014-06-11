nBrut = float(input('Digite o valor Bruto: '))
nDep = int(input('Numero de dependente: '))

if (nBrut <= 1317.07):
    inss = nBrut * 8/100
    nomInss = "8% de inss"
elif (nBrut <= 2195.12):
    inss = nBrut * 9/100
    nomInss = "9% de inss"
elif (nBrut >= 2195.1310):
    inss = nBrut * 11/100
    if (inss >= 482.93 ):
        inss = 482.93
        nomInss = "11% de inss"
    else:
        inss = inss
        nomInss = "11% de inss"

nBrut = nBrut - inss

if (nDep == 0):
    nDep = 0
    nomDep = "Não dependente"
elif (nDep > 0):
    nDep = nDep * 179.71
    nomDep = "Houve dependente deconto de "
    
nBrut = nBrut - nDep

if (nBrut <= 1787.77):
    irpf = 0
    nomIrpf = "Não houve dedução de Imposto"
elif (nBrut <= 2679.29):
    irpf = nBrut * 7.5/100
    irpf = irpf - 134.08
    nomIrpf = "Deduziu 7,5% "
elif (nBrut <= 3572.43):
    irpf = nBrut * 15/100
    irpf = irpf - 335.03
    nomIrpf = "Deduziu 15% "
elif (nBrut <= 4463.81):
    irpf = nBrut * 22.5/100
    irpf = irpf - 602.96
    nomIrpf = "Deduziu 22,5% "
elif (nBrut > 4463.81):
    irpf = nBrut * 27.5/100
    irpf = irpf - 826.15
    nomIrpf = "Deduziu 27,5% "
    
print("Foram descontados os seguintes valores")
print(nomInss, round(inss, 2), "R$")
print(nomDep, round(nDep, 2), "R$")
print(nomIrpf, "o valor para pagar", round(irpf, 2), "R$")
