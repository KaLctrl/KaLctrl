def tambah_kursus(nama, deskripsi):
    kursus = {"nama": nama, "deskripsi": deskripsi, "materi": [], "tes": []}
    courses.append(kursus)
    return kursus

def kelola_kursus():
    for i, kursus in enumerate(courses):
        print(f"{i+1}. {kursus['nama']}")

def tambah_pengumuman(nama_kursus, pengumuman):
    for kursus in courses:
        if kursus["nama"] == nama_kursus:
            kursus["pengumuman"].append(pengumuman)
            return
    print("Kursus tidak ditemukan")

def kelola_pengguna():
    for i, pengguna in enumerate(users):
        print(f"{i+1}. {pengguna['username']}")

def tambah_pengguna(username, password):
    pengguna = {"username": username, "password": password, "kursus_terdaftar": []}
    users.append(pengguna)
    return pengguna

def daftar_kursus(username, nama_kursus):
    for pengguna in users:
        if pengguna["username"] == username:
            for kursus in courses:
                if kursus["nama"] == nama_kursus:
                    pengguna["kursus_terdaftar"].append(kursus)
                    return
            print("Kursus tidak ditemukan")
            return
    print("Pengguna tidak ditemukan")

def lihat_materi_kursus(username, nama_kursus):
    for pengguna in users:
        if pengguna["username"] == username:
            for kursus in pengguna["kursus_terdaftar"]:
                if kursus["nama"] == nama_kursus:
                    for materi in kursus["materi"]:
                        print(materi)
                    return
            print("Kursus tidak ditemukan")
            return
    print("Pengguna tidak ditemukan")

def ikuti_tes(username, nama_kursus, nama_tes):
    for pengguna in users:
        if pengguna["username"] == username:
            for kursus in pengguna["kursus_terdaftar"]:
                if kursus["nama"] == nama_kursus:
                    for tes in kursus["tes"]:
                        if tes["nama"] == nama_tes:
                            # Simulasi proses mengerjakan tes
                            print("Anda telah mengikuti tes!")
                            return
                    print("Tes tidak ditemukan")
                    return
            print("Kursus tidak ditemukan")
            return
    print("Pengguna tidak ditemukan")

def main():
    while True:
        print("Selamat datang di Kursus Online Haikal!")
        print("1. Login Admin")
        print("2. Login Pengguna")
        print("3. Keluar")
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            login_admin()
        elif pilihan == "2":
            login_pengguna()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid")

def login_admin():
    username = input("Masukkan username admin: ")
    password = input("Masukkan password admin: ")

    if username == "Haikal" and password == "password":
        while True:
            print("Dasbor Admin")
            print("1. Tambah Kursus")
            print("2. Kelola Kursus")
            print("3. Kelola Pengguna")
            print("4. Tambah Pengumuman")
            print("5. Logout")
            pilihan = input("Masukkan pilihan Anda: ")

            if pilihan == "1":
                nama = input("Masukkan nama kursus: ")
                deskripsi = input("Masukkan deskripsi kursus: ")
                tambah_kursus(nama, deskripsi)
            elif pilihan == "2":
                kelola_kursus()
            elif pilihan == "3":
                kelola_pengguna()
            elif pilihan == "4":
                nama_kursus = input("Masukkan nama kursus: ")
                pengumuman = input("Masukkan pengumuman: ")
                tambah_pengumuman(nama_kursus, pengumuman)
            elif pilihan == "5":
                break
            else:
                print("Pilihan tidak valid")
    else:
        print("admin tidak valid")

def login_pengguna():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username == "Adis" and password == "password":
            while True:
                print("Dasbor Pengguna")
                print("1. Daftar Kursus")
                print("2. Lihat Materi Kursus")
                print("3. Ikuti Tes")
                print("4. Logout")
                pilihan = input("Masukkan pilihan Anda: ")

                if pilihan == "1":
                    nama_kursus = input("Masukkan nama kursus: ")
                    daftar_kursus(username, nama_kursus)
                elif pilihan == "2":
                    nama_kursus = input("Masukkan nama kursus: ")
                    lihat_materi_kursus(username, nama_kursus)
                elif pilihan == "3":
                    nama_kursus = input("Masukkan nama kursus: ")
                    nama_tes = input("Masukkan nama tes:")
                    ikuti_tes(username, nama_kursus, nama_tes)
                elif pilihan == "4":
                    break
                else:
                    print("Pilihan tidak valid")
            return
    print("pengguna tidak valid")

if __name__ == "__main__":
    main()