import os
os.system("cls")

from math import *

a = int(input("Zarzuć jakąś liczbą Ziomo:"))
b = int(input("Zarzuć jeszcze jedną ploxik: "))
print("To są Twoje liczby Brachu: ", a, " oraz ", b)

dodawanie = a+b
odejmowanie = a-b
mnozenie = a*b

if b==0:
    print("Ty no, ale przez zero to się nie uda Mistrzuniu :/")
else:
    dzielenie = a/b
print("Dodawanie ", dodawanie, " odejmowanie ", odejmowanie, " mnożenie ", mnozenie, " dzielenie", dzielenie)
