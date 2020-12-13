abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

huruf = input("masukkan huruf :")
number = int(input("masukkan number :")) - 1

selisih = abjad.index(huruf) - number
print("-----------------------------------------")
cp = list(map(int,input("masukkan chipertext : ").strip().split()))

for i in cp:
    print(abjad[cp[i]-selisih],end="")

