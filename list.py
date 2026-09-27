list_nilai_ujian = [60, 40, 50, 30, 20, 90, 100]
list_nama_mahasiswa = ["bagja", "budi", "candra", "dewi", "eka", "fadhil", "gita"]

#Mengambil Data List
print("List Nilai Ujian : ", list_nilai_ujian)
print("List Nama Mahasiswa : ", list_nama_mahasiswa)
print("nama mahasiswa ke 1", list_nama_mahasiswa[6])
print("nilai mahasiswa ke 1", list_nilai_ujian[6])

#perulangan dengan For
for i in list_nama_mahasiswa:
    print("nama mahasiswa", i)

# mengedit data
list_nama_mahasiswa[0] = "Rendi"
print("nama mahasiswa ke 1", list_nama_mahasiswa[0])

#Tambah Data Yaitu Fungsi Append
list_nama_mahasiswa.append("Setiawan Ningsih")
print(list_nama_mahasiswa)

#Hapus Kita Gunakan Fungsi .remove
list_nama_mahasiswa.remove("budi")
print(list_nama_mahasiswa)
