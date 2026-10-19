jumlah_A = 0
jumlah_B = 0
jumlah_C = 0
jumlah_D = 0
jumlah_E = 0
total_nilai = 0
tertinggi = 0
nama_tertinggi = ""
terendah = 100
nama_terendah = ""

for i in range(1, 11):
    print("Mahasiswa ke-" + str(i))
    nama = input("Nama        : ")
    tugas = float(input("Nilai tugas : "))
    uts = float(input("Nilai UTS   : "))
    uas = float(input("Nilai UAS   : "))

    akhir = 0.3 * tugas + 0.3 * uts + 0.4 * uas

    if akhir >= 85:
        kategori = "A"
        jumlah_A += 1
    elif akhir >= 75:
        kategori = "B"
        jumlah_B += 1
    elif akhir >= 65:
        kategori = "C"
        jumlah_C += 1
    elif akhir >= 50:
        kategori = "D"
        jumlah_D += 1
    elif akhir < 50:
        kategori = "E"
        jumlah_E += 1

    print("-> " + nama + " | Tugas:", tugas, "| UTS:", uts, "| UAS:", uas,
          "| Akhir:", akhir, "| Kategori:", kategori)

    total_nilai += akhir
    if akhir > tertinggi:
        tertinggi = akhir
        nama_tertinggi = nama
    if akhir < terendah:
        terendah = akhir
        nama_terendah = nama

print("== REKAP KELAS ==")
print("Jumlah A:", jumlah_A)
print("Jumlah B:", jumlah_B)
print("Jumlah C:", jumlah_C)
print("Jumlah D:", jumlah_D)
print("Jumlah E:", jumlah_E)
print("Nilai akhir tertinggi:", tertinggi, "(" + nama_tertinggi + ")")
print("Nilai akhir terendah :", terendah, "(" + nama_terendah + ")")
print("Rata-rata nilai akhir:", total_nilai / 10)