# game suit (batu,gunting,kertas)


from random import randint

def menang():
    global poin_pemain
    poin_pemain += 1
    print("Kamu menang !  (", pemain, ") lebih unggul dari (", com,")")

def kalah():
    global poin_com
    poin_com += 1
    print("Kamu kalah ! (",com,") mengalahkan (",pemain,")")

# daftar dari pilihan
pilih = ["batu","gunting","kertas"]


#papan score
ls_com = []
poin_com = 0
ls_pemain = []
poin_pemain = 0

# pesan/intruksi
print("kalahkan komputer di permainan suit")
print("ketik batu/gunting/kertas !")
print("===============================================")

main = True
while main:
    
    # komputer memilih random
    # random integer dari 0/1/2
    com = pilih[randint(0,2)]
    ls_com.append(com)
    pemain = input("batu, gunting, kertas ? : ")
    ls_pemain.append(pemain)
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
    print("--------------------------------------------------")
    lagi= input("\n Lanjut? (y/n) : ")
    if lagi == "y":
        main = True
    else:
        main = False

print("================================")
print("        papan score       ")
print("(ronde) (pemain)\t(komputer) ")
print("--------------------------------")
for i in range(len(ls_pemain)):
    print(i+1,"\t",ls_pemain[i],"\t",ls_com[i])

print("--------------------------------")
print("nilai :   ",poin_pemain,"\t\t",poin_com)
















