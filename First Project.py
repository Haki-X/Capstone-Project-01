
data_bisnis = [
    {"id": 1, "nama": "Bakso Pak Joko", "kategori": "Kuliner", "alamat": "Jl. Tropodo No.12, Waru", "telepon": "081234567891", "jam_buka": "10:00 - 21:00"},
    {"id": 2, "nama": "Roti Bakar Enak", "kategori": "Kuliner", "alamat": "Jl. Letjen Sutoyo No.5, Waru", "telepon": "081212345678", "jam_buka": "08:00 - 22:00"},
    {"id": 3, "nama": "Apotek Sehat Selalu", "kategori": "Kesehatan", "alamat": "Jl. Sidosermo No.45, Waru", "telepon": "082112233445", "jam_buka": "07:00 - 22:00"},
    {"id": 4, "nama": "Klinik Medika Waru", "kategori": "Kesehatan", "alamat": "Jl. Tropodo Utara No.3, Waru", "telepon": "085711223344", "jam_buka": "08:00 - 20:00"},
    {"id": 5, "nama": "Bengkel Motor Maju", "kategori": "Otomotif", "alamat": "Jl. Raya Waru No.10", "telepon": "082333221100", "jam_buka": "08:00 - 17:00"},
    {"id": 6, "nama": "Cuci Mobil Bersih Kilat", "kategori": "Otomotif", "alamat": "Jl. Tropodo Selatan No.6", "telepon": "081366655544", "jam_buka": "07:00 - 18:00"},    
    {"id": 7, "nama": "Toko ATK Smart", "kategori": "Pendidikan", "alamat": "Jl. Tropodo Indah No.2", "telepon": "081234990011", "jam_buka": "08:00 - 20:00"},
    {"id": 8, "nama": "Bimbingan Belajar Pintar", "kategori": "Pendidikan", "alamat": "Jl. Waru Indah No.7", "telepon": "085799887766", "jam_buka": "14:00 - 20:00"},    
    {"id": 9, "nama": "Laundry Express Waru", "kategori": "Jasa", "alamat": "Jl. Letjen Sutoyo No.20", "telepon": "081265478932", "jam_buka": "08:00 - 21:00"},
    {"id": 10, "nama": "Jasa Fotokopi & Print", "kategori": "Jasa", "alamat": "Jl. Tropodo Barat No.1", "telepon": "082178654321", "jam_buka": "08:00 - 22:00"},
    {"id": 11, "nama": "Toko Baju Murah", "kategori": "Fashion", "alamat": "Jl. Tropodo No.19", "telepon": "081333224455", "jam_buka": "09:00 - 21:00"},
    {"id": 12, "nama": "Butik Anggun", "kategori": "Fashion", "alamat": "Jl. Waru Jaya No.8", "telepon": "082144556677", "jam_buka": "10:00 - 20:00"},
    {"id": 13, "nama": "Sablon Kaos Waru", "kategori": "Percetakan", "alamat": "Jl. Tropodo Tengah No.11", "telepon": "081299887766", "jam_buka": "08:00 - 17:00"},
    {"id": 14, "nama": "Digital Printing Waru", "kategori": "Percetakan", "alamat": "Jl. Tropodo Baru No.2", "telepon": "085611223344", "jam_buka": "08:00 - 19:00"},
    {"id": 15, "nama": "Toko Elektronik Makmur", "kategori": "Elektronik", "alamat": "Jl. Raya Tropodo No.5", "telepon": "081212345699", "jam_buka": "09:00 - 21:00"},
    {"id": 16, "nama": "Service HP & Laptop", "kategori": "Elektronik", "alamat": "Jl. Waru Tengah No.4", "telepon": "085799912345", "jam_buka": "09:00 - 18:00"},
    {"id": 17, "nama": "Toko Bahan Bangunan Subur", "kategori": "Bangunan", "alamat": "Jl. Letjen Sutoyo No.9", "telepon": "081256789034", "jam_buka": "07:00 - 17:00"},
    {"id": 18, "nama": "UD Konstruksi Jaya", "kategori": "Bangunan", "alamat": "Jl. Tropodo Raya No.18", "telepon": "082144556600", "jam_buka": "08:00 - 17:00"},
    {"id": 19, "nama": "Barbershop Bro & Co", "kategori": "Grooming", "alamat": "Jl. Tropodo Indah No.9", "telepon": "081234556677", "jam_buka": "10:00 - 20:00"},
    {"id": 20, "nama": "Salon Cantik Kita", "kategori": "Grooming", "alamat": "Jl. Waru Selatan No.6", "telepon": "082144778899", "jam_buka": "09:00 - 19:00"}
]





