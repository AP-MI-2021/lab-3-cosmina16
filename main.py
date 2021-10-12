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
    :return: true daca
    """
    while n:
        if (n%10 == 2 or n%10==3 or n%10==5 or n%10==7):
            n//=10
        else:
            return False
    return True

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
    assert get_longest_prime_digits
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
        elif command == '3':
            lista_cifreprime = get_longest_prime_digits(lista)
            print(lista_cifreprime)

if __name__ == "__main__":
    main()