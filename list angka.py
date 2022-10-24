angka = input("Isi list angka (integer) :")
splitted_angka= angka.split()
for x in splitted_angka[0:]:
    x=int(x)
    if x%2==1:
        print(x, "adalah angka ganjil")
    elif x%2==0:
        print(x, "adalah angka genap")
if x%2==0:
    print("List angka memiliki angka genap")
else:
    print("List angka tidak memiliki angka genap")