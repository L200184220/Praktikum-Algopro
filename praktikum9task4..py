## Activity 4
import shelve

myFile = shelve.open ("Motwkel Mhmoud Mohmed Adam")
print (myFile["BIOGRAFI"][0])
print (myFile["BIOGRAFI"][1])
print (myFile["BIOGRAFI"][2])
print (myFile["BIOGRAFI"][3])
myFile.close()
