
# Problem: Write a program to count how many times a specific element appears in a list.

# Ask the user to input which number wants to count how many times is in the list
# Display the result.
       
       


broevi = []
brojach = int(input("broj na broevi "))

for i in range(brojach):
    broj = int(input("vnesi brij: "))
    broevi.append(broj)

target = int(input("koj broj da se prebroi"))
count = broevi.count(target)

print(f"brojot  {target} se pojavuva  {count} kolku pati vo listata")

# #2. Filter Even and Odd Numbers
# Problem: Write a program that separates a list into even and odd numbers.

# Use a loop to ask the user to input 10 numbers and add them to a list.
# Use a loop to iterate through the list and separate even and odd numbers into two new lists.
# Display the even numbers and odd numbers.

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

# 3. Calculate the Average of a List
# Problem: Write a program to calculate the average of a list of numbers.

# Ask the user to input a list of numbers.
# Use a loop to calculate the sum of the numbers.
# Divide the sum by the total number of elements to get the average.
# Display the result


broevi=[]
broj_na_broevi= int(input("broj na broevi"))
for i in range(broj_na_broevi):
    broj=int(input("vnesi broj:"))
    broevi.append (broj)
    zbir=sum(broevi)
    for broj in broevi:
        prosek=zbir/broj_na_broevi
print(f"suma {zbir}") 
print (f"proseok {prosek}")  

# 4. Remove Duplicates from a List
# Problem: Write a program to remove duplicate elements from a list.

# Ask the user to input a list of numbers.
# Display the list without duplicates.
lista_broevi=[]
broj_na_vneseni_broevi=int(input("broj na vneseni brovi: "))
for i in range (broj_na_vneseni_broevi):
    broj=int(input("vnesi broj"))
    lista_broevi.append(broj)
lista_bez_duplikati=[]
for broj in lista_broevi:
    if broj not in lista_bez_duplikati:
        lista_bez_duplikati.append(broj)
print(f"cela lista {lista_broevi}")
print(f"lista bez duplikati {lista_bez_duplikati}")


# 5. Shopping List Manager
# Problem: Write a program to manage a list of items to buy.

# Start with an empty list.
# Use a loop to ask the user to input the product and the price
# Store the product in the list (Bonus if you store the price in another list
# Display the final list and how much the user has to pay.


proizvodi=[]
ceni =[]
broj_na_proizvodi=int(input('broj na prozivodi'))
for i in range(broj_na_proizvodi):

    proizvod=input("proizvod: ")
    cena=int(input("cena:"))
    proizvodi.append(proizvod)
    ceni.append(cena)
vkupno=sum(ceni)  
print(f"lista na proizvodi {proizvodi}")
print(f"ceni na proizvodi {ceni}")
print(f"vkupno za plakanje {vkupno}")