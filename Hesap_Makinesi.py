from tkinter import *

pencere = Tk()
pencere.geometry("400x400+300+100")
pencere.title("Hesap Makinesi")
pencere.resizable(FALSE, FALSE)

depo = ""

def hesapla(tus):
    global depo
    if str(tus) in "0123456789":  # tus'u karakter dizisine dönüştürüyoruz
        ekran.insert(END, tus)
        depo = depo + str(tus)
    if tus in "+-/*":
        ekran.insert(END, tus)
        depo += tus
    if tus == "=":
        ekran.delete(0, END)
        hesap = eval(depo, {"__builtins__": None}, {})
        depo = str(hesap)
        ekran.insert(END, depo)
    if tus == "C":
        ekran.delete(0, END)
        depo = ""

ekran = Entry(width=40, justify=RIGHT)
ekran.grid(row=0, column=0, columnspan=3, ipady=4)

liste = ["C", " ", " ", "/", "7", "8", "9", "*", "4", "5", "6", "-", "1", "2", "3", "+", "0", " ", " ", "="]

sira = 1
sutun = 0

for i in liste:
    komut = lambda x=i: hesapla(x)  
    Button(text=i, font="verdana 8 bold", width=10, height=2, relief=GROOVE, command=komut).grid(row=sira, column=sutun)
    sutun += 1
    if sutun > 3:
        sutun = 0
        sira += 1

mainloop()
