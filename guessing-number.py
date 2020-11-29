# guessing number game ( tebak angka )


# import modul (function) random
import random

# angka rahasia
rahasia = random.randrange(1,100)

# kesempatan
K = 7


while K > 0:
    # user menginput suatu angka
    print("------------------------sisa nyawa:",K)
    tebakan =int(input("tebak sebuah angka = "))
    
    # kesempatan berkurang
    K -= 1

    # pengondisian
    if tebakan == rahasia:
        print("\n\t Selamat..... anda berhasil menebak!")
        print("\n")
        #loopnya akan selesai
        break
    elif tebakan > rahasia:
        print("angka terlalu tinggi!")
    elif tebakan < rahasia:
        print("angka terlalu rendah!")

#jika loopnya selesai
if K <= 0:
    print("\n\tAngka rahasianya adalah = ",rahasia)
    print("\tCoba lagi ya.... :D ")




