# 1405 deplacement balle.py
from tkinter import *
from math import *


def avance(balle, x, y, x1, y1, x2, y2, x3, y3, x4, y4, dx, dy, rayon, largeur, hauteur):
    # fait déplacer la balle horizontalement ou verticalemnt
    avancer = 0
    x, y = x + dx, y + dy
    if x + rayon + dx > largeur:
        avancer = 1  # arret à la largeur
    if x < x1:
        y = y
    if x == x1:  # deuxième point vertical haut
        dx, dy = 5, -5
        if y == y1 : dx, dy = 5, -5
    if x > x2 and x < x3: y = y2   # horizontal vers troisième point
    if x == x3:                # quatrième point point vertical bas
        dx, dy = 5, 5
        if y == y3: dx, dy = 5, 5 # cinquième point
    if x > x4: y = y4  # horizontal
    can.coords(balle, x - rayon, y - rayon, x + rayon, y + rayon)
    if avancer == 0:
        fenetre.after(20, lambda: avance(balle, x, y, x1, y1, x2, y2, x3, y3, x4, y4, dx, dy, rayon, largeur, hauteur))


def lancer_balle(x, y, x1, y1, x2, y2, x3, y3, x4, y4, dx, dy, rayon, largeur, hauteur, couleur):
    # création de la balle et lancement
    balle = can.create_oval(x, y, x + rayon, y + rayon, fill=couleur)
    avance(balle, x, y, x1, y1, x2, y2, x3, y3, x4, y4, dx, dy, rayon, largeur, hauteur)


# -------------programme principal --------------------------------#
fenetre = Tk()
fenetre.title("Déplacement Balle")
#fenetre.iconbitmap("logo-isn.ico")
# largeur=fenetre.winfo_screenwidth()-120
largeur = 1000
# hauteur=fenetre.winfo_screenheight()-200
hauteur = 500
fenetre.geometry(str(largeur) + 'x' + str(hauteur + 80))
fenetre.configure(bg='light blue')
couleur = 'red'
x, y, x1, y1, x2, y2, x3, y3, x4, y4, dx, dy, rayon = 0, 300, 250, 300, 300, 170, 500, 170, 560, 300, 5, 0, 30
can = Canvas(fenetre, width=largeur, height=hauteur, bg='ivory')
can.grid(row=0, column=0, columnspan=2)
mur = can.create_rectangle(300, 200, 500, 330, width=5, fill='green', outline='black')
sol = can.create_rectangle(0, 330, largeur, 330, fill='green', width=5)
b = Button(fenetre, text='Balle rouge', font='verdana 12 bold', fg='red', command=lambda: lancer_balle(x, y, x1, y1, x2, y2, x3, y3, x4, y4, dx, dy, rayon, largeur, hauteur, couleur))
b.grid(row=1, column=0)
fenetre.mainloop()