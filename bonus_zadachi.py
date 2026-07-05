# Да се направи програма во која корисникот ќе може да внесе
# произволен број на елементи. Потоа со помош на циклус(и) да се
# сортира листата во растечки редослед.
# *Да не се користи готова функција
# *Бонус – Да може корисникот да избере дали да биде сортирањето во
# растечки или опаѓачки редослед


# broj_na_elemnti = int(input("Kolku elementi sakas da vneses: "))

# lista = []

# for i in range(broj_na_elemnti):
#     broj = int(input("Vnesi broj: "))
#     lista.append(broj)

# opcija = input("Vnesi 'r' za rastecki ili 'o' za opagjacki: ")
# for i in range(broj_na_elemnti):
#     for j in range(broj_na_elemnti - i - 1):
#         if opcija == "r":
#             if lista[j] > lista[j + 1]:
#                 lista[j] = lista[j + 1]
#                 lista[j + 1] = lista[j]
#         elif opcija == "o":
#             if lista[j] < lista[j + 1]:
#                 lista[j] = lista[j + 1]
#                 lista[j + 1] = lista[j]

#         else:
#             print("Gresen izbor!")
#             break

# print("Sortirana lista:", lista)

# Да се направи програма во која корисникот ќе може да внесе
# произволен број на елементи. Потоа корисникот да избере за кој
# елемент сака да се преброи колку пати се појавува и со помош на
# циклуси да се преброи појавуавњето. Доколку елементот го нема во
# листата да се испечати дека тој елемент не постои

# broj_na_elemnti = int(input("Kolku elementi sakas da vneses: "))

# lista = []

# for i in range(broj_na_elemnti):
#     broj = int(input("Vnesi broj: "))
#     lista.append(broj)

# broj_na_povtoruvanja = int(input("Vnesi element koj sakas da go proveris: "))

# brojac = 0

# for i in range(broj_na_elemnti):
#     if lista[i] == broj_na_povtoruvanja:
#         brojac += 1


# if brojac > 0:
#     print("Elementot se pojavuva", brojac, "pati")
# else:
#     print("Elementot ne postoi vo listata")

# Да се направи програма во која корисникот ќе може да внесе
# произволен број на елементи. Потоа со помош на циклуси да се
# избришаат дупликатите доколку ги има во листата

# broj_na_elementi = int(input("Kolku elementi sakas da vneses: "))

# lista = []

# for i in range(broj_na_elementi):
#     broj = int(input("Vnesi broj: "))
#     lista.append(broj)
# unikatna_lista = []
# for i in range(broj_na_elementi):
#     if lista[i] not in unikatna_lista:
#         unikatna_lista.append(lista[i])

# print("Lista bez duplikati:", unikatna_lista)


# Бонус – Да се брои секој дупликат што е пронајден по колку пати се има
# појавено – може да се користи dictionary за ова

broj_na_elementi = int(input("Kolku elementi sakas da vneses: "))

lista = []

for i in range(broj_na_elementi):
    broj = int(input("Vnesi broj: "))
    lista.append(broj)
broevi = {}
for i in range(broj_na_elementi):
    if lista[i] in broevi:
        broevi[lista[i]] += 1
    else:
        broevi[lista[i]] = 1

for broj in broevi:
    if broevi[broj] > 1:
        print(broj, "se pojavuva", broevi[broj], "pati (duplikat)")
    else:
        print(broj, "se pojavuva 1 pat")