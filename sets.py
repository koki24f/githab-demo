#sets- nemoze da imame duplikati, ne moze da pristapuvame do odredeni podatoci
x_sets={"ponedelnik",1,2,3,4,"python","ovoshje","ponedelnik","True",3.14}
print(x_sets)
#print (x_sets[0])==neznam cekam odgovor
x_sets.add("nov element")
print(x_sets)
x_sets.remove(3.14)
print(x_sets)

lista_duplikati=[1,1,1,2,33,102,11,11,13,102]
set_diplikati=set(lista_duplikati)
lista_cisti=lista_duplikati
print(lista_cisti)