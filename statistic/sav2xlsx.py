# jika kamu punya file sav
# kamu bisa mengconvert file sav (file spss) dengan program ini..

import pandas as pd

# baca file .sav
# rubah name-file.sav dengan nama file
df = pd.read_spss("name-file.sav")
print(df.head())


# simpan file ke xlsx
# rubah data.xlsx dengan nama data tujuan..
df.to_excel("data.xlsx")
