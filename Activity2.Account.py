## program Account
## Made By David L200184220
import random
Number_random = random.randint(0,1000)
Name = "Motwkel Mhmoud Mhmed Adam"
DateOfBirth="30 August 1998"
Name_nickname = Name[0] +'.'+ Name[8] +'.'+ Name[15]+'.'+Name[21:25]
Username = Name[0]+DateOfBirth[0:2]+DateOfBirth[11:15]
Password = Name[0:3]+str(Number_random)
