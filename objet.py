from tkinter import *

fenetre = Tk()


can = Canvas(fenetre, borderwidth=0, relief=GROOVE, width=500, height=300, bg ='grey')
can.pack(padx =0, pady =0)
rect = can.create_rectangle(40, 50, 100, 80, fill='yellow')

fenetre.mainloop()