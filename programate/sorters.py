def sorter_v1(lista: list):
    """
    Ordena de mayor a menor una lista dada 'lista'.
    :param lista:
    :return lista_ordenada:
    """
    n = len(lista)
    int_cam = False
    while int_cam == False :
        for i in range(0, n-1):
            if lista[i+1] < lista[i]:
                int_cam = True
                var = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = var
        if int_cam == True:
            int_cam = False
        else:
            int_cam = True
    return lista


def sorter_v2(lista: list):
    """
    Ordena de mayor a menor una lista dada 'lista'.
    :param lista:
    :return lista_ordenada:
    """
    n = len(lista)
    for i in range(0, n, 1):
        for j in range(i, n, 1):
            if lista[i] > lista[j]:
                var = lista[i]
                lista[i] = lista[j]
                lista[j] = var
    return lista


#CREADO POR MI.
def sorter_jj(lista: list):
    length = len(lista)
    sorted_list = []
    for i in range(0, length):
        minimum = min(lista)
        sorted_list.append(minimum)
        lista.remove(minimum)
    return sorted_list


def sorter_v3(lista: list, start = 1, end = None):
    if end == None:
        end = len(lista)
    for i in range(start, end):
        j = i-1
        if lista[i] < lista[i-1]:
            var = lista[i]
            lista[i] = lista[i - 1]
            lista[i - 1] = var
        while(j>=1) and (lista[j-1]>lista[j]):
            var = lista[j-1]
            lista[j-1] = lista[j]
            lista[j] = var
            j = j - 1
    return lista



def inside(lista: list, beginin: int, end: int):
    i = beginin - 1
    pivote = lista[end - 1]
    for j in range(beginin,end):
        if lista[j] <= pivote:
            i = i + 1
            lista[i], lista[j] = lista[j], lista[i]
    return i


def sorter_v4(lista: list, inicio: int, fin: int):
     if fin > inicio:
         p = inside(lista, inicio, fin)
         sorter_v4(lista, inicio, p)
         sorter_v4(lista, p+1, fin)


def sorter_v4a(lista: list, final):
    p = -1
    l = len(lista)
    if final >= 0:
        for i in range(0, final+1):
            if lista[i] <= lista[final]:
                p = p +1
                lista[i], lista[p] = lista[p], lista[i]
            piv = p
        return sorter_v4a(lista[0: piv+1], piv-1)+sorter_v4a(lista[piv+1:], l-2-piv)
    if final <= 0:
        return lista

#print(sorter_v1([99, 2, 0, 4, 7, 9]))
#print(sorter_v2([99, 2, 0, 4, 7, 9]))
#print(sorter_jj([99, 2, 0, 4, 7, 9,88,2]))
#print(sorter_v3([110,44,38,5,47,27,2,46,19,16]))
print(sorter_v4([3,44,38,5,47,27,2,46,19,16]))

