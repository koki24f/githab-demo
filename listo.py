# lista=[1,2,3,4,"python","ovoshje","ponedelnik",True,3.14]

# # print(lista)
# print(lista[4])
# print(lista[-1])
# print(lista[4:6])

#lista=["hemija","ovoshje","zelenchuk","meso","sokovi","alkohol","tekstil","elektrika","kabli","televizor"]
# print(lista[6])
# print(lista[-3])
# print(lista[1:7])

# lista.append("nov element")
# lista.append(2.333)
# lista[5]="jabolki"
# print(lista)
# lista=[1,2,3,4,"python","ovoshje","ponedelnik",True,3.14]
# lista.append("nov element")
# lista.insert(2,333)
# lista[5]="jabolki"
# print(lista)

# lista = []

# for i in range(6):
#     element = input("Vnesi element: ")
#     lista.append(element)

# print("Listata e:", lista)
# lista = []

# broj = int(input("Kolku elementi sakash da vnesesh? "))

# for i in range(broj):
#     element = input("Vnesi element: ")
#     lista.append(element)

# print("Listata e:", lista)

# #zadacha 2


# parni = []
# neparni = []

# for i in range(10):
#     broj = int(input("Vnesi broj: "))

#     if broj % 2 == 0:
#         parni.append(broj)
#     else:
#         neparni.append(broj)

# print("Parni broevi:", parni)
# print("Neparni broevi:", neparni)

# #zadacha 3
# oceni = []
# zbir = 0

# for i in range(5):
#     ocena = int(input("Vnesi ocena: "))
#     oceni.append(ocena)
#     zbir += ocena

# prosek = zbir / 5

# print("Oceni:", oceni)
# print("Prosekot e:", prosek)


# lista.remove("python") # koj sakame elenemnt
# lista.pop(5) # koja vrednos skalme da go izbrisheme prema indeks
# lista.pop() # go brishe posledniot vo listata
# lista.clear() # gi brishe site elementi vo listata a listata si postoi
# print (lista)

# lista_broevi=(1,2,3,4,5)
# for broj in lista_broevi:
#     dupliran_broj = broj *2
#     if dupliran_broj %2 ==0:
#         print(f"brojot {broj}  brojot pomnozen so 2 e paren")
#     else:
#         print(f"brojot {broj} e  brojot pomnozen so 2 eneparen")

#zadacha 1
# lista =[]
# broj = int(input("Kolku elementi sakash da vnesesh: "))

# for i in range(broj):
#      element = input("Vnesi element: ")
#      lista.append(element)
# print (f"listata e {lista}")

# #zadacha 2
parni=[]
neparni =[]

for brojach in range (10):
  broj=int(input("vnesi broj {brojach}: "))
  if broj %2==0:
    parni.append(broj)
    print (f"brojot e paren") 
  else:
    neparni.append(broj)   
    print("brojot e neparen")
print(f"parni broevi {parni}")
print (f"neparni broevi {neparni}")

# zadacha 3
# oceni=[]
# for i in range (5):
#     ocena = int(input("vnesi ocena :"))
#     oceni.append (ocena)
# prosek=sum(oceni)/5

# print (f"oceni na studentot {oceni}")
# print (f"prosek {prosek}")

lista=[1,2,3,4,"python","ovoshje","ponedelnik",True,3.14,3,4,4,3]
# br_na_4ki=lista.count("python")
# print(br_na_4ki)
# indexs_element=lista.index("python")
# print(indexs_element)
# dolzina_kolku_elemnti_ima=len(lista)
# lista.sort(reverse=) #defold(revers=)=ascemblinf, reverse=true-descembing
# print(lista)

# oceni=[]
# broj_na_ocena= int(input("broj na oceni"))
# for i in range(broj_na_ocena):
#     ocena=int(input("vnesi ocena:"))
#     oceni.append (ocena)
#     suma=0
#     for ocena in oceni:
#         suma+=ocena
#         prosek=suma/broj_na_ocena
#         broj_na_5ki=0
#         broj_na_4ki=0
#         for ocena in oceni:
#             if ocena ==5:
#                 broj_na_5ki+=1
#             elif ocena ==4:
#                 broj_na_4ki+=1
# print(f"broj na oceni na sutdento {oceni}")  
# print (f"proseok {prosek}")  
# print(f"broj na 5ki{broj_na_5ki }")        
# print(f"broj na 4ki{broj_na_4ki }")      

# oceni=[]
# broj_na_ocena= int(input("broj na oceni"))
# for i in range(broj_na_ocena):
#     ocena=int(input("vnesi ocena:"))
#     oceni.append (ocena)
#     suma=0
#     for ocena in oceni:
#         suma+=ocena
#         prosek=suma/broj_na_ocena
#         broj_na_5ki= oceni.count(5)
#         broj_na_4ki=oceni.count(4)
        
# print(f"broj na oceni na sutdento{ oceni}")  
# print (f"proseok {prosek}")  
# print(f"broj na 5ki;{broj_na_5ki}")        
# print(f"broj na 4ki,{broj_na_4ki}" )   