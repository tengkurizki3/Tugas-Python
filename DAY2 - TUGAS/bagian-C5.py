jam_masuk = int(input("Jam masuk      : "))
menit_masuk = int(input("Menit masuk    : "))
jam_keluar = int(input("Jam keluar     : "))
menit_keluar = int(input("Menit keluar   : "))

total_masuk = (jam_masuk * 60) + menit_masuk
total_keluar = (jam_keluar * 60) + menit_keluar

lama_menit = (total_keluar - total_masuk) % 1440

tampil_jam = lama_menit // 60
tampil_menit = lama_menit % 60

jam_ditagih = (lama_menit + 59) // 60

tarif_normal = 3000 + ((jam_ditagih - 1) * 2000)

is_maksimal = tarif_normal > 20000
total_tarif = (tarif_normal * (not is_maksimal)) + (20000 * is_maksimal)

# hasil
print("Lama parkir  :", tampil_jam, "jam", tampil_menit, "menit")
print("Jam ditagih  :", jam_ditagih)
print("Total tarif  : Rp", total_tarif)