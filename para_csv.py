import csv
def para_csv(file):
    mylist=[]

    with open(file,"r",encoding="utf-8") as f:
        data=csv.reader(f)
        for i in data:
            mylist.append(i)
        del mylist[0]
        return mylist
if __name__ == '__main__':
    data=para_csv(r"C:\Users\ErvinChiu\Desktop\csv_data.csv")
    print(data)


