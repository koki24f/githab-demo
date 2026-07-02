# keep your code dry-do not repeat

# def pechati_zdravo():
#     print("zdravo od funkcija")


def soberi_broevi(broj1:int,broj2:int,broj3:int=1):
    """
    dokumntaicjata za funkcijata soberi_broevi. prima 2 zadolzitelni i eden nezadolzitelen
    ako ne dadenme vrednost za broj 3 ke zeme defalt 1

    """
    zbir=(broj1+broj2)*broj3
    return zbir 
    print(f"zbirot e {zbir}")
broj1=28
broj2=12
zbir=soberi_broevi(broj1=broj1,broj2=broj2)   

print(f"zbirot od funkcijat e {zbir}")
# pechati_zdravo()
# pechati_zdravo()

def pechati_zdravo(ime):
    print(f"zdravo {ime}")
ime="kostadinka"  
pechati_zdravo(ime)
    
def pechati_ime(ime,godini):
    if godini >=18:
        print(f"{ime} e polnoleten")
    else:
        print(f"{ime}ne polnoleten")    

ime="Kostadinka"
godini=20
pechati_ime(ime,godini)
