bilangan = int(input("Masukkan bilangan 5 digit: "))

is_valid = 10000 <= bilangan <= 99999

d5 = bilangan % 10             # d5 = 1 (digit ke-5/satuan)
d4 = (bilangan // 10) % 10     # d4 = 2 (digit ke-4/puluhan)
d3 = (bilangan // 100) % 10    # d3 = 7 (digit ke-3/ratusan) -> seperti petunjuk soal
d2 = (bilangan // 1000) % 10   # d2 = 0 (digit ke-2/ribuan)
d1 = bilangan // 10000         # d1 = 4 (digit ke-1/puluh ribuan)

jumlah_digit = d1 + d2 + d3 + d4 + d5

banyak_genap = (d1 % 2 == 0) + (d2 % 2 == 0) + (d3 % 2 == 0) + (d4 % 2 == 0) + (d5 % 2 == 0)

terbalik = (d5 * 10000) + (d4 * 1000) + (d3 * 100) + (d2 * 10) + d1

is_palindrom = bilangan == terbalik

is_harshad = (bilangan % jumlah_digit) == 0

# hasil
print("Input valid        :", is_valid)
print("Jumlah digit       :", jumlah_digit)
print("Banyak digit genap :", banyak_genap)
print("Bilangan terbalik  :", terbalik)
print("Palindrom          :", is_palindrom)
print("Bilangan Harshad   :", is_harshad)