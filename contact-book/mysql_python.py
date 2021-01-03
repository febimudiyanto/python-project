import mysql.connector as mysql

def buat_db():
    cursor.execute("CREATE DATABASE if not exist "+DATABASE)
    cursor.execute("use "+DATABASE)
    cursor.execute("CREATE TABLE nomor_tlp (id INT AUTO_INCREMENT PRIMARY KEY, nama VARCHAR(255), nomor VARCHAR(255))")
    
    return 0

def koneksi_db():
    global HOST,DATABASE,USER,PASSWORD,db_connect,cursor,db
    HOST= "192.168.122.176"
    DATABASE= "contact"
    USER= "python-user"
    PASSWORD= "inirahasia"
    db_connect= mysql.connect(host=HOST,user=USER, passwd=PASSWORD)
    cursor= db_connect.cursor()
    if db_connect:
        print("Koneksi Sukses...")
        return 1
    else:
        print("Koneksi Gagal.!!!")
        return 0
    list_db=cursor.execute("show databases")
    if DATABASE not in list_db:
        buat_db()
     

koneksi_db()



def tambah_db(nama,nomor):
    cursor.execute("use "+DATABASE)
    sql = "INSERT INTO nomor_tlp (name,nomor) VALUES (%s, %s)"
    value = (nama,nomor)
    cursor.execute(sql,value)

tambah_db("febi","085267582992")
    

