# python-project

## Guessing Number
tebakan angka


### Import Modul
Menggunakan modul "random" untuk memberikan angka rahasia secara acak

```
import random

```

### Inisialisasi angka rahasia dan K (kesempatan)
rahasia, adalah variable untuk angka yang akan di tebak
K, adalah total kesempatan yang dimiliki user untuk menebak

```
# angka rahasia
rahasia = random.randint(1,100)

# kesempatan
K = 7

```

### Looping dan cek tebakan
Looping akan berjalan dengan kondisi K > 0, kemudian setiap loop K akan berkurang 1.
```
while K > 0:
    # user menginput suatu angka
    print("------------------------sisa nyawa:",K)
    tebakan =int(input("tebak sebuah angka = "))
    
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
    
    # kesempatan berkurang
    K -= 1

```

### Jika loop selesai, cek kondisi apakah Kesempatan masih > 0
ada 2 kondisi saat while selesai, yaitu:
1. kondisi ketika tebakan benar, maka "break" akan menghentikan loop
2. kondisi ketika K=0
maka ketika while selesai, dengan tebakan benar maka K tentu masih >0, sehingga perlu di cek
sebagai berikut.
```
#jika loopnya selesai
if K <= 0:
    print("\n\tAngka rahasianya adalah = ",rahasia)
    print("\tCoba lagi ya.... :D ")
```


Terimakasih.


Febi Mudiyanto
