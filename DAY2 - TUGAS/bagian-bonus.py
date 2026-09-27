b1 = int(input("Bilangan 1: "))
b2 = int(input("Bilangan 2: "))
b3 = int(input("Bilangan 3: "))

max_b1_b2 = (b1 * (b1 >= b2)) + (b2 * (b1 < b2))
min_b1_b2 = (b1 * (b1 <= b2)) + (b2 * (b1 > b2))


terbesar = (max_b1_b2 * (max_b1_b2 >= b3)) + (b3 * (max_b1_b2 < b3))
terkecil = (min_b1_b2 * (min_b1_b2 <= b3)) + (b3 * (min_b1_b2 > b3))


tengah = (b1 + b2 + b3) - terbesar - terkecil

is_aritmetika = (tengah - terkecil) == (terbesar - tengah)

# hasil
print("Terkecil           :", terkecil)
print("Tengah             :", tengah)
print("Terbesar           :", terbesar)
print("Barisan aritmetika :", is_aritmetika)