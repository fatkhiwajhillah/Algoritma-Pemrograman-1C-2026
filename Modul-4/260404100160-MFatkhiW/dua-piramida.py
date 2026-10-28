while True:
    n = int(input("Masukkan angka (bilangan bulat positif): "))
    if n <= 0:
        print("Bilangan tidak boleh nol atau negatif, ulangi.")
    else:
        break

spasi = 4

for i in range(1, n + 1):

    for k in range(1, i + 1):
        print(k, end=" ")

    for j in range(n - i):
        print(" ", end=" ")

    for s in range(spasi):
        print(" ", end=" ")

    for j in range(n - i):
        print(" ", end=" ")

    for k in range(i, 0, -1):
        print(k, end=" ")

    print()