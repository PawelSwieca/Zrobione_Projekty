from tkinter import *
from tkinter import ttk
from requests import get
from json import loads

POGODA_URL = "https://danepubliczne.imgw.pl/api/data/synop"
CITIES = ["Lublin", "Terespol", "Warszawa"]

ws = Tk()
ws.title('Pogoda 2023')
ws.geometry('500x500')
ws['bg'] = 'green'
pogoda_frame = Frame(ws)
scroll = Scrollbar(pogoda_frame)
scroll.pack(side=RIGHT, fill=Y)
my_pogoda = ttk.Treeview(pogoda_frame, xscrollcommand=scroll.set)
my_pogoda['columns'] = ['nazwa_miasta', 'godzina_pomiaru', 'temeratura']
response = get(POGODA_URL)

def add1():
    global count
    citeis_num = len(CITIES)
    for row in loads(response.text):
        if row["stacja"] in CITIES:
            msto = row['stacja']
            gpo = row['godzina_pomiaru']
            tem = row['temperatura']
    data_list.clear()
    if citeis_num > 0:
        data_list.append((msto, gpo, tem))
        citeis_num -= 1
    else:
        exit("Wypisalem dane wszystkich miast, ktore Cie interesowaly.")
    for item in data_list:
        my_pogoda.insert(parent='', index='end', iid=count, text=f'{count + 1}', values=(item))
        CITIES.remove(msto)
    count += 1


global count
count = 0

my_pogoda.column("#0", width=0, stretch=NO)
my_pogoda.column("nazwa_miasta", anchor=CENTER, width=80)
my_pogoda.column("godzina_pomiaru", anchor=CENTER, width=150)
my_pogoda.column("temeratura", anchor=CENTER, width=80)

help_button = Button(ws, text="Pokaz dane miasta", width=30, command=add1, bg='yellow', activebackground='yellow')
help_button.place(x=140, y=226)


my_pogoda.heading("#0", text="", anchor=CENTER)
my_pogoda.heading("nazwa_miasta", text="Miasto", anchor=CENTER)
my_pogoda.heading("godzina_pomiaru", text="Godzina pomiaru", anchor=CENTER)
my_pogoda.heading("temeratura", text="Temperatura", anchor=CENTER)

data_list = []

my_pogoda.pack()
pogoda_frame.pack()
ws.mainloop()