def menu():
    while True:
        header("📊 YELLOW PAGES DIGITAL UMKM Waru Sidoarjo")
        print("Silakan pilih menu yang kamu butuhkan:")
        print("1. 📋 Tampilkan data ")
        print("2. ✨ Tambah data baru")
        print("3. ✏️ Edit data")
        print("4. 🗑️ Hapus data")
        print("5. 🚪 Keluar dari program")
        pilihan = input("\nMasukkan pilihanmu (1-5): ")

        while True:
            pilihan = input("\nMasukkan pilihanmu (1-5): ").strip()
            if pilihan in ["1", "2", "3", "4", "5"]:
                break  
            print("⚠️  Pilihan nggak valid. Masukkan hanya angka 1 sampai 5 ya!")

        if pilihan == "1":
            tampilkan_data()
        elif pilihan == "2":
            tambah_data()
        elif pilihan == "3":
            edit_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            print("\n👋 Terima kasih sudah pakai program ini. Sampai jumpa lagi ya!\n")
            break


def cetak_tabel():
    print("-" * 115)
    print("{:<4} | {:<25} | {:<15} | {:<28} | {:<15} | {:<15}".format("ID", "Nama", "Kategori", "Alamat", "Telepon", "Jam Buka"))
    print("-" * 115)

def tampilkan_semua():
    if not data_bisnis:
        print("\n--- Belum ada data bisnis yang tersedia. ---\n")
        return 

    print("\n--- Berikut adalah daftar bisnis yang tersedia: ---\n") 
    cetak_tabel()
    for bisnis in data_bisnis:
        print("{:<4} | {:<25} | {:<15} | {:<28} | {:<15} | {:<15}|".format(
            bisnis["id"], bisnis["nama"], bisnis["kategori"], bisnis["alamat"], bisnis["telepon"], bisnis["jam_buka"]))

    print()

def header(judul):
    print("\n" + "=" * 70)
    print(judul.center(70))
    print("=" * 70)
    print()

def navigasi_setelah_aksi():
    while True:
        jawab = input("🔄 Kembali ke menu utama? (y/n): ").lower()
        if jawab == "y":
            print("\n➡️ Menu utama akan ditampilkan...\n")
            break 
        elif jawab == "n":
            keluar = input("❓ Apakah kamu ingin keluar dari program? (y/n): ").lower()
            if keluar == "y":
                print("\n👋 Sampai jumpa! Terima kasih telah menggunakan aplikasi ini.\n")
                exit()
            elif keluar == "n":
                print("\n😊 Baik, kamu bisa memilih menu lagi.\n")
                break  
            else:
                print("⚠️ Jawaban tidak dikenali. Ketik 'y' atau 'n'.")
        else:
            print("⚠️ Jawaban tidak dikenali. Ketik 'y' atau 'n'.")
    
