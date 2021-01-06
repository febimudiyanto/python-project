'''
author : Febi Mudiyanto
date : 06-01-2021
description : program ini dibuat untuk yang bingung data mau diapakan dengan Machine Learning :D

'''

print("=================================")
print("    Mengolah Data dengan ML")
print("---------------------------------")
x = input("Apakah Jumlah data lebih dari 50 record? (y/n)")
if x != 'y':
    print("\t>>cari tambahan data")
else:
    x = input("Memprediksi Kategori? (y/n)")
    if x == 'y':
        x = input("Apakah data punya label? (y/n)")
        if x=='y':
            x = input("Apakah Jumlah Data < 100.000 record? (y/n)")
            if x=='y':
                print("\t>>Gunakan Metode Linear SVC atau KNN")
            else:
                print("\t>>Gunakan Metode SGDClassifier")
        else:
            print("Cari Kategori-kategori yang anda ketahui")
            x = input("Apakah jumlah sampel data < 10.000? (y/n)")
            if x=='y':
                print("\t>>Gunakan Metode Kmeans atau Spectral Cluster")
            else:
                print("\t>>Gunakan Metode Mini BatchKmeans")
            
    else:
        x = input("Memprediksi Kuantitas/Jumlah? (y/n)")
        if x!='y':
            print("\t>>Gunakan Metode Principal Componen Analysis (PCA)")
        else:
            x = input("Apakah Jumlah Data < 100.000 record ? (y/n)")
            if x =='y':
                print("\t>>Gunakan Metode RidgeRegressionSVR (kernel = linear)")
            else:
                print("\t>>Gunakan Metode SGDRegressor")

        