def cek_prima(angka): 
    # angka = 5
    #inisialisasi awal
    prima = True
    # filter untuk cek prima
    if angka < 2:
      prima = False # bukan prima
    else:
      for x in range(2,angka): 
        if (angka % x == 0):
          prima = False # bukan prima
          break

    if prima:
      print("bilangan prima")
    else:
      print("bukan prima")


def cek_genap(angka):
  if (angka%2==0):
    print("angka genap")
  else:
    print('angka ganjil')

def akar(x):
    return x**(1/2)