def tampilkan_data():
    header("📋 YELLOW PAGES Digital UMKM Waru - Sidoarjo")
    if not data_bisnis:
        print("Ups, belum ada data bisnis yang tersedia!\n")
        return
    print("1. Tampilkan semua data")
    print("2. Tampilkan berdasarkan kategori")
    print("3. Tampilkan menu berdasarkan nama bisnis")

    while True:
        try:
            pilih_menu = int(input("Masukkan pilihan nomor menu: "))
            break
        except ValueError:
            print("Mohon masukkan pilihan berupa angka!")

    if pilih_menu == 1:
        tampilkan_semua()
        navigasi_setelah_aksi()

    elif pilih_menu == 2:
        print("-" * 30)
        print("Pilih Kategori:")
        kategori_unik = sorted(list(set(bisnis["kategori"] for bisnis in data_bisnis)))
        if not kategori_unik:
            print("Tidak ada kategori unik yang tersedia.")
            navigasi_setelah_aksi()
            return
        
        for i, kategori in enumerate(kategori_unik): 
            print(f"{i+1}. {kategori}")
        

        while True:
            try:
                pilihan_kategori_index = int(input("Masukkan nomor kategori yang ingin dicari: ")) - 1
                if 0 <= pilihan_kategori_index < len(kategori_unik):
                    kategori_terpilih = kategori_unik[pilihan_kategori_index]
                    break
                else:
                    print("Pilihan kategori tidak valid. Mohon masukkan nomor yang benar.")
            except ValueError:
                print("Mohon masukkan pilihan berupa angka!")


        header("📋 YELLOW PAGES Digital UMKM Waru - Sidoarjo")
        print(f"\n--- Data Bisnis Kategori: {kategori_terpilih} ---")
        cetak_tabel()

        ditemukan_data = False
        for bisnis in data_bisnis:
            if bisnis["kategori"].lower() == kategori_terpilih.lower():
                print("{:<4} | {:<25} | {:<15} | {:<28} | {:<15} | {:<15}|".format(
                bisnis["id"], bisnis["nama"], bisnis["kategori"], bisnis["alamat"], bisnis["telepon"], bisnis["jam_buka"]))
                ditemukan_data = True

        if not ditemukan_data:
            print("Tidak ada data bisnis untuk kategori ini.")
        print()
        navigasi_setelah_aksi() 
   
    elif pilih_menu == 3: 
        cari_nama = input("Masukkan nama bisnis yang ingin dicari (sebagian atau penuh): ").strip().lower()
        
        hasil_pencarian = []
        for bisnis in data_bisnis:
            if cari_nama in bisnis["nama"].lower():
                hasil_pencarian.append(bisnis)
        
        if hasil_pencarian:
            print(f"\n--- Hasil Pencarian untuk '{cari_nama}' ---")
            cetak_tabel()
            for bisnis in hasil_pencarian:
                print("{:<4} | {:<25} | {:<15} | {:<28} | {:<15} | {:<15}|".format(
                    bisnis["id"], bisnis["nama"], bisnis["kategori"], bisnis["alamat"], bisnis["telepon"], bisnis["jam_buka"]))
            print()
        else:
            print(f"Tidak ditemukan bisnis dengan nama yang mengandung '{cari_nama}'.")
        navigasi_setelah_aksi()

    else:
        print("Pilihan menu tidak valid.")
        navigasi_setelah_aksi()

def tambah_data():
    header("✨ Tambah Data Bisnis Baru")
    print("Yuk, isi data bisnis baru di bawah ini ya!")

    nama = input("📝 Nama Bisnis     : ").strip().title()
   
    while not nama:
        print("⚠️ Nama bisnis tidak boleh kosong. Mohon diisi.")
        nama = input("📝 Nama Bisnis     : ").strip().title()

    kategori = input("🏷️  Kategori        : ").strip().title()
    while not kategori:
        print("⚠️ Kategori tidak boleh kosong. Mohon diisi.")
        kategori = input("🏷️  Kategori        : ").strip().capitalize()

    alamat = input("📍 Alamat          : ").strip().title()
    while not alamat:
        print("⚠️ Alamat tidak boleh kosong. Mohon diisi.")
        alamat = input("📍 Alamat          : ").strip().title()

    while True:
        telepon_input = input("📞 Telepon         : ").strip()
        if telepon_input.isdigit(): 
            telepon = telepon_input
            break
        else:
            print("⚠️ Nomor telepon harus berupa angka! Mohon masukkan angka yang benar.")

    jam_buka = input("⏰ Jam Buka        : ").strip()
  
    while not jam_buka:
        print("⚠️ Jam buka tidak boleh kosong. Mohon diisi.")
        jam_buka = input("⏰ Jam Buka        : ").strip()

    id_baru = data_bisnis[-1]["id"] + 1 if data_bisnis else 1


    data_bisnis.append({
        "id": id_baru,
        "nama": nama,
        "kategori": kategori,
        "alamat": alamat,
        "telepon": telepon,
        "jam_buka": jam_buka
    })

    print("\n🎉 Data berhasil ditambahkan! Semoga usahanya makin sukses!\n")
    navigasi_setelah_aksi()

