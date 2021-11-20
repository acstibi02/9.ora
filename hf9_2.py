a_oldal = float(input("Add meg a doboz 'a' oldalának hosszát két tizedesjegyre kerekítve(cm): "))
b_oldal = float(input("Add meg a doboz 'b' oldalának hosszát két tizedesjegyre kerekítve(cm): "))
c_oldal = float(input("Add meg a doboz 'c' oldalának hosszát két tizedesjegyre kerekítve(cm): "))

def terfogat(a_oldal:float,b_oldal:float,c_oldal:float):
    ter=a_oldal*b_oldal*c_oldal
    return ter

print(terfogat(a_oldal,b_oldal,c_oldal))