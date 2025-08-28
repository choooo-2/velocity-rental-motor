import uuid
import json

FILE = "rental.json"

try:
    with open(FILE, "r") as file: # Buka file JSON, "r" = read
        data = json.load(file) # Baca isi file JSON, lalu ubah (load) jadi objek Python.
except FileNotFoundError:
    data = []

print("""
======================================================
      /nSelamat Datang di Rental Kendaraan Warjoeg
=======================================================
      """)
    
pertanyaan = str(input(" rental (y) atau kembalikan kendaraan(n)? (y/n): "))

if pertanyaan == 'n':
    print("Rental Kendaraan Warjoeg")
    id = str(input("Masukkan id Kendaraan: "))
    
    transaksi = None
    
    for t in data:
        if t["id"] == id:
            transaksi = t
            break
        else :
            transaksi = None
            print("ID Kendaraan tidak ditemukan")
    
    if transaksi:
        data.remove(transaksi)
        
        with open(FILE, "w") as file:
            json.dump(data, file)
            
        print("\n✅ Pengembalian berhasil dicatat!")
        print("Terimakasih telah meminjam kendaraan")
        
    else:
        print("ID Kendaraan tidak ditemukan")
    
   
    
else:
    pertanyaan == 'y'

    print("""
    =======================================
         *** Rental Kendaraan Warjoeg ***
    =======================================
    Jenis Mobil:
    a. Avanza        : Rp 350.000 / hari
    b. Xenia         : Rp 320.000 / hari
    c. Innova        : Rp 500.000 / hari
    d. Pajero Sport  : Rp 800.000 / hari

    Jenis Motor:
    e. Beat          : Rp 80.000 / hari
    f. Vario         : Rp 100.000 / hari
    g. NMAX          : Rp 150.000 / hari
    h. PCX           : Rp 160.000 / hari
    =======================================
    """)

    nama = str(input("Nama Penyewa : "))
    alamat = str(input("Alamat       : "))
    nohp = int(input("No. HP       : "))
    ktp = int(input("No. KTP      : "))
    unique_id = str(uuid.uuid4())[:8]  # ambil 8 karakter pertama biar ga kepanjangan
    kendaraan = input("Pilih kendaraan (a-h): ")
    lama = int(input("Lama pinjam (hari): "))
    
    penyewa = {
        "id": unique_id,
        "nama": nama,
        "alamat": alamat,
        "nohp": nohp,
        "ktp": ktp,
        "kendaraan": kendaraan,
        "lama": lama
    }
    
    data.append(penyewa)
    
    with open(FILE, "w") as file:
        json.dump(data, file)

    if kendaraan == 'a':
        jenis = "Avanza"
        harga = 350000
    elif kendaraan == 'b':
        jenis = "Xenia"
        harga = 320000
    elif kendaraan == 'c':
        jenis = "Innova"
        harga = 500000
    elif kendaraan == 'd':
        jenis = "Pajero Sport"
        harga = 800000
    elif kendaraan == 'e':
        jenis = "Beat"
        harga = 80000
    elif kendaraan == 'f':
        jenis = "Vario"
        harga = 100000
    elif kendaraan == 'g':
        jenis = "NMAX"
        harga = 150000
    elif kendaraan == 'h':
        jenis = "PCX"
        harga = 160000
    else:
        print("Pilihan tidak tersedia!")
        exit()

    subtotal = harga * lama

    if lama >= 5:
        diskon = int(subtotal * 0.1)  # diskon 10%
    else:
        diskon = 0

    total = subtotal - diskon

    print(f"\nTotal yang harus dibayar: Rp {total}")
    bayar = int(input("Masukkan nominal pembayaran: "))

    print("\n===================================")
    print("           STRUK RENTAL            ")
    print("===================================")
    print("Nama       :", nama)
    print("Alamat     :", alamat)
    print("No KTP     :", ktp)
    print("-----------------------------------")
    print("Kendaraan  :", jenis)
    print("ID Kendaraan:", unique_id)
    print("Harga/Hari : Rp", harga)
    print("Lama Pinjam:", lama, "hari")
    print("Subtotal   : Rp", subtotal)
    print("Diskon     : Rp", diskon)
    print("-----------------------------------")
    print("TOTAL BAYAR: Rp", total)
    print("Dibayar    : Rp", bayar)

    if bayar >= total:
        kembali = bayar - total
        print("Kembalian  : Rp", kembali)
        print("Silahkan ambil kendaraan di tempat ")
        print("Status     : LUNAS ✅, Terimakasih")
        print("Simpan id untuk pengembalian kendaraan")
    else:
        kurang = total - bayar
        print("Kekurangan : Rp", kurang)
        print("Status     : BELUM LUNAS ❌")

    print("===================================")

   
    