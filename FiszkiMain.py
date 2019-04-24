from random import randrange
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
import copy
import codecs

def WyswietlSlowa(event):
    listaSlow = []
    saveMe = codecs.open("Slowa1D.txt", "a",'UTF-8')
    saveMe.truncate(0)
    # Wczytanie pliku
    filename = askopenfilename()
    with open(filename, 'r', encoding='UTF-8') as inputfile:
        for line in inputfile:
            listaSlow.append(line.strip().split(";"))

# losowanie par słów i zapis do pliku
    i = 0
    kopiaKonsolaPowtorka = copy.copy(konsolaUczNowe.get("1.31", "end-1c"))
    konsolaUczNowe.delete("1.0", "end-1c")
    while i < int(kopiaKonsolaPowtorka):
        rand = randrange(0, listaSlow.__len__())
        konsolaUczNowe.insert(INSERT, listaSlow.__getitem__(rand).__getitem__(0) + ' - ' + listaSlow.__getitem__(rand).__getitem__(1) + "\n")
        saveMe.write(listaSlow.__getitem__(rand).__getitem__(0) + ' - ' + listaSlow.__getitem__(rand).__getitem__(1)+";")
        i += 1
    konsolaUczNowe['state'] = 'disable'

def Powtorz(event):
    listaPowtorka=[]
    konsolaUczNowe.delete("1.0", END)
    with open("Slowa1D.txt",'r',encoding="UTF-8") as inputfile:
        for line in inputfile:
            listaPowtorka.append(line.strip().split(";"))
    i=0
    while listaPowtorka.__getitem__(0).__getitem__(i):
        konsolaUczNowe.insert(INSERT, listaPowtorka.__getitem__(0).__getitem__(i)+"\n")
        i+=1
#GUI
root = tk.Tk()
root.title("FiszkiPY")

buttonPowtorka = Button(root,text="Powtórka", width=20, height=26)
buttonPowtorka.pack(side=RIGHT)
buttonPowtorka.bind("<Button-1>", Powtorz)

konsolaUczNowe = tk.Text(root, height=25, width=60)
konsolaUczNowe.bind("<Return>", WyswietlSlowa)
konsolaUczNowe.pack()
konsolaUczNowe.insert("1.0","Podaj liczbe słów do powtórki: ")
root.mainloop()



