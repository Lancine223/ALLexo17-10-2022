number=int(input("Saisir un nombre positif: "))
factorisation=1
i=1
while (i <= number):
    factorisation=factorisation*i
    i=i+1
print(f"La factorielle de {number} est: {factorisation}")