def edit_data():
    header("✏️ Edit Data Bisnis")
    print("Bagaimana Anda ingin mengedit data?\n")
    print("1. Edit berdasarkan ID")
    print("2. Edit berdasarkan Kategori")

    while True:
        pilihan_edit = input("Masukkan pilihan (1/2): ").strip()
        if pilihan_edit == '1':
            edit_by_id()
            break
        elif pilihan_edit == '2':
            edit_by_kategori()
            break
        else:
            print("⚠️ Pilihan tidak valid. Mohon masukkan '1' atau '2'.")
    
    navigasi_setelah_aksi()

def edit_by_id():
   
    while True:
        tampilkan_semua()
        try:
            id_edit = int(input("Masukkan ID bisnis yang ingin diedit: "))
            break
        except ValueError:
            print("⚠️ Harap masukkan ID berupa angka ya!\n")
            continue

    bisnis_ditemukan = None
    for bisnis in data_bisnis:
        if bisnis["id"] == id_edit:
            bisnis_ditemukan = bisnis
            break

    if bisnis_ditemukan:
        print("\nSilakan ubah data di bawah ini. Kalau tidak ingin mengubah, cukup tekan Enter.\n")
        
        old_nama = bisnis_ditemukan['nama']
        old_kategori = bisnis_ditemukan['kategori']
        old_alamat = bisnis_ditemukan['alamat']
        old_telepon = bisnis_ditemukan['telepon']
        old_jam_buka = bisnis_ditemukan['jam_buka']

        nama_baru = input(f"Nama Baru ({bisnis_ditemukan['nama']}): ").strip().title()
        if nama_baru: bisnis_ditemukan['nama'] = nama_baru

        kategori_baru = input(f"Kategori Baru ({bisnis_ditemukan['kategori']}): ").strip().title()
        if kategori_baru: bisnis_ditemukan['kategori'] = kategori_baru

        alamat_baru = input(f"Alamat Baru ({bisnis_ditemukan['alamat']}): ").strip().title()
        if alamat_baru: bisnis_ditemukan['alamat'] = alamat_baru

        while True:
            telepon_baru = input(f"Telepon Baru ({bisnis_ditemukan['telepon']}): ").strip()
            if not telepon_baru: 
                telepon_baru = bisnis_ditemukan['telepon']
                break
            elif telepon_baru.isdigit():
                bisnis_ditemukan['telepon'] = telepon_baru
                break
            else:
                print("⚠️ Nomor telepon harus berupa angka! Mohon masukkan angka yang benar.")
        
        jam_buka_baru = input(f"Jam Buka Baru ({bisnis_ditemukan['jam_buka']}): ").strip()
        if jam_buka_baru: bisnis_ditemukan['jam_buka'] = jam_buka_baru

        print("\n✅ Data berhasil diperbarui! Makasih ya!\n")
        print("--- Data Sebelum Perubahan ---")
        print(f"ID       : {bisnis_ditemukan['id']}")
        print(f"Nama     : {old_nama}")
        print(f"Kategori : {old_kategori}")
        print(f"Alamat   : {old_alamat}")
        print(f"Telepon  : {old_telepon}")
        print(f"Jam Buka : {old_jam_buka}")
        print("\n--- Data Setelah Perubahan ---")
        print(f"ID       : {bisnis_ditemukan['id']}")
        print(f"Nama     : {bisnis_ditemukan['nama']}")
        print(f"Kategori : {bisnis_ditemukan['kategori']}")
        print(f"Alamat   : {bisnis_ditemukan['alamat']}")
        print(f"Telepon  : {bisnis_ditemukan['telepon']}")
        print(f"Jam Buka : {bisnis_ditemukan['jam_buka']}\n")
    else:
        print("😕 Maaf, ID yang kamu masukkan nggak ditemukan dalam data. Coba lagi ya!\n")

