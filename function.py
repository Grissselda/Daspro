def length (list):
    list_temp=append(list,"%")
    j=0
    while list_temp[j]!="%":
        j+=1
    return j

def append(list1,list2):
    list=[*list1,*list2]

    return list

def read(file_csv):
    with open(file_csv) as csv: 
        data=csv.readlines()
        data_fix=[]
        for baris in data :
            part=[]
            temp=""
            for huruf in baris:
                if huruf==";" or huruf=="\n":
                    part=append(part,[temp])
                    temp=""
                else :
                    temp+=huruf
            data_fix=append(data_fix,[part])
        return (data_fix)

def write(file_csv, data):
    with open(file_csv, 'a') as csv:
        csv_line = ';'.join(str(x) for x in data) + '\n'
        csv.write(csv_line)

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
