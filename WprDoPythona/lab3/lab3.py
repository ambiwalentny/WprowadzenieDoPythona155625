#zadanie 1
import string

lista = [x for x in range(1,11)]
listaNowa = lista[5:]
lista = lista [:5]
print(f"lista oryginalna: {lista}, lista nowa: {listaNowa}")


#zadanie 2
listaPelna = lista + listaNowa
listaPelna.insert(0,0)
listaKopia = listaPelna.copy()
listaKopia.sort(reverse=True)
print(f"kopia połączonej listy, ułożona malejąco: {listaKopia}")

#zadanie3
zdanie = "Lorem ipsum dolor sit amet, consectetur adipiscing elit." #input("Podaj zdanie: ")
litery = set(zdanie.lower())
litery = [x for x in litery if x.isalpha()]
litery = sorted(litery)
print(f"Podane zdanie: {zdanie}\nNiepowatarzalne litery ułżone alfabetycznie: ", ' '.join(litery))

#zadanie 4
miesiacePL = {
    1: 'styczeń',
    2: 'luty',
    3: 'marzec',
    4: 'kwiecień',
    5: 'maj',
    6: 'czerwiec',
    7: 'lipiec',
    8: 'sierpień',
    9: 'wrzesień',
    10: 'październik',
    11: 'listopad',
    12: 'grudzień'
}


#zadanie 5
miesiaceENG = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}
miesiace = {
    'PL': miesiacePL,
    'ENG': miesiaceENG
}
print(miesiace['ENG'][4], miesiace['PL'][4])

#zadanie 6
imie = 'Marianna'#input("Podaj imię")
slownik = dict.fromkeys(set(imie),1)
print(slownik)

#zadanie 7
zdanieZad7 = input("podaj zdanie")

maleLitery = [x for x in zdanieZad7.lower() if x in string.ascii_letters]
maleLiteryProcenty = (len(maleLitery)/len(zdanieZad7))*100
print(len(zdanieZad7))
liczby = [x for x in zdanieZad7.lower() if x in string.digits]
liczbyProcenty = (len(liczby)/len(zdanieZad7))*100
print(f"Liczba znaków pokrywająca się string.ascii_lowercase {len(maleLitery)}, odpowiada to {maleLiteryProcenty:.2f}% zdania")
print(f"Liczba znaków pokrywająca się string.digits {len(liczby)}, odpowiada to {liczbyProcenty:.2f}% zdania")