def edit_by_kategori():
    kategori_unik = sorted(list(set(bisnis["kategori"] for bisnis in data_bisnis)))
    if not kategori_unik:
        print("Belum ada kategori yang tersedia untuk diedit.")
        return

    print("\n--- Kategori yang Tersedia ---")
    for i, kategori in enumerate(kategori_unik):
        print(f"{i+1}. {kategori}")
    print("------------------------------")

    kategori_terpilih = None
    while True:
        try:
            pilihan_kategori = int(input("Masukkan nomor kategori yang ingin diedit: ")) - 1
            if 0 <= pilihan_kategori < len(kategori_unik):
                kategori_terpilih = kategori_unik[pilihan_kategori]
                break
            else:
                print("Pilihan kategori tidak valid. Mohon masukkan nomor yang benar.")
        except ValueError:
            print("Mohon masukkan pilihan berupa angka!")

    if not kategori_terpilih: 
        return

    print(f"\n--- Bisnis dalam Kategori '{kategori_terpilih}' ---")
    bisnis_di_kategori = [bisnis for bisnis in data_bisnis if bisnis["kategori"].lower() == kategori_terpilih.lower()]

    if not bisnis_di_kategori:
        print(f"Tidak ada bisnis dalam kategori '{kategori_terpilih}'.")
        return

    print("-" * 115)
    print("{:<4} | {:<25} | {:<15} | {:<28} | {:<15} | {:<15}".format("ID", "Nama", "Kategori", "Alamat", "Telepon", "Jam Buka"))
    print("-" * 115)
    for bisnis in bisnis_di_kategori:
        print("{:<4} | {:<25} | {:<15} | {:<28} | {:<15} | {:<15}|".format(
            bisnis["id"], bisnis["nama"], bisnis["kategori"], bisnis["alamat"], bisnis["telepon"], bisnis["jam_buka"]))
    print("-" * 115)

    while True:
        try:
            id_edit = int(input("Masukkan ID bisnis dari kategori ini yang ingin diedit: "))
            break
        except ValueError:
            print("⚠️ Harap masukkan ID berupa angka ya!\n")
            continue

    bisnis_ditemukan = None
    for bisnis in bisnis_di_kategori:
        if bisnis["id"] == id_edit:
            bisnis_ditemukan = bisnis
            break

    if bisnis_ditemukan:
        print("\nSilakan ubah data di bawah ini. Kalau tidak ingin mengubah, cukup tekan Enter.\n")
        
       
        old_nama = bisnis_ditemukan['nama']
        old_kategori = bisnis_ditemukan['kategori']
        old_alamat = bisnis_ditemukan['alamat']
        old_telepon = bisnis_ditemukan['telepon']
        old_jam_buka = bisnis_ditemukan['jam_buka']

        nama_baru = input(f"Nama Baru ({bisnis_ditemukan['nama']}): ").strip()
        if nama_baru: bisnis_ditemukan['nama'] = nama_baru

        kategori_baru = input(f"Kategori Baru ({bisnis_ditemukan['kategori']}): ").strip()
        if kategori_baru: bisnis_ditemukan['kategori'] = kategori_baru

        alamat_baru = input(f"Alamat Baru ({bisnis_ditemukan['alamat']}): ").strip()
        if alamat_baru: bisnis_ditemukan['alamat'] = alamat_baru

        while True:
            telepon_baru = input(f"Telepon Baru ({bisnis_ditemukan['telepon']}): ").strip()
            if not telepon_baru: 
                telepon_baru = bisnis_ditemukan['telepon']
                break
            elif telepon_baru.isdigit():
                bisnis_ditemukan['telepon'] = telepon_baru
                break
            else:
                print("⚠️ Nomor telepon harus berupa angka! Mohon masukkan angka yang benar.")
        
        jam_buka_baru = input(f"Jam Buka Baru ({bisnis_ditemukan['jam_buka']}): ").strip()
        if jam_buka_baru: bisnis_ditemukan['jam_buka'] = jam_buka_baru

        print("\n✅ Data berhasil diperbarui! Makasih ya!\n")
        print("--- Data Sebelum Perubahan ---")
        print(f"ID       : {bisnis_ditemukan['id']}")
        print(f"Nama     : {old_nama}")
        print(f"Kategori : {old_kategori}")
        print(f"Alamat   : {old_alamat}")
        print(f"Telepon  : {old_telepon}")
        print(f"Jam Buka : {old_jam_buka}")
        print("\n--- Data Setelah Perubahan ---")
        print(f"ID       : {bisnis_ditemukan['id']}")
        print(f"Nama     : {bisnis_ditemukan['nama']}")
        print(f"Kategori : {bisnis_ditemukan['kategori']}")
        print(f"Alamat   : {bisnis_ditemukan['alamat']}")
        print(f"Telepon  : {bisnis_ditemukan['telepon']}")
        print(f"Jam Buka : {bisnis_ditemukan['jam_buka']}\n")
    else:
        print("😕 Maaf, ID yang kamu masukkan tidak ditemukan dalam kategori ini. Coba lagi ya!\n")


