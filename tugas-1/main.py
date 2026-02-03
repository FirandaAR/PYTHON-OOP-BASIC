data = []

def tambah_data():
    print("Tambah data\n")
    id = int(input("ID   :  "))
    nama = input("Nama   :  ")
    kelas = input("Kelas   :  ")

    data.append({
        "id": id,
        "nama": nama,
        "kelas": kelas
    })
    print("Data telah di tambahkan! \n")

def tampilkan_data():
    print("Ini data nya bray:")
    if len(data) == 0:
       print("Kosong kayak dompet lo")
    else:
        for d in data:
            print("ID:", d["id"])
            print("Nama:", d["nama"])
            print("Kelas:", d["kelas"])
            print("-" * 20)

def ubah_data():
    print("\nMau ubah data?")
    id_cari = int(input("Masukkan id data yang ingin diubah : "))

    for d in data:
        if d["id"] == id_cari:
            d["nama"] = input("Nama baru : ")
            d["kelas"] = input("Kelas baru : ")
            print("Data udah diubah\n")
            return
    print("Data ora ono")
            

def hapus_data():
    print("\nMau hapus data?")
    id_cari = int(input("Masukkin ID yang mau dihapus : "))

    for d in data:
        if d["id"] == id_cari:
            data.remove(d)
            print("Data berhasil gw hapus")
            return

    print("Data ora ono")

while True:
    print("=== MENU ===")
    print("1. Tambah data")
    print("2. Tampilkan data")
    print("3. Ubah data")
    print("4. Hapus data")
    print("0. Keluar\n")

    pilihan = int(input("Pilih yang mana tot? "))
    print("")

    if pilihan == 1:
        tambah_data()
    elif pilihan == 2:
        tampilkan_data()
    elif pilihan == 3:
        ubah_data()
    elif pilihan == 4:
        hapus_data()
    elif pilihan == 0:
        print("Okee gut bay")
        break
    else:
        print("Pilih nomer yang ada aja! ")