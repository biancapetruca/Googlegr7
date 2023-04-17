def validare(cnp):
    if len(cnp) != 13:
        return False
    for cifra in cnp:
        if not cifra.isdigit():
            return False
    cifra1 = int(cnp[1])
    # sex = 0
    an = 0
    zi = 0
    luna = 0
    jj = 0
    nnn = 0
    if cifra1 == [1, 2]:
        an += 1900
    elif cifra1 == [3, 4]:
        an += 1800
    elif cifra1 == [5, 6]:
        an += 2000
    elif cifra1 == [7, 8]:
        return("Persoane straine rezidente in Romania")
    elif cifra1 == 9:
        return("Persoane straine")
    else:
        return("CNP invalid")
    while an in (1800, 2100):
        ultimele_cifre = an % 100
        print(ultimele_cifre)
    if luna > 12 and zi > 31:
        return("CNP invalid")
    if jj in range(1, 52):
        return jj
    if nnn in range(1, 999):
        return nnn

# cifra de control
    control = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
    suma = 0
    for i in range(12):
        suma += control[i] * int(cnp[i])
    cifra_control = suma % 11
    if cifra_control == 10:
        cifra_control = 1
    if cifra_control == int(cnp[12]):
        return True
    else:
        return False

cnp = input("Introduceti CNP-ul: ")
if validare(cnp):
    print("CNP-ul este valid.")
else:
    print("CNP-ul este invalid.")







