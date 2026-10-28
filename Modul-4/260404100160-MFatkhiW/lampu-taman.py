while True:
    jumlah_baris_lampu = int(input("Masukkan jumlah baris lampu (bilangan bulat positif): "))
    jumlah_lampu = int(input("Masukkan jumlah lampu (bilangan bulat positif): "))
    if jumlah_baris_lampu <= 0 or jumlah_lampu <= 0:
        print("Bilangan tidak boleh nol atau negatif, ulangi.")
    else:
        break

ada_gangguan = False

for i in range(1, jumlah_baris_lampu + 1):
    print(f"Baris Lampu ke-{i}")
    for j in range(1, jumlah_lampu + 1):
        if j % 3 == 0:
            print(f"Lampu {j} mengalami gangguan")
            ada_gangguan = True
        else:
            print(f"Lampu {j} berfungsi normal") 

if ada_gangguan:
    print("Lampu mengalami gangguan, periksa sumber listrik utama taman!")
else:
    print("Semua lampu normal, sumber listrik utama taman aman.")