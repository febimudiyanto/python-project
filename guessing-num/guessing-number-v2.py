# guessing number game ( tebak angka )
# syarat : I/O, Looping, Pengodisian, Control Flow

# import modul (function) random
import random


def cek_tebakan(tebakan):
    global benar
    if tebakan == rahasia:
        print("\n\t Selamat..... anda berhasil menebak!")
        print("\n")
        
        benar=True
    elif tebakan > rahasia:
        benar = False
        print("angka terlalu tinggi!")
    elif tebakan < rahasia:
        benar = False
        print("angka terlalu rendah!")
    

# angka rahasia
rahasia = random.randint(1,100) # mengacak bilangan bulat dari 1 - 100 // 68

# kesempatan/ nyawa
K = 7

print("===========================================")
print("Tebak lah suatu angka dari 1-100")
print("kamu cuma punya",K,"kesempatan")
print("gunakan sebaik-baiknya, tebak dengan tepat")
print("--------------------------------------------")

while K > 0: #berjalan ketika True
    # user menginput suatu angka
    print("------------------------sisa nyawa:",K)
    tebakan =int(input("tebak sebuah angka = "))
    
    # pengondisian

    cek_tebakan(tebakan)
    if benar: # benar==True
        break
    # kesempatan berkurang
    K -= 1
    
# kondisi ketika selesai
# 1. K <= 0 atau nyawa habis
# 2. Jawaban benar, while akan selesai dengan cara "break" K>0

#jika loopnya selesai
if K <= 0:
    print("\n\tAnda belum berhasil")
    print("\tAngka rahasianya adalah = ",rahasia)
    print("\tCoba lagi ya.... :D ")

