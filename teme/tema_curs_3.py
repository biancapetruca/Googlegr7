
def operatie():
    lista = ('+', "-", "*", "/")
    while True:
        operator = input("Alege operatia dorita: ")
        if operator in lista:
            return operator
        else:
            print(f"Alege o alta operatie: ")

# def stergere():
#     cifra = input("Alege o cifra: ")
#     if cifra.isdigit():
#         return cifra
#     elif cifra == "C":
#         return calcul()
#     else:
#         print("Intorduceti o cifra sau C pentru a sterge: ")

def calcul():
    num1 = input("Alege primul numar: ")
    num2 = input("Alege al doilea numar: ")
    lista = ('+', "-", "*", "/")
    operator = operatie()

    if operator in lista and num1.isdigit() and num2.isdigit():
        if operator == "+":
                print(f"Suma numerelor este: {num1} + {num2} =  {int(num1) + int(num2)}")
        elif operator == "-":
                print(f"Diferenta numerelor este: {num1} - {num2} = {int(num1) - int(num2)}")
        elif operator == "*":
                print(f"Produsul numerelor este: {num1} * {num2} = {int(num1) * int(num2)}")
        else:
                print(f"Impartirea numerelor este: {num1} / {num2} = {int(num1) / int(num2)}")
    else:
            print(f"Alege o operatie din lista: {','.join(lista)}")


calcul()

