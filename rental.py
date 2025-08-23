class Rental:
    def __init__(self):
        self.mobil = {
            'a': {'nama': 'Toyota Avanza', 'harga/h': 300000, 'kapasitas': '7 Orang'},
            'b': {'nama': 'Honda Brio', 'harga/h': 250000, 'kapasitas': '5 Orang'},
            'c': {'nama': 'Toyota Fortuner', 'harga/h': 500000, 'kapasitas': '7 Orang'},
            'd': {'nama': 'Daihatsu Xenia', 'harga/h': 275000, 'kapasitas': '7 Orang'}
        }
        
        self.montor = {
            'a': {'nama': 'Honda Vario', 'harga/h': 100000},
            'b': {'nama': 'Honda Beat', 'harga/h': 150000},
            'c': {'nama': 'Yamaha R1', 'harga/h': 500000},
            'd': {'nama': 'Suzuki Gixxer', 'harga/h': 275000}
        }
        
        self.paket_tambahan = {
            'a': {'nama': 'Supir Professional', 'harga': 150000},
            'b': {'nama': 'Asuransi Lengkap', 'harga': 75000},
            'c': {'nama': 'Dengan BBM', 'harga': 200000},
            'd': {'nama': 'Baby Seat', 'harga': 25000}
        }
        
        self.pesanan = []
        self.total_harga = 0
    def tampilkan_header(self):
        print("=" * 50)
        print("*** Velocity Rental ***")
        print("=" * 50)
        
    def tampilkan_menu_mobil(self):
        print("\nList Mobil Rental")
        print("-" * 50)
        for key, value in self.mobil.items():
            print(f"{key}. {value['nama']} : Rp {value['harga/h']:,}/hari")
            print(f"   Kapasitas: {value['kapasitas']}")
        print()
        
    def tampilkan_menu_montor(self):
        print("\nList Montor Rental")
        print("-" * 50)
        for key, value in self.montor.items():
            print(f"{key}. {value['nama']} : Rp {value['harga/h']:,}/hari")
        print()
        
    def tampilkan_paket_tambahan(self):
        print("\nPaket Tambahan")
        print("-" * 50)
        for key, value in self.paket_tambahan.items():
            print(f"{key}. {value['nama']} : Rp {value['harga']:,}")
        print()
        
    def tampilkan_promo(self):
        print("\nPromo!!")
        print("Rental > 3 hari dapat diskon 10%")
        print("Rental > 7 hari dapat diskon 20%")
        print("=" * 50)
        
    def proses_pemesanan(self):
        print("\nProses Pemesanan")
        print("-" * 50)
        
        while True:
            try:
                pilihan = int(input("Pilih mobil (1) atau montor (2): "))
                if pilihan == 1 or 2:
                    break
                print("Masukkan angka yang valid.")
            except ValueError:
                print("Masukkan angka yang valid.")
                
        if pilihan == 1:
            self.tampilkan_menu_mobil()
        else:
            self.tampilkan_menu_montor()
        
        # Pilih mobil
        while True:
            pilihan_mobil = input("Pilih mobil or montor (a/b/c/d): ").lower()
            if pilihan_mobil in self.mobil or pilihan_mobil in self.montor:
                break
            print("Pilihan tidak valid. Silakan pilih a, b, c, atau d.")
            
        # Input jumlah hari
        while True:
            try:
                jumlah_hari = int(input("Berapa hari rental? "))
                if jumlah_hari > 0:
                    break
                print("Masukkan jumlah hari yang valid.")
            except ValueError:
                print("Masukkan angka yang valid.")
                
         # Hitung harga mobil
        harga_mobil = self.mobil[pilihan_mobil]['harga/h'] * jumlah_hari
        self.pesanan.append({
            'item': self.mobil or self.montor[pilihan_mobil]['nama'],
            'harga': harga_mobil,
            'jumlah': jumlah_hari,
            'tipe': 'motor'
        })
        
        self.total_harga += harga_mobil
        
        # paket tambahan
        print("\nApakah ingin menambah paket layanan?")
        self.tampilkan_paket_tambahan()
        
        while True:
            tambah_layanan = input("Tambah layanan? (y/n): ").lower()
            if tambah_layanan == 'y':
                pilihan_layanan = input("Pilih layanan (a/b/c/d): ").lower()
                if pilihan_layanan in self.paket_tambahan:
                    harga_layanan = self.paket_tambahan[pilihan_layanan]['harga']
                    self.pesanan.append({
                        'item': self.paket_tambahan[pilihan_layanan]['nama'],
                        'harga': harga_layanan,
                        'jumlah': 1,
                        'tipe': 'layanan'
                    })
                    self.total_harga += harga_layanan
                    print(f"Layanan {self.paket_tambahan[pilihan_layanan]['nama']} ditambahkan.")
                else:
                    print("Pilihan tidak valid.")
            else:
                break
            
             # Hitung diskon
        diskon = 0
        if jumlah_hari > 7:
            diskon = 0.2
            print("Selamat! Anda mendapatkan diskon 20%")
        elif jumlah_hari > 3:
            diskon = 0.1
            print("Selamat! Anda mendapatkan diskon 10%")
            
        jumlah_diskon = self.total_harga * diskon
        total_setelah_diskon = self.total_harga - jumlah_diskon
        
         # Tampilkan struk
        print("\n" + "=" * 50)
        print("STRUK RENTAL")
        print("velocity rental")
        print("=" * 50)
        
        for item in self.pesanan:
            #ternary operator 'hari' if item['tipe'] == 'motor' else 'unit'
            print(f"{item['item']} ({item['jumlah']} {'hari' if item['tipe'] == 'motor' else 'unit'}) : Rp {item['harga']:,}")
        
        print("-" * 50)
        print(f"Subtotal      : Rp {self.total_harga:,}")
        print(f"Diskon        : Rp {jumlah_diskon:,}")
        print(f"Total         : Rp {total_setelah_diskon:,}")
        while True:
            try:
                jumlah_DP = int(input("Berikan DP terlebih dahulu minimal 5 % dari harga total: "))
                if jumlah_DP > 0:
                    break
                print("Masukkan jumlah DP yang valid.")
            except ValueError:
                print("Harus angka.")
        print("=" * 50)
        print("Terima kasih atas pesanan Anda!")
        print("Silakan datang ke lokasi kami untuk mengambil mobil.")
        print('Pembayaran Total dilakukan ketika pengambilan mobil.')
        
    # Jalankan program
if __name__ == "__main__":
    rental = Rental()
    rental.tampilkan_header()
    rental.tampilkan_menu_mobil()
    rental.tampilkan_menu_montor()
    rental.tampilkan_promo()
    rental.proses_pemesanan()