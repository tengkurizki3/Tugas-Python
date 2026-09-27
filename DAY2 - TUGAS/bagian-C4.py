tugas = float(input("Nilai tugas       : "))
uts = float(input("Nilai UTS         : "))
uas = float(input("Nilai UAS         : "))
kehadiran = float(input("Kehadiran (%)     : "))
penghasilan = int(input("Penghasilan ortu  : "))
sertifikat = int(input("Jumlah sertifikat : "))

nilai_akhir = (20 * tugas + 35 * uts + 45 * uas) / 100

input_valid = (0 <= tugas <= 100) and (0 <= uts <= 100) and (0 <= uas <= 100) and (0 <= kehadiran <= 100)

is_layak = (
    input_valid and 
    (nilai_akhir >= 80) and 
    (kehadiran >= 85) and 
    (tugas >= 65) and (uts >= 65) and (uas >= 65) and 
    (penghasilan < 4000000 or sertifikat >= 2)
)

status = ("TIDAK " * (not is_layak)) + "LAYAK"

# hasil
print("Nilai akhir :", nilai_akhir)
print("Input valid :", input_valid)
print("Status      :", status)