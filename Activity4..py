Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Name = "Motwkel Mhmoud Mohmed Adam"
>>> NIM = 220
>>> Height = 1.71
>>> Weight = 70
>>> YearOfBrith = 1998
>>> Me = (YearOfBrith, Weight, Height, NIM, Name)
>>> Data = [YearOfBrith, Weight, Height, NIM, Name]
>>> type (Me)
<class 'tuple'>
>>> ##this command to know What is type of Me,Why the python print<class 'tuple'> ? becuse Me is type tuple.
>>> Me [0]
1998
>>> ##this command call word in the tuple. the row of object and it is start(0,1,2,3,4,.....)
>>> a = NIM % 4 : Me [a]
SyntaxError: invalid syntax
>>> a = NIM % 4 ; Me [a]
1998
>>> type (Me[a])
<class 'int'>
>>> ##this command to know What the type of Me[a], type is int beacuse value Me[a] is 1998.
>>> Me[a:4]
(1998, 70, 1.71, 220)
>>> ##this command slice word in the yuple. beacuse value of Me [a:4] is YearOfBrith , weight,height and NIM.
>>> type(Data)
<class 'list'>
>>> ##this command to know what is type of Data.
>>> type(Data[4])
<class 'str'>
>>> ##this command to know what is the type of Data[4]. in the Data[4] is Name.
>>> Data[4][5]
'e'
>>> ##beacuse there is e in fifth object.
>>> Data[4][a:6]
'Motwke'
>>> ##beacuse Data[4] is Name.
>>> Data[0] = 'ok'; Data
['ok', 70, 1.71, 220, 'Motwkel Mhmoud Mohmed Adam']
>>> ##beacuse the first to changed with 'ok'
>>> Data[-a]
'ok'
>>> ##beause the first in the Data is ok.
>>> range(a)
range(0, 0)
>>> ##beause in the "a" Data there is 0 object.
