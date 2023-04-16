def length(list):
    list_temp = append(list, "%")
    j = 0
    while list_temp[j] != "%":
        j += 1
    return j


def append(list1, list2):
    list = [*list1, *list2]

    return list

def findBahanBangunan(nama,deskripsi,jumlah) :
    f = read("bahan_bangunan.csv")
    found = False
    for i in range(length(f)) :
        if(f[i][0] == nama and f[i][1] == deskripsi) :
            found = True
            num = str(int(f[i][2]) + int(jumlah))
            edit("bahan_bangunan.csv",[nama,deskripsi,num],i)
    if(not found) :
        write("bahan_bangunan.csv",[nama,deskripsi,jumlah])

def findJin(nama,pasir,batu,air) :
    f = read("candi.csv")
    found = False
    lastIndex = 0
    for i in range(1,length(f)-1,1):

        if (f[i][1] == nama):

            found = True
            num1 = str(int(f[i][2]) + int(pasir))
            num2 = str(int(f[i][3]) + int(batu))
            num3 = str(int(f[i][4]) + int(air))

            editForFind("candi.csv", [i,nama,num1,num2,num3], i)
        lastIndex = i

    if (not found):
        write("candi.csv", [lastIndex+1,nama,pasir,batu,air])

def read(file_csv):
    with open(file_csv) as csv:
        data = csv.readlines()
        data_fix = []
        for baris in data:
            part = []
            temp = ""
            for huruf in baris:
                if huruf == ";" or huruf == "\n":
                    part = append(part, [temp])
                    temp = ""
                else:
                    temp += huruf
            data_fix = append(data_fix, [part])
        return (data_fix)


def write(file_csv, data):
    with open(file_csv, 'a') as csv:
        csv_line = ';'.join(str(x) for x in data) + '\n'
        csv.write(csv_line)


def editForFind(file_csv, data_new, row):
    with open(file_csv) as csv:
        data = csv.readlines()

    temp = ""
    if row < length(data):
        for i in range(length(data_new)):
            temp += str(data_new[i])
            if i== (length(data)) :
               temp += "\n"
            else :
                temp += ";"

        data[row] = temp

        with open(file_csv, 'w') as csv:
            csv.writelines(data)

def edit(file_csv,data_new,row):
    with open(file_csv) as csv:
        data=csv.readlines()

    if row < length(data):
        data[row]=f"{data_new[0]};{data_new[1]};{data_new[2]}\n"

        with open(file_csv, 'w') as csv:
            csv.writelines(data)

def delete(file_csv, row):
    with open(file_csv, 'r') as csv:
        data = csv.readlines()

    if row < length(data):
        del data[row]

        with open(file_csv, 'w') as csv:
            csv.writelines(data)

def LCG(count,NthKumpul) :
    temp = []
    Xi =( (NthKumpul**2) + 199) % 219
    Xi%=10

    if(Xi !=5) :
        Xi%=5

    if count == 3:
        return [Xi]

    temp += ([Xi] + LCG(count +1,(NthKumpul+count + 1)))

    return temp