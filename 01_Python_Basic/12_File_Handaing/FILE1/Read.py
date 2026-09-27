fi =open("File.txt",'r') #to open file
content=fi.read() #read entire cintent of file
print("Content of files using read")
print(content)
fi.close()
