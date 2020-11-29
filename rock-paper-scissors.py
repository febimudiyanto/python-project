# game suit (batu,gunting,kertas)


from random import randint

def menang():
    print("Kamu menang !  (", pemain, ") lebih unggul dari (", com,")")

def kalah():
    print("Kamu kalah ! (",com,") mengalahkan (",pemain,")")




# daftar dari pilihan
pilih = ["batu","gunting","kertas"]



# pesan/intruksi
print("kalahkan komputer di permainan suit")
print("ketik batu/gunting/kertas !")
print("===============================================")

main = True
while main:
    
    # komputer memilih random
    # random integer dari 0/1/2
    com = pilih[randint(0,2)]
    
    pemain = input("batu, gunting, kertas ? : ")
    print("--------------------------------------------------")
    if pemain == com:
        print("Seri !")
    elif pemain == "batu":
        if com == "kertas":
            kalah()
        else:
            menang()
    elif pemain == "gunting":
        if com == "batu":
            kalah()
        else:
            menang()
    elif pemain == "kertas":
        if com == "gunting":
            kalah()
        else:
            menang()
    else:
        print("\tmasukkan batu/gunting/kertas !")
        continue
    print("--------------------------------------------------")
    lagi= input("\n Lanjut? (y/n) : ")
    if lagi == "y":
        main = True
    else:
        main = False

