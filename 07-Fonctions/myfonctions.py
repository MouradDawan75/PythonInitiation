def somme_liste(entiers:list[int]) -> int:

    s = 0
    for i in entiers:
        s += i

    return s


def moyenne_liste(entiers:list[int]) -> float:
    s = somme_liste(entiers)
    nb_elements = 0
    for e in entiers:
        nb_elements += 1

    return s / nb_elements

def table_multipication(nombre, premier_multiple, dernier_multiple):
    for i in range(premier_multiple, dernier_multiple + 1):
        print(f"{nombre} x {i} = {nombre * i}")


def table_multipication_avec_while(nombre, premier_multiple, dernier_multiple):
    i = 0
    while True:
        print(f"{nombre} x {premier_multiple + i} = {nombre * (premier_multiple + i)}")
        i += 1
        if i == dernier_multiple:
            break

def table_multipication_avec_while_finie(nombre, premier_multiple, dernier_multiple):
    i = 0
    while i < dernier_multiple:
        print(f"{nombre} x {premier_multiple + i} = {nombre * (premier_multiple + i)}")
        i += 1


if __name__ == '__main__':

    print(somme_liste([1,2]))
    print(moyenne_liste([1,2]))