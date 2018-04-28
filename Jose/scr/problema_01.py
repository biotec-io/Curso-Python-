multiplos_3 = []
multiplos_5 = []
def multiplo(valor, multiplo):
    resto = valor % multiplo
    if resto == 0:
        return True
    else:
        return False

for i in range(1, 1001):
    if multiplo(i, 3):
        multiplos_3.append(i)
    if multiplo(i, 5):
        multiplos_5.append(i)
print("Multiplos de 3: ", multiplos_3)
print(" ")
print("Multiplos de 5: ", multiplos_5)
