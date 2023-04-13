a = input("Alege o valoare: ")
try:
    print(int(a))
    print(variabila_nedef)

except NameError as e:
    variabila_nedef = None
    print('Name error', e)

except ValueError:
    print("S-a intalnit o eroare")
    a = input("Alege o alta valoare: ")

except Exception as e:
    print(e)
else:
    print("S-a executat cu succes")
finally:
    print("Se executa oricum")
print("A trecut de blocul de try-except",variabila_nedef)