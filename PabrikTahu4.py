
class Node:
    def __init__(self, idd, bulan, tahun, saldo_tetap, pemasukan, pengeluaran):
        self.idd = idd
        self.bulan = bulan
        self.tahun = tahun
        self.saldo = saldo_tetap
        self.pemasukan = pemasukan
        self.pengeluaran = pengeluaran
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.current_id = 1

    def tambah_data_kas(self, bulan, tahun, saldo_tetap, pemasukan, pengeluaran):
        new_node = Node(self.current_id, bulan, tahun, saldo_tetap, pemasukan, pengeluaran)
        self.current_id += 1
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def lihat_buku_kas(self):
        current = self.head
        while current:
            print(f"ID: {current.idd}, Bulan: {current.bulan}, Tahun: {current.tahun}")
            print("Saldo:", current.saldo)
            print("Pemasukan:", current.pemasukan)
            print("Pengeluaran:", current.pengeluaran)
            print("")
            current = current.next

    def hapus_data(self, idd):
        if not self.head:
            print("Buku kas masih kosong.")
            return
        if self.head.idd == idd:
            self.head = self.head.next
            print("Data berhasil dihapus.")
            return
        current = self.head
        while current.next:
            if current.next.idd == idd:
                current.next = current.next.next
                print("Data berhasil dihapus.")
                return
            current = current.next
        print("ID tidak ditemukan.")

    def sorting(self):
        if not self.head:
            print("Buku kas masih kosong.")
            return
        swapped = True
        while swapped:
            current = self.head
            swapped = False
            while current.next:
                if current.tahun > current.next.tahun or (current.tahun == current.next.tahun and current.bulan > current.next.bulan):
                    current.idd, current.next.idd = current.next.idd, current.idd
                    current.bulan, current.next.bulan = current.next.bulan, current.bulan
                    current.tahun, current.next.tahun = current.next.tahun, current.tahun
                    current.saldo, current.next.saldo = current.next.saldo, current.saldo
                    current.pemasukan, current.next.pemasukan = current.next.pemasukan, current.pemasukan
                    current.pengeluaran, current.next.pengeluaran = current.next.pengeluaran, current.pengeluaran
                    swapped = True
                current = current.next
        print("Buku kas berhasil diurutkan.")

    def jump_search(self, key, attribute):
        found_entries = []
        current = self.head
        while current:
            if attribute == "bulan" and current.bulan == key:
                found_entries.append(current)
            elif attribute == "tahun" and current.tahun == key:
                found_entries.append(current)
            current = current.next
        return found_entries if found_entries else None

bukukas = LinkedList()
bukukas.tambah_data_kas("Desember", 2022, 1000000, 2000000, 1600000)
bukukas.tambah_data_kas("Januari", 2023, 1400000, 1500000, 500000)
bukukas.tambah_data_kas("Februari", 2024, 2400000, 2100000, 1900000)
bukukas.tambah_data_kas("Mei", 2024, 2600000, 1500000, 2000000)
bukukas.tambah_data_kas("April", 2024, 2100000, 1750000, 820000)
bukukas.tambah_data_kas("Agustus", 2024, 3030000, 2500000, 4545000)
bukukas.tambah_data_kas("Januari", 2024, 985000, 2900000, 1500000)

while True:
    print("Selamat Datang")
    print("Menu")
    print("1. Lihat Buku Kas")
    print("2. Tambahkan Data Baru")
    print("3. Hapus Data")
    print("4. Ubah Data")
    print("5. Sorting")
    print("6. Pencarian")
    print("7. Keluar")
    pilih = input("Masukkan Pilihan : ")

    if pilih == "1":
        print("Data Kas Bulanan:")
        bukukas.lihat_buku_kas()

    elif pilih == "2":
        bulan = input("Masukkan Bulan Transaksi : ")
        tahun = int(input("Masukkan Tahun Transaksi : "))
        pemasukan = int(input("Masukkan Pemasukan Transaksi : "))
        pengeluaran = int(input("Masukkan Pengeluaran Transaksi : "))
        
        saldo_terakhir = 0
        if bukukas.head:
            current = bukukas.head
            while current.next:
                current = current.next
            saldo_terakhir = current.saldo        
        saldo_baru = saldo_terakhir + pemasukan - pengeluaran
        bukukas.tambah_data_kas(bulan, tahun, saldo_baru, pemasukan, pengeluaran)
        print("Data Berhasil Ditambahkan.")
        print("")

    elif pilih == "3":
        idd_hapus = int(input("Masukkan ID yang ingin dihapus: "))
        bukukas.hapus_data(idd_hapus)

    elif pilih == "4":
        print("Menu Ubah Data: (Belum Diimplementasikan)")
        bulan_update = str(input("Masukkan Nama Bulan yang ingin Diperbarui : "))
        tahun_update = int(input("Masukkan Tahun yang ingin diperbarui : "))
        if bukukas.dapatkan_data_kas(bulan_update, tahun_update):
            pemasukan_baru = int(input("Masukkan Jumlah Pemasukan Baru : "))
            pengeluaran_baru = int(input("Masukkan Jumlah Pengeluaran Baru : "))
            saldo_baru = int(input("Masukkan Saldo Baru : "))
            if bukukas.update_data_kas(bulan_update, tahun_update, pemasukan_baru, pengeluaran_baru, saldo_baru):
                print("Data kas berhasil diperbarui.")
            else:
                print("Gagal memperbarui data.")
        else:
            print("Data tidak ditemukan.")
    elif pilih == "5":
        bukukas.sorting()

    elif pilih == "6":
        print("Menu Pencarian:")
        print("1. Pencarian berdasarkan Bulan")
        print("2. Pencarian berdasarkan Tahun")
        search_choice = input("Pilih jenis pencarian: ")
        if search_choice == "1":
            bulan_search = input("Masukkan Nama Bulan yang ingin dicari: ")
            result = bukukas.jump_search(bulan_search, "bulan")
            if result:
                print("Data ditemukan:")
                for entry in result:
                    print(f"ID: {entry.idd}, Bulan: {entry.bulan}, Tahun: {entry.tahun}")
                    print("Saldo:", entry.saldo)
                    print("Pemasukan:", entry.pemasukan)
                    print("Pengeluaran:", entry.pengeluaran)
            else:
                print("Data tidak ditemukan.")
        elif search_choice == "2":
            tahun_search = int(input("Masukkan Tahun yang ingin dicari: "))
            result = bukukas.jump_search(tahun_search, "tahun")
            if result:
                print("Data ditemukan:")
                for entry in result:
                    print(f"ID: {entry.idd}, Bulan: {entry.bulan}, Tahun: {entry.tahun}")
                    print("Saldo:", entry.saldo)
                    print("Pemasukan:", entry.pemasukan)
                    print("Pengeluaran:", entry.pengeluaran)
            else:
                print("Data tidak ditemukan.")

    elif pilih == "7":
        break
