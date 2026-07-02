#index=value

x_dic={
    "ime":"stojan",
    "prezime":"Stojanov",
    "pol":"mashki",
    "email":["mail1@example.com","mail2@example.com"],
    "tel_broj":{
        "pribaten":"07000000",
        "sluzben":"07800000",
    }
}
print(x_dic["ime"])
print(f"{x_dic["ime"]},{x_dic['prezime']},{x_dic["pol"]}")
print(x_dic["tel_broj"])
print(x_dic["email"][0])
      
print(type(x_dic["email"]))

#x_dic["grad"]="skopje" # da dodademe eden element
#x_dic.update({"grad":"skopje","prezime":"Jovanov"})

#brishenje
# x_dic.pop("pol")
# del x_dic


for index in x_dic.keys():
    print(x_dic[index])
      
      
for value in x_dic.values():  
    print(value)
  

for index, value in x_dic.items():
    print("------------------")
    print(index)
    print(value)
    print ('---------')


# korisnik = {
#     "ime":"Kostadinka",
#     "prezime":"Trajanova",
#     "godini":20
# }

# if korisnik["godini"]>=18:
#     korisnik["dali e polnoleten"]="da"
# else:
#     korisnik["dali e polnoleten"]="ne"  
# print(korisnik)      

# broevi = {}

# broevi["broj1"] = int(input("Vnesi prv broj: "))
# broevi["broj2"] = int(input("Vnesi vtor broj: "))

# broevi["sobiranje"] = broevi["broj1"] + broevi["broj2"]
# broevi["odzemanje"] = broevi["broj1"] - broevi["broj2"]
# broevi["mnozenje"] = broevi["broj1"] * broevi["broj2"]
# broevi["delenje"] = broevi["broj1"] / broevi["broj2"]

# print("\nRezultati:")
# print(f"Broj 1: {broevi['broj1']}")
# print(f"Broj 2: {broevi['broj2']}")
# print(f"+: {broevi['sobiranje']}")
# print(f"-: {broevi['odzemanje']}")
# print(f"*: {broevi['mnozenje']}")
# print(f"/: {broevi['delenje']}")