from konstruktor import *

def login(user,jumlah_baris):
    Username=input("Username : ")
    Password=input("Password : ")
    part=user_part(user,jumlah_baris)
    list_user=part[0]
    list_pass=part[1]
    list_role=part[2]
    user_valid=False
    pass_valid=False
    for i in range (length(list_user)):
        if Username == list_user[i] :
            user_valid=True
            if Password==list_pass[i]:
                pass_valid=True
                break
    
    if user_valid==True and pass_valid==True:
        print (f'\nSelamat datang, {Username}!\nMasukkan command “help” untuk daftar command yang dapat kamu panggil.')
        return list_role[i]
    elif user_valid==True and pass_valid==False:
        print("\nPassword salah!")
        return 0
    else:
        print("\nUsername tidak terdaftar!")
        return 0

def logout():
    return 0

def summonjin():
    return 0

def hapusjin():
    return 0

def ubahjin():
    return 0

def bangun():
    return 0

def kumpul():
    return 0

def batchkumpul():
    return 0

def laporanjin():
    return 0

def laporancandi():
    return 0

def hancurkancandi():
    return 0

def ayamberkokok():
    return 0

def save():
    return 0

def help(role):
    if role=="bandung_bondowoso":
        print("===================== HELP ======================")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. summonjin")
        print("   Untuk memanggil jin")
        print("3. haousjin")
        print("   Untuk menghapus jin")
        print("4. ubahjin")
        print("   Untuk mengubah tipe jin")
        print("5. batchkumpul")
        print("   Untuk mengumpulkan bahan")
        print("6. batchbangun")
        print("   Untuk mengumpulkan jin bangun")
        print("7. laporanjin")
        print("   Untuk mengetahui kinerja jin")
        print("8. laporancandi")
        print("   Untuk mengetahui proses pembangunan candi")
        print("9. save")
        print("   Untuk menyimpan data")

    elif role=="roro_jonggrang":
        print("===================== HELP ======================")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. hancurkancandi")
        print("   Untuk menghancurkan candi yang tersedia")
        print("3. ayamberkokok")
        print("   Untuk menyelesaikan permainan.")
        print("4. save")
        print("   Untuk menyimpan data")
    
    elif role=="jin_pengumpul":
        print("====================== HELP ======================")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. kumpul")
        print("   Untuk mengumpulkan resource candi")

    elif role=="jin_pembangun":
        print("====================== HELP ======================")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. bangun")
        print("   Untuk membangun candi")

    elif role==0:
        print("====================== HELP ======================")
        print("1. login")
        print("   Untuk masuk menggunakan akun")
        print("2. load")
        print("   Untuk memuat file eksternal ke dalam permainan")
        print("3. exit")
        print("   Untuk keluar dari permainan")

    else:
        return None

def exit(Exit):
    valid=False
    while valid==False:
        simpan=input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
        if simpan == "y":
            valid=True
            return 0
        elif simpan=="n":
            valid=True
            Exit=True
            return Exit