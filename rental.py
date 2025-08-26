pilihan = 'y'
while pilihan == 'y':
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

    nama = input("Nama Penyewa : ")
    alamat = input("Alamat       : ")
    ktp = input("No. KTP      : ")

    jaminan = input("Jaminan (SIM/KTP/KK): ")

    kendaraan = input("Pilih kendaraan (a-h): ")
    lama = int(input("Lama pinjam (hari): "))

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
        continue

    subtotal = harga * lama

    if lama > 7:
        diskon = int(subtotal * 0.1)  # diskon 10%
    else:
        diskon = 0

    ppn = int((subtotal - diskon) * 0.1)
    total = subtotal - diskon + ppn

    print(f"\nTotal yang harus dibayar: Rp {total}")
    bayar = int(input("Masukkan nominal pembayaran: "))

    print("\n===================================")
    print("           STRUK RENTAL            ")
    print("===================================")
    print("Nama       :", nama)
    print("Alamat     :", alamat)
    print("No KTP     :", ktp)
    print("Jaminan    :", jaminan)
    print("-----------------------------------")
    print("Kendaraan  :", jenis)
    print("Harga/Hari : Rp", harga)
    print("Lama Pinjam:", lama, "hari")
    print("Subtotal   : Rp", subtotal)
    print("Diskon     : Rp", diskon)
    print("PPN (10%)  : Rp", ppn)
    print("-----------------------------------")
    print("TOTAL BAYAR: Rp", total)
    print("Dibayar    : Rp", bayar)

    if bayar >= total:
        kembali = bayar - total
        print("Kembalian  : Rp", kembali)
        print("Status     : LUNAS ✅, Terimakasih")
    else:
        kurang = total - bayar
        print("Kekurangan : Rp", kurang)
        print("Status     : BELUM LUNAS ❌")

    print("===================================")

    pilihan = input("\nApakah ingin rental lagi? (y/n): ")