def hapus_data():
    header("🗑️ Hapus Data Bisnis")
    print("Bagaimana Anda ingin menghapus data?")
    print("1. Hapus berdasarkan ID")
    print("2. Hapus berdasarkan Kategori")

    while True:
        pilihan_hapus = input("Masukkan pilihan (1/2): ").strip()
        if pilihan_hapus == '1':
            hapus_by_id()
            break
        elif pilihan_hapus == '2':
            hapus_by_kategori()
            break
        else:
            print("⚠️ Pilihan tidak valid. Mohon masukkan '1' atau '2'.")
    
    navigasi_setelah_aksi()

def hapus_by_id():
    while True:
        tampilkan_semua()
        id_input = input("Masukkan ID bisnis yang ingin dihapus: ").strip()

        if not id_input.isdigit():
            print("⚠️ Input harus berupa angka ID. Coba lagi ya.\n")
            continue

        id_bisnis = int(id_input)
        bisnis_ditemukan = None
        for bisnis in data_bisnis:
            if bisnis["id"] == id_bisnis:
                bisnis_ditemukan = bisnis
                break
        
        if bisnis_ditemukan:
            konfirmasi = input(f"Apakah kamu yakin ingin menghapus bisnis '{bisnis_ditemukan['nama']}' (ID: {bisnis_ditemukan['id']})? (y/n): ").lower()
            if konfirmasi == "y":
                data_bisnis.remove(bisnis_ditemukan)
                print(f"\n✅ Data bisnis dengan ID {id_bisnis} berhasil dihapus.\n")
                print("--- Detail Data yang Dihapus ---")
                print(f"ID       : {bisnis_ditemukan['id']}")
                print(f"Nama     : {bisnis_ditemukan['nama']}")
                print(f"Kategori : {bisnis_ditemukan['kategori']}")
                print(f"Alamat   : {bisnis_ditemukan['alamat']}")
                print(f"Telepon  : {bisnis_ditemukan['telepon']}")
                print(f"Jam Buka : {bisnis_ditemukan['jam_buka']}\n")
            else:
                print("❎ Penghapusan dibatalkan.\n")
            return # Keluar dari fungsi setelah aksi (hapus/batal)
        else:
            print(f"\n🚫 Tidak ditemukan bisnis dengan ID {id_bisnis}.\n")
            lihat_data = input("Apakah kamu ingin melihat daftar bisnis yang tersedia untuk memastikan ID? (y/n): ").lower()
            if lihat_data == "y":
                tampilkan_semua()
            else:
                print("Kamu bisa coba input ulang ID yang benar atau pilih opsi lain.")
                continue # Lanjutkan loop untuk meminta ID lagi

