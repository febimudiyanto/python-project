# guessing number game ( tebak angka )


# import modul (function) random
import random

# angka rahasia
rahasia = random.randrange(1,100)

# kesempatan
K = 7
print("===========================================")
print("kamu cuma punya",K,"kesempatan")
print("gunakan sebaik-baiknya, tebak dengan tepat")
print("--------------------------------------------")

while K > 0:
    # user menginput suatu angka
    print("\n------------------------sisa nyawa:",K)
    tebakan =int(input("tebak sebuah angka = "))

    # pengondisian
    if tebakan == rahasia:
        print("----------------------------------------------")
        print("|\n|\t Selamat..... anda berhasil menebak!")
        print("|")
        print("----------------------------------------------")
        #loopnya akan selesai
        break
    elif tebakan > rahasia:
        print("angka terlalu tinggi!")
    elif tebakan < rahasia:
        print("angka terlalu rendah!")
    
    # kesempatan berkurang
    K -= 1


#jika loopnya selesai
if K <= 0:
    print("----------------------------------------------")
    print("|\n|\tAngka rahasianya adalah = ",rahasia)
    print("|\tCoba lagi ya.... :D ")
    print("----------------------------------------------")



