# Zadanie 1
zadanie1_liczba1 = int(12.34)
zadanie1_liczba2 = int('1111011', 2)

zadanie1_liczba3 = float("12.34")
zadanie1_liczba4 = float(1234)
print("    zadanie 1")
print(f"liczby po przekształceniu: \n na int {zadanie1_liczba1}  {zadanie1_liczba2}\n na float {zadanie1_liczba3} {zadanie1_liczba4}\n")
# Zadanie 2
# metoda
zadanie2_liczba1 = 2047 #binarnie 0111 1111 1111,sumując jedynki wynik jest równy 11
zadanie2_liczba1_bitCount = zadanie2_liczba1.bit_count()

zadanie2_liczba2 = 2048 #binarnie 1000 0000 0000, sumując jedynki wynik jest równy 1
zadanie2_liczba2_bitCount = zadanie2_liczba2.bit_count()
print("    zadanie 2")
print("metoda bit_count()")
print(f"suma bitów liczby {zadanie2_liczba1} wynosi {zadanie2_liczba1_bitCount}\nsuma bitów liczby {zadanie2_liczba2} wynosi {zadanie2_liczba2_bitCount}\n ")
print("metoda is_integer()")
zadanie2_liczby = [1.003, 3.73, 12.0, 13.43, 28.0]
for x in zadanie2_liczby:
    if not x.is_integer():
        print(f"liczba {x} nie jest całkowita")
    else:
        print(f"liczba {x} jest całkowita")




# Zadanie 3
#1. sprawdzanie parzystości liczby
print("\n    zadanie 3")
print("1. sprawdzanie parzystości liczby")
zadanie3_liczba1 = 8


if zadanie3_liczba1 & 1:
    print(f"liczba {zadanie3_liczba1} jest nieparzysta")
else:
    print(f"liczba {zadanie3_liczba1} jest parzysta")

#2. sprawdzanie czy dwa zbiory są rozłączne
print("\n2. sprawdzanie czy dwa zbiory są rozłączne")
zadanie3_zbior1 = {1, 2, 3}
zadanie3_zbior2 = {4, 5, 6}
if zadanie3_zbior1 & zadanie3_zbior2:
    print(f"zbiory {zadanie3_zbior1} i {zadanie3_zbior2} mają część wspólną")
else:
    print(f"zbiory {zadanie3_zbior1} i {zadanie3_zbior2} są rozłączne")

#3. sprawdzanie równości dwóch liczb
print("\n3. sprawdzanie równości dwóch liczb")
zadanie3_liczba3 = 12
zadanie3_liczba4 = 32

if zadanie3_liczba3 ^ zadanie3_liczba4 == 0:
    print(f"liczby {zadanie3_liczba3} i {zadanie3_liczba4} są równe")
else:
    print(f"liczby {zadanie3_liczba3} i {zadanie3_liczba4} nie są równe")

#4. zliczanie bitów potrzebnych do przedstawienia liczby
print("\n4. zliczanie bitów potrzebnych do przedstawienia liczby")
zadanie3_liczba5 = 2047

tmp = 0
while zadanie3_liczba5 > 0:
    tmp += 1
    zadanie3_liczba5 = zadanie3_liczba5 >> 1
print(f"liczba {int(zadanie3_liczba5)} potrzebuje {tmp} bitów do reprezentacji")