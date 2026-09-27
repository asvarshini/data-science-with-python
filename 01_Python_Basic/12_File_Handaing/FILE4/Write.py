# Open file in write mode ("w")
# If the file doesn't exist, it will be created.
# If it already exists, its content will be overwritten.
file = open("Names.txt", 'w')
file.write("Varshini AS\n")
file.write("Prathima M\n")
file.close()
#if i will append a in it then 
filr=open("Names.txt", "a")
print("New content added")
filr.write("Sridhar k")
filr.write("Amrutha AS")
file.close()