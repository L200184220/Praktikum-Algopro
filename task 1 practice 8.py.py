Dictionary = {"NIM" : "L200184220",
              "Name" : "Motwkel Mhmoud Mohmed Adam ",
              "Address" :"pesma",
              "Post_Code" : "127575",
              "No.Hp" : "00249127575925",
              "Instagram" : "motwkelmhmoudkola",
              "Email" : "motwukelmohamoud@gmail.com"}
print("""
option available:
b to show this help
N to show NIM
a to show Name
A to show Address
K to show Post Code
S to show no.HP
R to show Instagram
G to show Email
k Out
""")
k = "Thank you"
M = input ("your choice : ")
while M != "k" :
     if M == "N" :
        print (Dictionary["NIM"])
        print("")
        M = input ("your choice : ")
     elif M == "a" :
        print (Dictionary["Name"])
        print ("")
        M = input ("your choice : ")
     elif M == "A" :
        print (Dictionary["Address"])
        print("")
        M = input ("your choice : ")
     elif M == "K" :
        print (Dictionary["Post_Code"])
        print ("")
        M = input ("your choice : ")
     elif M == "S" :
        print (Dictionary["No.Hp"])
        print("")
        M = input ("your choice : ")
     elif M == "R" :
        print (Dictionary["Instagram"])
        print ("")
        M = input ("your choice : ")
     elif M == "G" :
        print (Dictionary["Email"])
        print("")
        M = input ("your choice : ")
     elif M == "b":
        print ("""
option available :
b to show this help
N to show NIM
a to show Name
A to show Address
K to show Post Code
S to show no.HP
R to show Instagram
G to show Email
k Out
""")

        print ("")
        M = input ("your choice : ")
     else : 
        print ("it is not definded")
        print ("")
        M = input ("your choice : ")
print (k)

