#erite inside txt filc
colours=["yellow","Blue","white"]

try:
    file=open("sample.txt","w")
    for i in colours:
        file.write(f"{i}\n")
    file.close()
except FileNotFoundError:
    print("\n file not found")
except PermissionError:
    print("your are not having peremission to write inside the file")
except Exception as e:
    print("Error: Unkonwn file error")
#Write inside the csv file with with
names=["Varshini","Hasini","Bhoomika"]
try:
    with open("sample2.csv",'w') as file:
        for i in names:
            file.write(f"{i}\n")
except FileNotFoundError:
    print("\n file not found")
except PermissionError:
    print("your are not having peremission to write inside the file")
except Exception as e:
    print("Error: Unkonwn file error")
    #read from txt file
colours=["yellow","Blue","white"]

try:
    file=open("sample.txt","r")
    for i in colours:
        con=file.read()
        print(con)
    file.close()
except FileNotFoundError:
    print("\n file not found")
except PermissionError:
    print("your are not having peremission to write inside the file")
except Exception as e:
    print("Error: Unkonwn file error")

              
              