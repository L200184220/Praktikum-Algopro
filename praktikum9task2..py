## writ the date to file
myFile = open ("L200184220","w")
myFile.write ("L200184220 \n")
myFile.write ("30/08/1998 \n")
myFile.write ("Motwkel Mhmoud Momhmed Adam \n")
myFile.write ("solo")
myFile.close ()

myFile = open ("L200184220","r")
x = myFile.readlines()
print (x[2])
print (x[3]+ ','+ x[1])
print (x[0])
myFile.close()
