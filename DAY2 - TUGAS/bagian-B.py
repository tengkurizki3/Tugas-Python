n1 = float(input("Nilai 1: "))
n2 = float(input("Nilai 2: "))
n3 = float(input("Nilai 3: "))

rata = (n1 + n2 + n3) / 3
lulus = rata >= 75 and n1 >= 60 and n2 >= 60 and n3 >= 60

print("Rata-rata:", rata)
print("Lulus:", lulus)