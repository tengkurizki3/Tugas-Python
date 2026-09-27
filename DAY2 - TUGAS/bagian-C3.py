tanggal = int(input("Tanggal : "))
bulan = int(input("Bulan   : "))
tahun = int(input("Tahun   : "))

is_kabisat = (tahun % 400 == 0) or ((tahun % 4 == 0) and (tahun % 100 != 0))

bulan_31 = (bulan == 1) or (bulan == 3) or (bulan == 5) or (bulan == 7) or (bulan == 8) or (bulan == 10) or (bulan == 12)
bulan_30 = (bulan == 4) or (bulan == 6) or (bulan == 9) or (bulan == 11)
bulan_februari = (bulan == 2)

jumlah_hari = (31 * bulan_31) + (30 * bulan_30) + ((28 + is_kabisat) * bulan_februari)

is_tanggal_valid = 1 <= tanggal <= jumlah_hari

print("Tahun kabisat :", is_kabisat)
print("Jumlah hari   :", jumlah_hari)
print("Tanggal valid :", is_tanggal_valid)