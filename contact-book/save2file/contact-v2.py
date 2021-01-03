import os
from os import path


# cek file 
if path.exists("data-contact.txt"):
    file = open("data-contact.txt","r")
    # baca file jika ada data-contact.txt
    contact=file.read()
    if contact!='':
        #jika ada isinya, maka langsung rubah ke dict pakai "eval"
        contact = eval(contact)
        file.close()
        print("============================================")
        print("data-contact.txt --- berhasil diakses")
    else:
        #jika kosong, maka langsung tutup, nanti akan di rewrite di akhir
        contact = {}
        file.close()

else:
    # jika file belum ada, biarkan saja, nanti dibuat di akhir
    contact = {}






def tambah_kontak():
    while True:
        nama=input("Masukkan nama = ")
        nomor=input("Masukkan nomor = ")
        print("--------------------------------------------")
        print("apakah anda ingin memasukkan kontak berikut?")
        print("nama :",nama,"\nnomor :",nomor)
        print("--------------------------------------------")
        opsi=input("ingin di simpan? (y/n) : ")
        if opsi=='y':
            contact[nama]=nomor
            print("penyimpanan sukses...")
        
        print("--------------------------------------------")
        opsi=input("ingin menambahkan kontak lagi ? (y/n) :")
        if opsi!='y':
            break
def hapus_kontak():
    while True:
        print("--------------------------------------------")
        nama = input("masukkan nama kontak yang akan dihapus : ")
        if nama in contact.keys():
            del contact[nama]
            print(nama,"telah dihapus dari kontak\n")
        else:
            print(nama,"tidak ada dalam kontak")

        print("--------------------------------------------")
        opsi = input("apakah ada lagi? (y/n) :")
        if opsi !='y':
            break

def rubah_kontak():
    while True:
        print("--------------------------------------------")
        nama = input("masukkan nama kontak yang akan diubah :")
        if nama in contact.keys():
            nomor = input("masukkan nomor : ")
            contact[nama]=nomor
            print("ubah kontak sukses....")
            
        else:
            print("nama tidak ada di kontak ")
        
        print("--------------------------------------------")
        opsi = input("apakah ada lagi? (y/n) :")
        if opsi !='y':
            break


while True:

    # clear console
    print("\033[H\033[J") 


    print("============================================")
    print("Buku Kontak")
    print("--------------------------------------------")
    if len(contact)==0:
        print("buku kontak kamu masih kosong!")
        opsi=input("berniat mengisinya? (y/n) : ")
        if opsi=='y':
            tambah_kontak()
            continue
    else:
        for nama,nomor in contact.items():
            print("\t",nama,"--->",nomor)
    print("--------------------------------------------")
    print("1. menambah kontak")
    print("2. menghapus kontak")
    print("3. merubah kontak")
    print("0. keluar")
    print("--------------------------------------------")
    opsi = input("masukkan pilihan anda : (1/2/3/0) :")
    if opsi=='1':
        tambah_kontak()
    elif opsi=='2':
        hapus_kontak()
    elif opsi=='3':
        rubah_kontak()
    elif opsi=='0':
        print("sampai jumpa....")
        break
    else:
        print("pilihan anda tidak ada dalam opsi!!")
    
    print("\n\n")



# simpan contact --> data-contact.txt

file = open("data-contact.txt","w")
file.write(str(contact))
file.close()
print("--------------------------------------------")
print("data kontak berhasil tersimpan ")
print("nama file : data-contact.txt")




