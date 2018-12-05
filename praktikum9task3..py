## Activities 3
import shelve

myFile = open ("L200184220","r")
NIM = myFile.readline()
BORN = myFile.readline()
NAME = myFile.readline()
CITY =myFile.readline()

myFile = shelve.open ("Motwkel Mhmoud Mohmed Adam")
myFile ["BIOGRAFI"] = [NIM, BORN, NAME, CITY]
myFile.close()
