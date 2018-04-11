from tkinter import *

fenetre = Tk()

fenetre['bg']='white'

# frame 1
Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack(side=LEFT, padx=300, pady=200)

# frame 2
Frame2 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame2.pack(side=LEFT, padx=10, pady=10)

# frame 3 dans frame 2
Frame3 = Frame(Frame2, bg="white", borderwidth=2, relief=GROOVE)
Frame3.pack(side=RIGHT, padx=5, pady=5)

# Ajout de labels
Label(Frame1, text="Frame 1").pack(padx=300, pady=80)
Label(Frame2, text="Frame 2").pack(padx=10, pady=10)
Label(Frame3, text="Frame 3",bg="white").pack(padx=10, pady=10)


for ligne in range(5):
    for colonne in range(5):
        Button(fenetre, text='L%s-C%s' % (ligne, colonne), borderwidth=1).grid(row=ligne, column=colonne)
    Button(fenetre, text='L1-C1', borderwidth=1).grid(row=1, column=1)
    Button(fenetre, text='L1-C2', borderwidth=1).grid(row=1, column=2)
    Button(fenetre, text='L2-C3', borderwidth=1).grid(row=2, column=3)
    Button(fenetre, text='L2-C4', borderwidth=1).grid(row=2, column=4)
    Button(fenetre, text='L3-C3', borderwidth=1).grid(row=3, column=3)

fenetre.mainloop()