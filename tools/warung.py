import main
from services import db

def tambah():
    kode_barang = input("Kode barang: ")
    nama_barang = input("Nama Barang: ")
    harga_barang = int(input("Harga Barang: "))
    stok_barang = int(input("Stok Barang: "))
    
    db.insert_barang(kode_barang, nama_barang, harga_barang, stok_barang)


def check():
    items = db.fetch()
    for item in items:
        kode_barang = item[1]
        nama_barang = item[2]
        harga_barang = item[3]
        stok_barang = item[4]
        print(f'''
Kode - {kode_barang}
{nama_barang} | Rp.{harga_barang:,.0f}
Stok: {stok_barang}
              ''')

def start():
    while True:
        menu = int(input("menu:\n\n1. Tambah Barang\n2. Check Barang\n3. Exit\n\nMasukkan pilihan menu: "))
        if menu == 1:
            tambah()
        elif menu == 2:
            check()
        elif menu == 3:
            main.menu()
        else:
            break
            
if __name__ == "__main__":
    start()