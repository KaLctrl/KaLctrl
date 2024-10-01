#Nama: Muh Haikal Adis Yafiq
#Nim: 2409116035
#Kelas: A
while True:
    # input nama dan Nim
    nama = str(input("Masukkan Nama Anda: "))
    nim = int(input("Masukkan Nim Anda: "))
    # Input jam kerja dan tarif kerja
    jam_kerja = float(input("Masukkan jumlah jam kerja: "))
    tarif_kerja = float(input("Masukkan tarif kerja per jam: "))

    # Menghitung gaji
    gaji = jam_kerja * tarif_kerja

    # Cek apakah jam kerja lebih dari 160 untuk bonus 10%
    if jam_kerja > 160:
        bonus = 0.1 * gaji
        gaji_total = gaji + bonus
        print(f"Anda mendapat bonus 10% sebesar: {bonus}")
    else:
        gaji_total = gaji
        print("Anda tidak mendapat bonus.")

    print(f"Gaji total Anda: {gaji_total}")

    # Perulangan untuk mengulang atau keluar
    pilihan = input("Apakah Anda ingin menghitung gaji lagi? (ya/tidak): ").lower()
    if pilihan != "ya":
        print("Terima kasih! Program selesai.")
        break
