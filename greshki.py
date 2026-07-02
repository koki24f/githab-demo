#try....except/ try .....catch
try:
    #print(100/0)
#     broj1=int(input("vnsei broj 1:"))
#     broj2=int(input("vnesi broj 2:"))
#     zbir= broj1/broj2
#     print(zbir)
# except ZeroDivisionError:
#     print("nemoze da se deli so nula!!!")

# print(100/0)
    broj1=int(input("vnsei broj 1:"))
    broj2=int(input("vnesi broj 2:"))
    zbir= broj1/broj2
    print(zbir)
except:
    raise ValueError ("vnesovte loshi podatoci")