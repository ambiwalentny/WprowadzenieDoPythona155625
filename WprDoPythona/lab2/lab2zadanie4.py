a = 1357
b = 2468
c = 12345678901234567890
d = 12345678.12345
print(f"1. Wyrównanie do prawej strony z wypełnieniem spacjami\n{a:>10} {b:>10}")
print(f"2. Wyrównanie do lewej strony z wypełnieniem spacjami\n{a:<10} {b:<10}")
print(f"3. Wyrównanie do prawej strony z wypełnieniem zerami\n{a:0>10} {b:0>10}")
print(f"4. Liczba z separatorem tysięcy\n {c:,}")
print(f"5. Liczba z separatorem tysięcy i dokładnością do 2 miejsc po przecinku\n {d:,.2f}")
