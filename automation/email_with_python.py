#!/usr/bin/env python3

# Author : Febi Mudiyanto
# Date   : 13 - 12 - 2020



#import pandas untuk membuka file xlsx
import pandas as pd
#import getpass untuk menyembunyikan input pwd
import getpass
#import smtp
import smtplib
import string


# ambil database dari xlsx
# df = pd.read_excel("database.xlsx");

# ambil kolom 'email' dan convert ke list
# email = df['email'].tolist()
email = input("masukkan email tujuan : ")


# email pengirim, butuh password untuk authentikasi
# untuk gmail yang didaftarkan verifikasi 2 langkah
# perlu didaftarkan 'sandi aplikasi' sehingga nanti akan diberikan
# password baru khusus untuk perangkat tersebut
# source="emailpengirim@gmail.com"

source = input("masukkan email pengirim : ")
subject = input("masukkan subject : ")

# text yang akan dikirim
body= """

ini text yang akan di kirimkan


terimakasih

"""
# batas text
text = ",".join([
        "From: %s" % source,
        "\nTo: %s" % email,
        "\nSubject: %s" % subject+"\n"
        +body
        ])



print("-------------------------------")
print("mengirim pesan via",source)
# input password, getpass digunakan untuk menyembunyikan hasil ketikan
pwd = getpass.getpass(prompt ="masukkan password :",stream=None)

# koneksi ke server / "smtp.gmail.com"
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    # login email
    server.login(source,pwd)
    print("login sukses")
except:
    print("login gagal")

print("-------------------------------")
try:
    server.sendmail(source,email,text)
    print("[sukses] email berhasil terkirim.....")
except:
    print("[gagal] email tidak terkirim.....!!")

server.quit()

