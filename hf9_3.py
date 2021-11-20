szam1 = int(input("Add meg az 1. számot: "))
szam2 = int(input("Add meg az 2. számot: "))
szam3 = int(input("Add meg az 3. számot: "))
szam4 = int(input("Add meg az 4. számot: "))
szam5 = int(input("Add meg az 5. számot: "))

def legnagyobb(szam1:int,szam2:int,szam3:int,szam4:int,szam5:int):
    seged = szam1
    lista = []
    lista.append(szam1),lista.append(szam2)
    lista.append(szam3)
    lista.append(szam4)
    lista.append(szam5)
    for i in range(len(lista)):
        if lista[i] > seged:
            seged = lista[i]
    return seged
print(legnagyobb(szam1,szam2,szam3,szam4,szam5))