
########################################
##############  Zadanie1  ##############
########################################
def Zadanie1():
    linia = input("podaj linię danych rozdzielonych separatorem: ")
    separatorWejsciowy = input("podaj wejściowy separator: ")
    separatorWyjsciowy = input("podaj wyjściowy separator: ")
    liniaPodzielona = linia.split(separatorWejsciowy)
    wynik = separatorWyjsciowy.join(liniaPodzielona)
    print(wynik)


#zadanie można uprościć stosując metodę replace() zamiast split i join
def Zadanie1_2():
    linia = input("podaj linię danych rozdzielonych separatorem: ")
    separatorWejsciowy = input("podaj wejściowy separator: ")
    separatorWyjsciowy = input("podaj wyjściowy separator: ")
    wynik = linia.replace(separatorWejsciowy, separatorWyjsciowy)
    print(wynik)


########################################
##############  Zadanie2  ##############
########################################

zadanie2 = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"

########################################
##############  Zadanie3  ##############
########################################

def Zadanie3(litera_1, litera_2):
    liczba_liter1 = zadanie2.lower().count(litera_1)
    liczba_liter2 = zadanie2.lower().count(litera_2)
    print(f"W tekście jest {liczba_liter1} liter {litera_1} oraz {liczba_liter2} liter {litera_2}")

imie = "Tomasz"
nazwisko = "Rudziński"

Zadanie3(imie[2], nazwisko[3])


########################################
##############  Zadanie4  ##############
########################################