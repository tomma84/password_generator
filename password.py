from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import random
import numpy as np

def genera():
    if lunghezza.get() and (maiuscole.get() or minuscole.get() or numeri.get() or speciali.get()):
        caratteri_minuscoli = 'qwertyuiopasdfghjklzxcvbnm'
        caratteri_maiuscoli = 'QWERTYUIOPASDFGHJKLZXCVBNM'
        caratteri_numerici = '1234567890'
        caratteri_speciali = '!$&./@€_'

        caratteri_in_uso = ''

        nuova_password = ''

        if minuscole.get():
            nuova_password += caratteri_minuscoli[np.random.randint(len(caratteri_minuscoli))]
            caratteri_in_uso += caratteri_minuscoli

        if maiuscole.get():
            nuova_password += caratteri_maiuscoli[np.random.randint(len(caratteri_maiuscoli))]
            caratteri_in_uso+= caratteri_maiuscoli

        if numeri.get():
            nuova_password += caratteri_numerici[np.random.randint(len(caratteri_numerici))]
            caratteri_in_uso+= caratteri_numerici 

        if speciali.get():
            nuova_password += caratteri_speciali[np.random.randint(len(caratteri_speciali))]
            caratteri_in_uso+= caratteri_speciali
        
        while len(nuova_password) < lunghezza.get():
            nuova_password += caratteri_in_uso[np.random.randint(len(caratteri_in_uso))]

        testo = list(nuova_password)
        random.shuffle(testo)
        testo = ''.join(testo)
        password.set(testo)
    else:
        showerror("Errore", "Seleziona un tipo di carattere e una dimensione")


root = Tk()

root.title('Password Generator')

root.resizable(width=False, height=False)

contenitore = Frame(root)
contenitore.grid(column=0, row=0)

Label(contenitore, text='Password').grid(column=0, row=0)

password = StringVar()
password_entry = Entry(contenitore, textvariable=password, width=30)
password_entry.grid(column=1, row=0)

pulsante_genera = Button(contenitore, text='Genera', command=genera)
pulsante_genera.grid(column=2, row=0)

frame_opzioni = LabelFrame(contenitore, text='Opzioni')
frame_opzioni.grid(column=0, row=1, columnspan=3)

minuscole = BooleanVar()
maiuscole = BooleanVar()
numeri = BooleanVar()
speciali = BooleanVar()

Label(frame_opzioni, text='Set Caratteri').grid(column=0, row=0, padx=(0, 20))
minuscole_opt = Checkbutton(frame_opzioni, text='minuscole', variable=minuscole)
minuscole_opt.grid(column=0, row=1, sticky='W')
maiuscole_opt = Checkbutton(frame_opzioni, text='maiuscole', variable=maiuscole)
maiuscole_opt.grid(column=0, row=2, sticky='W')
numeri_opt = Checkbutton(frame_opzioni, text='numeri', variable=numeri)
numeri_opt.grid(column=0, row=3, sticky='W')
speciali_opt = Checkbutton(frame_opzioni, text='speciali', variable=speciali)
speciali_opt.grid(column=0, row=4, sticky='W')

lunghezza = IntVar()

lunghezza_8 = Radiobutton(frame_opzioni, text=8, variable=lunghezza, value=8)
lunghezza_10 = Radiobutton(frame_opzioni, text=10, variable=lunghezza, value=10)
lunghezza_16 = Radiobutton(frame_opzioni, text=16, variable=lunghezza, value=16)
lunghezza_20 = Radiobutton(frame_opzioni, text=20, variable=lunghezza, value=20)
Label(frame_opzioni, text='Lunghezza').grid(column=1, row=0)
lunghezza_8.grid(column=1, row=1, sticky='W')
lunghezza_10.grid(column=1, row=2, sticky='W')
lunghezza_16.grid(column=1, row=3, sticky='W')
lunghezza_20.grid(column=1, row=4, sticky='W')

root.mainloop()