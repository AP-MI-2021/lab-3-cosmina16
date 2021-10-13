def citire_lista():
    result_list = []
    dimensiune = int(input("Dimensiune lista "))
    while dimensiune:
        element = int(input('introduceti un element'))
        result_list.append(element)
        dimensiune -=1
    return result_list


def numar_cifre_prime(n):
    """
    Verifica daca un nr e format doar din cifre prime
    :param n: intreg
    :return: true daca e doar din cifre prime,false altfel
    """
    while n:
        if (n%10 == 2 or n%10==3 or n%10==5 or n%10==7):
            n//=10
        else:
            return False
    return True

def test_numar_cifre_prime():
    assert numar_cifre_prime(33) == True
    assert numar_cifre_prime(11) == False


def all_prime(lista):

    for i in lista:
        if not numar_cifre_prime(i):
            return False
    return True



def get_longest_prime_digits(lista):

    lista_secvente = []
    for start in range (0, len(lista)):
        for end in range(start+1, len(lista)+1):
             if all_prime(lista[start:end]):
                 lista_secvente.append(lista[start:end])
    max_sec = []
    for secventa in lista_secvente:
        if len(secventa)>len(max_sec):
            max_sec = secventa

    return max_sec

def test_get_longest_prime_digits():
    assert get_longest_prime_digits([33,55,355]) == [33, 55,355]
    assert get_longest_prime_digits([22,33,55,11,66,77,55]) == [22 ,33, 55]

def semne_alternante(i,n):
    """
    Verifica daca doua numere au semne alternante
    :param i: un nr intreg
    :param n: un nr intreg
    :return: true - daca doua numere au semne alternante ; false -daca doua numere au semne alternante
    """
    if (i<0 and n>0) or (i>0 and n<0):
        return True
    return False


def all_semne_alternante(lista):

    for i in range(len(lista)-1):
        if not semne_alternante(lista[i],lista[i+1]):
            return False
    return True

def get_longest_alternating_signs(lista):

    lista_secvente = []
    for start in range (0, len(lista)):
        for end in range(start+1, len(lista)+1):
             if all_semne_alternante(lista[start:end]):
                 lista_secvente.append(lista[start:end])
    max_sec = []
    for secventa in lista_secvente:
        if len(secventa)>len(max_sec):
            max_sec = secventa

    return max_sec

def test_get_longest_alternating_signs():
    assert get_longest_alternating_signs([-33,55,-355]) == [-33, 55,-355]
    assert get_longest_alternating_signs([-22,33,-55,-11,-66,77,55]) == [-22 ,33,-55]


def main():
    stop = False
    lista = []
    while not stop:
        print ("""
        1 Citire lista 
        2 afisare numere semne alternate
        3 afiseaza numere doar din cifre prime
        x Exit
        """)
        command = input("alege comanda ")
        if command == 'x':
            stop = True
        elif command == '1':
            lista = citire_lista()
        elif command == '2':
            test_get_longest_alternating_signs()
            lista_semne_alt = get_longest_alternating_signs(lista)
            print(lista_semne_alt)
        elif command == '3':
            test_numar_cifre_prime()
            test_get_longest_prime_digits()
            lista_cifreprime = get_longest_prime_digits(lista)
            print(lista_cifreprime)

if __name__ == "__main__":
    main()