db = "database.txt"


def format_number(data):
    result = ""
    data = list(data)
    data.reverse()
    for num, x in enumerate(data):
        result+=x
        if (num+1)%3 == 0: result+="."
    result = list(result)
    result.reverse()

    return "".join(result)


def lihat():
    data = [x for x in open(db, "r").read().split("\n") if len(x) > 3]
    print("""
===============================
|  PRODUK  |  STOK  |  HARGA  |
==============================="""[1:])
    for x in data:
        if len(x) < 4: continue
        print(x.replace(";;", "\t"))
    print("===============================")
    input("[Press Enter to Continue]")


def add():
    data = ""
    for label in ["Nama Produk : ", "Stok : ", "Harga : "]:
        if "Harga" in label:
            data+="Rp."+format_number(str(input(label)))+";;"
        else:
            data+=str(input(label))+";;"
    open(db, "a").write(data[:-2]+"\n")
    input("[Press Enter to Continue]")


def edit():
    data = [x for x in open(db, "r").read().split("\n") if len(x) > 3]
    print("""
======================================
|  NO  |  PRODUK  |  STOK  |  HARGA  |
======================================"""[1:])
    for num, x in enumerate(data):
        if len(x) < 4: continue
        subdata = f"   {num+1}\t"
        subdata+=x.replace(";;", "\t")
        print(subdata)
    print("======================================")
    while True:
        select_item = str(input("Pilih produk berdasarkan angka : "))
        if select_item.isdigit():
            select_item = int(select_item)
            if (select_item > 0) and (select_item <= len(data)): break
        print("Mohon memasukkan inputan dengan benar")

    update_data = data[select_item-1].split(";;")[0]+";;"
    update_data+=str(input(f"Stok {data[select_item-1].split(';;')[0]} : "))+";;"
    update_data+="Rp."+format_number(str(input(f"Harga {data[select_item-1].split(';;')[0]} : ")))

    result = ""
    for num, x in enumerate(data):
        if num+1 == select_item:
            result+=update_data+"\n"
            continue
        result+=x+"\n"

    open(db, "w").write(result)
    input("[Press Enter to Continue]")


def delete():
    data = [x for x in open(db, "r").read().split("\n") if len(x) > 3]
    print("""
======================================
|  NO  |  PRODUK  |  STOK  |  HARGA  |
======================================"""[1:])
    for num, x in enumerate(data):
        if len(x) < 4: continue
        subdata = f"   {num+1}\t"
        subdata+=x.replace(";;", "\t")
        print(subdata)
    print("======================================")
    while True:
        select_item = str(input("Pilih produk berdasarkan angka : "))
        if select_item.isdigit():
            select_item = int(select_item)
            if (select_item > 0) and (select_item <= len(data)): break
        print("Mohon memasukkan inputan dengan benar")

    result = ""
    for num, x in enumerate(data):
        if num+1 == select_item: continue
        result+=x+"\n"

    open(db, "w").write(result)
    input("[Press Enter to Continue]")


def main():
    while True:
        print("""
=====================================
             toko xyz
=====================================
MENU
1. Lihat Produk
2. Input Porduk
3. Edit Produk
4. Hapus Produk
=====================================""")
        choice = str(input("Pilih Menu ? "))

        if choice == "1":
            lihat()
        elif choice == "2":
            add()
        elif choice == "3":
            edit()
        elif choice == "4":
            delete()
        else:
            print("Mohon memilih menu dengan benar")


if __name__ == '__main__':
    main()


if False:
    pilihan="y"
    while pilihan=="y":
        print("""
        ==============================
                    toko xyz
        ==============================
        A. kentang : Rp 2.000
        B. wortel : Rp 1.500
        C. tomat : Rp 1.000
        ==============================
        """)
        pesan=str(input("masukkan list abjad produk ="))
        jumlahpesan=int(input("masukkan jumlah pesanan ="))
        if pesan == "a":
            listnama= "kentang"
            harga=(2000*jumlahpesan)
      
        elif pesan == "b":
            listnama= "wortel"
            harga = (1500*jumlahpesan)
           
        elif pesan == "c":
            listnama= "tomat"
            harga=int(1000*jumlahpesan)
      
        else:
            listnama = "-"
            harga = "-"
            
            pilihan=input("menu tidak tersedia, silahkan masukkan abjad menu yang tersedia silahkan ulangi kembali Y/N =")
     
        print("--------------------------")
        print("toko xyz")
        print("--------------------------")
        print("Menu :",listnama)
        print("Jumlah Pesan :", jumlahpesan)
        print("Harga :", harga)
        print("--------------------------")
        print("--------------------------")
        pilihan=input("apakah anda ingin order kembali Y/N =")