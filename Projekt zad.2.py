lista1 = [1,2,3,4]
lista2 = [2,4,6,8]
def mnozenie_list(lista1, lista2):
    lista3 = []
    for i in range(len(lista1)):
        lista3.append(lista1[i]*lista2[i])
    return lista3

print(mnozenie_list(lista1, lista2))

lista4 = [3,4,5,6,7]
lista5 = [5,6,7,8,9]
print(mnozenie_list(lista4, lista5))

lista7 = [1,2,3]
lista8 = [2,3,4]
print(mnozenie_list(lista7, lista8))
