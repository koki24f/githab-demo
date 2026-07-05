# Задача 1: Напиши функција која прашува од корисникот да внесе својата возраст и испишува
#  "Вие сте малолетни" ако возраста е помала од 18, а "Вие сте полнолетни" во спротивно.

# def pechati_ime(ime,godini):
#     if godini <=18:
#         print(f"{ime} vie ste maloletni")
#     else:
#         print(f"{ime} vie ste polnoleteni")    

# ime="Kostadinka"
# godini=20
# pechati_ime(ime,godini)

#Задача 2: Напиши програма која бара од корисникот да внесе број и креирај функција која испишува
#  дали тој е позитивен, негативен или нула.
# def pechati_broj(broj:int):
#     if broj <0:
#         print(f"{broj} brojot e negativen")
#     elif broj >0:
#         print(f"{broj} brojot e pozitiven")
#     else:
#         print (f"{broj} e ednakov na nula")   

# broj=22
# pechati_broj(broj)

# Задача 3: Напиши програма која го прашува корисникот да внесе број и го креирај функција која 
# испишува збирот на сите броеви од 1 до внесениот број.
# def soberi_broevi(n: int):
#     zbir = 0

#     for i in range(1, n + 1):
#         zbir += i

#     return zbir


# broj = 28

# rezultat = soberi_broevi(broj)

# print(f"Zbirot od 1 do {broj} e {rezultat}")

# Задача 4: Напиши програма која го прашува корисникот да внесе текст и го креирај функција која
# испишува текстот во обратен редослед.

# def vnesi_tekst(tekst: str):
#     obratno = tekst[::-1]
#     print(f"vnesi_tekst: {obratno}")

# vnesi_tekst("nato")
# Задача 6: Напиши програма која прашува корисникот да внесе реченица и креирај функција 
# која го пресметува бројот на самогласки (a, e, i, o, u) во реченицата.
   

# def broi_samoglaski(rechenica: str):
#     samoglaski = "aeiou"
#     brojac = 0

#     rechenica = rechenica

#     for bukva in rechenica:
#         if bukva in samoglaski:
#             brojac += 1

#     return brojac


# tekst =("kostadinka: ")

# rezultat = broi_samoglaski(tekst)

# print(f"Broj na samoglaski: {rezultat}")
        
# Задача 7: Напиши програма која прашува од корисникот да внесе реченица и креирај функција која
# го пресметува бројот на појавувања на секоја буква во реченицата. Игнорирај големината на буквите.

# def broi_bukvi(rechenica: str):
#     rechenica = rechenica.lower()
#     bukvi = {}

#     for bukva in rechenica:
#         if bukva .isalpha():  
#             if bukva  in bukvi:
#                 bukvi[bukva] += 1
#             else:
#                 bukvi[bukva] = 1

#     return bukvi


# tekst = input("Vnesi rechenica: ")

# rezultat = broi_bukvi(tekst)

# for bukva, broj in rezultat.items():
#     print(f"{bukva}: {broj}")


# Задача 8: Напиши програма која прашува од корисникот да внесе низа од броеви сè додека
# не внесе негативен број. креирај функција која ќе го спечати го збирот на позитивните 
# броеви што биле внесени.

# def pecati_zbir(zbir):
#     print(f"zbirot na pozitivni broevi e {zbir} ")

# zbir = 0

# while True:
#     broj = int(input("vnesi broj (negativen za kraj): "))

#     if broj < 0:
#         break

#     zbir += broj

# pecati_zbir(zbir)

# БОНУС: Напиши програма која генерира листа со случајни броеви помеѓу 1 и 100. 
# Испечати го најголемиот број во листата

import random
lista = []

for i in range(10):
    broj = random.randint(1, 100)
    lista.append(broj)

print("lista:", lista)
najgolem = max(lista)

print("najgolemiot e :", najgolem)