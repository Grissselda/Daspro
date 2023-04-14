from function import *

def login(data_user):
    Username=input("Username : ")
    Password=input("Password : ")
    user_valid=False
    pass_valid=False
    for i in range (1,length(data_user)):
        if Username == data_user[i][0] :
            user_valid=True
            if Password==data_user[i][1]:
                pass_valid=True
                break
    
    if user_valid==True and pass_valid==True:
        print (f'\nSelamat datang, {Username}!\nMasukkan command “help” untuk daftar command yang dapat kamu panggil.')
        return (data_user[i][2],data_user[i][0])
    elif user_valid==True and pass_valid==False:
        print("\nPassword salah!")
        return 0,0
    else:
        print("\nUsername tidak terdaftar!")
        return 0,0

def logout(role):
    if role == 0 :
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        role=0
    else :
        role=0
    
    return role

def summonjin(data,role):
    if length(data)<104 and role=="bandung_bondowoso":
        print("Jenis jin yang dapat dipanggil:")
        print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print(" (2) Pembangun - Bertugas membangun candi")
        valid=False
        new_user=[0,0,0]
        while valid==False:
            nomor=input("\nMasukkan nomor jenis jin yang ingin dipanggil: ")
            if nomor=="1" or nomor=="Pengumpul":
                print("\nMemilih jin “Pengumpul”.")
                valid=True
                new_user[2]="jin_pengumpul"
            elif nomor=="2" or nomor=="Pembangun":
                print("\nMemilih jin “Pembangun”.")
                valid=True
                new_user[2]="jin_pembangun"
            elif nomor!="1" or nomor!="2" or nomor!="Pembangun" or nomor!="Pengumpul" :
                print(f"\nTidak ada jenis jin bernomor “{nomor}”!")
        valid=False
        while valid==False:
            nama=input("\nMasukkan username jin: ")
            j=1
            while j<length(data):
                if data[j][0]==nama:
                    print(f"\nUsername “{nama}” sudah diambil!")
                    valid=False
                    break
                else :
                    j+=1            
                
            if j == length(data):
                valid=True
                new_user[0]=nama

        valid=False
        password=input("Masukkan password jin: ")
        while valid==False:
            if 5<=length(password)<=25 :
                valid=True
                new_user[1]=password
                print("\nMengumpulkan sesajen...")
                print("Menyerahkan sesajen...")
                print("Membacakan mantra...")
                print(f"\nJin {new_user[0]} berhasil dipanggil!")
            else:
                print("\nPassword panjangnya harus 5-25 karakter!")
                password=input("\nMasukkan password jin: ")  
                valid=False              
        
        return new_user
    elif length(data)>=104:
        return 0
    if role!="bandung_bondowoso":
        return 1

def hapusjin(file_csv,data,role):
    if role=="bandung_bondowoso":
        name_del=input("Masukkan username jin : ")
        j=1
        while j < length(data):
            if name_del==data[j][0] :
                break
            else :
                j+=1
        if j==length(data):
            print("\nTidak ada jin dengan username tersebut.")
        else:
            valid=input(f"Apakah anda yakin ingin menghapus jin dengan username {name_del} (Y/N)? ")
            if valid=="Y" or valid=="y":
                delete(file_csv,j)
                print("Jin telah berhasil dihapus dari alam gaib.")
                return 0
            else:
                return 0
    else :
        return 1

def ubahjin(file_csv,data,role):
    if role=="bandung_bondowoso":
        name_change=input("Masukkan username jin : ")
        j=1
        while j < length(data):
            if name_change==data[j][0] :
                break
            else :
                j+=1
        if j==length(data):
            print("\nTidak ada jin dengan username tersebut.")
        else:
            if data[j][2]=="jin_pengumpul":
                valid=input("Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ")
                new=[data[j][0],data[j][1],"jin_pembangun"]
                if valid=="Y" or valid=="y":
                    edit(file_csv,new,j)
                    print("\nJin telah berhasil diubah.")
                    return 0
                else:
                    return 0                
            elif data[j][2]=="jin_pembangun":
                valid=input("Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ")
                new=[data[j][0],data[j][1],"jin_pengumpul"]                
                if valid=="Y" or valid=="y":
                    edit(file_csv,new,j)
                    print("\nJin telah berhasil diubah.")
                    return 0
                else:
                    return 0
    else :
        return 1

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

def load():
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