def hapus_by_kategori():
    kategori_unik = sorted(list(set(bisnis["kategori"] for bisnis in data_bisnis)))
    if not kategori_unik:
        print("Belum ada kategori yang tersedia untuk dihapus.")
        return

    print("\n--- Kategori yang Tersedia ---")
    for i, kategori in enumerate(kategori_unik):
        print(f"{i+1}. {kategori}")
    print("------------------------------")

    kategori_terpilih = None
    while True:
        try:
            pilihan_kategori_index = int(input("Masukkan nomor kategori yang ingin dihapus bisnisnya: ")) - 1
            if 0 <= pilihan_kategori_index < len(kategori_unik):
                kategori_terpilih = kategori_unik[pilihan_kategori_index]
                break
            else:
                print("Pilihan kategori tidak valid. Mohon masukkan nomor yang benar.")
        except ValueError:
            print("Mohon masukkan pilihan berupa angka!")

    if not kategori_terpilih: 
        return

    bisnis_di_kategori = [bisnis for bisnis in data_bisnis if bisnis["kategori"].lower() == kategori_terpilih.lower()]

    if not bisnis_di_kategori:
        print(f"Tidak ada bisnis dalam kategori '{kategori_terpilih}'.")
        return

    print(f"\n⚠️ Peringatan! Anda akan menghapus SEMUA bisnis dalam kategori '{kategori_terpilih}'.")
    print("Berikut adalah daftar bisnis yang akan dihapus:")
    print("-" * 120)
    print("{:<4} | {:<25} | {:<15} | {:<28} | {:<15} | {:<15}".format("ID", "Nama", "Kategori", "Alamat", "Telepon", "Jam Buka"))
    print("-" * 120)
    for bisnis in bisnis_di_kategori:
        print("{:<4} | {:<25} | {:<15} | {:<28} | {:<15} | {:<15}|".format(
            bisnis["id"], bisnis["nama"], bisnis["kategori"], bisnis["alamat"], bisnis["telepon"], bisnis["jam_buka"]))
    print("-" * 120)

    konfirmasi_massal = input(f"Apakah Anda YAKIN ingin menghapus {len(bisnis_di_kategori)} bisnis ini? (y/n): ").lower()

    if konfirmasi_massal == "y":
        bisnis_yang_dihapus = []
        for bisnis_to_remove in bisnis_di_kategori:
            data_bisnis.remove(bisnis_to_remove)
            bisnis_yang_dihapus.append(bisnis_to_remove)
        
        print(f"\n✅ Berhasil menghapus {len(bisnis_yang_dihapus)} bisnis dari kategori '{kategori_terpilih}'.\n")
        print("--- Detail Data yang Dihapus ---")
        if bisnis_yang_dihapus:
            print("-" * 115)
            print("{:<4} | {:<25} | {:<15} | {:<28} | {:<15} | {:<15}".format("ID", "Nama", "Kategori", "Alamat", "Telepon", "Jam Buka"))
            print("-" * 115)
            for b in bisnis_yang_dihapus:
                print("{:<4} | {:<25} | {:<15} | {:<28} | {:<15} | {:<15}|".format(
                    b["id"], b["nama"], b["kategori"], b["alamat"], b["telepon"], b["jam_buka"]))
            print("-" * 115)
        else:
            print("Tidak ada data yang dihapus (mungkin ada kesalahan internal atau kategori sudah kosong).")
    else:
        print("❎ Penghapusan berdasarkan kategori dibatalkan.")


menu()
