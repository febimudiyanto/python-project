abjad = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

cp = list(map(str,input("masukkan chipertext :").strip().split()))
print("-----------------------------------------")

for i in range(len(cp)):
    if cp[i].isnumeric():
        print(abjad[i], end="")
    else:
        print(cp[i],end="")
print("")
