total_belanja = int(input("Total belanja : "))
uang_dibayar = int(input("Uang dibayar  : "))

uang_cukup = uang_dibayar >= total_belanja

kekurangan = (total_belanja - uang_dibayar) * (not uang_cukup)

kembalian = (uang_dibayar - total_belanja) * uang_cukup

sisa = kembalian

p100 = sisa // 100000
sisa = sisa % 100000

p50 = sisa // 50000
sisa = sisa % 50000

p20 = sisa // 20000
sisa = sisa % 20000

p10 = sisa // 10000
sisa = sisa % 10000

p5 = sisa // 5000
sisa = sisa % 5000

p2 = sisa // 2000
sisa = sisa % 2000

p1 = sisa // 1000
sisa = sisa % 1000

p500 = sisa // 500
sisa = sisa % 500

total_lembar = p100 + p50 + p20 + p10 + p5 + p2 + p1 + p500

print("Uang cukup :", uang_cukup)
print("Kekurangan :", kekurangan)
print("Kembalian  :", kembalian)
print("Rp100.000  :", p100)
print("Rp50.000   :", p50)
print("Rp20.000   :", p20)
print("Rp10.000   :", p10)
print("Rp5.000    :", p5)
print("Rp2.000    :", p2)
print("Rp1.000    :", p1)
print("Rp500      :", p500)
print("Total lembar/keping :", total_lembar)