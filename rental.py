class RentalMobil:
    def __init__(self):
        self.mobil = {
            'a': {'nama': 'Toyota Avanza', 'harga/h': 300000, 'kapasitas': '7 Orang'},
            'b': {'nama': 'Honda Brio', 'harga/h': 250000, 'kapasitas': '5 Orang'},
            'c': {'nama': 'Toyota Fortuner', 'harga/h': 500000, 'kapasitas': '7 Orang'},
            'd': {'nama': 'Daihatsu Xenia', 'harga/h': 275000, 'kapasitas': '7 Orang'}
        }
        
        self.montor = {
            'a': {'nama': 'Honda Vario', 'harga/h': 300000},
            'b': {'nama': 'Honda Beat', 'harga/h': 250000},
            'c': {'nama': 'Yamaha R1', 'harga/h': 500000},
            'd': {'nama': 'Suzuki Gixxer', 'harga/h': 275000}
        }
        
        self.paket_tambahan = {
            'a': {'nama': 'Supir Professional', 'harga/h': 150000},
            'b': {'nama': 'Asuransi Lengkap', 'harga/h': 75000},
            'c': {'nama': 'Dengan BBM', 'harga/h': 200000},
            'd': {'nama': 'Baby Seat', 'harga/h': 25000}
        }
        
        self.pesanan = []
        self.total_harga = 0
    def tampilkan_header(self):
        print("=" * 50)
        print("*** Waroeng Njagoeng Rental Mobil ***")
        print("=" * 50)
        
    def tampilkan_header(self):
        print("=" * 50)
        print("*** Waroeng Njagoeng Rental Mobil ***")
        print("=" * 50)
        
    def tampilkan_menu_mobil(self):
        print("\nList Mobil Rental")
        print("-" * 50)
        for key, value in self.mobil.items():
            print(f"{key}. {value['nama']} : Rp {value['harga']:,}/hari")
            print(f"   Kapasitas: {value['kapasitas']}")
        print()
        
    def tampilkan_menu_montor(self):
        print("\nList Montor Rental")
        print("-" * 50)
        for key, value in self.montor.items():
            print(f"{key}. {value['nama']} : Rp {value['harga']:,}/hari")
            print(f"   Kapasitas: {value['kapasitas']}")
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