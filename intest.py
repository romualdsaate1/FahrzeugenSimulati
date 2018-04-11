import random
from tkinter import *
import os
import math


from lxml import etree



tree = etree.parse("parameter.xml")
root = tree.getroot()


# Création de la fenêtre principale

largeur = 800
hauteur1 = 506
hauteur = 200
fenetre = Tk()
#fenetre.geometry("800x516")
#fenetre.attributes('-fullscreen', 1)
fenetre.title("Simulation Fahrzeugen")

#fenetre.geometry(str(largeur)+ 'x' +str(hauteur1+20))

couleur= 'yellow'


"""
def avance(car, x, y, x1, y1, x2, y2, x3, y3, x4, y4, dx, dy, carlang, largeur, hauteur):
    # fait déplacer la balle horizontalement ou verticalemnt
    avancer = 0
    x, y = x + dx, y + dy
    if x + carlang + dx > largeur:
        avancer = 1  # arret à la largeur
    if x < x1:
        y = y

    if x == x1 and x < x2 :  # deuxième point vertical haut
        dx, dy = 1, -0.5
        if y == y1 and y < y2: dx, dy = 1, -0.5
    if x > x2 and x < x3: y = y2   # horizontal vers troisième point
    if x == x3:                # quatrième point point vertical bas
        dx, dy = 1, 1
        if y == y3: dx, dy = 1, 1 # cinquième point
    if x > x4: y = y4  # horizontal
    Frame2.coords(car, x - carlang, y - carlang, x + carlang, y + carlang)
    if avancer == 0:
        Frame2.after(20, lambda: avance(car, x, y, x1, y1, x2, y2, x3, y3, x4, y4, dx, dy, carlang, largeur, hauteur))

def lancer_car(x, y, x1, y1, x2, y2, x3, y3, x4, y4, dx, dy, carlang, largeur, hauteur, couleur):
    # création de la balle et lancement
    photo = PhotoImage(file="car.png")
    car = Frame2.create_image(0, 150, anchor=NW, image=photo)
    avance(car, x, y, x1, y1, x2, y2, x3, y3, x4, y4, dx, dy, carlang, largeur, hauteur)
"""



# Creation Interface
for user in tree.xpath("/parameter/rectbouton/lang"):
    langrectb = user.text
for user in tree.xpath("/parameter/rectbouton/hohe"):
    hoherectb = user.text

Frame0 = Frame(fenetre,borderwidth=0,relief=GROOVE, width=langrectb, height=hoherectb)
Frame0.pack(padx=0,pady=0)

Button(Frame0,text="Start",fg='navy',command=lambda: lancer_car(x, y, x1, y1, x2, y2, x3, y3, x4, y4, dx, dy, carlang, largeur, hauteur, couleur)).pack(side=LEFT, padx=10,pady=10)
Button(Frame0,text="Pause",fg='navy',command=Frame0.destroy).pack(side=LEFT, padx=10,pady=10)
Button(Frame0,text="Reset",fg='navy',command=Frame0.destroy).pack(side=RIGHT, padx=10,pady=10)


for user in tree.xpath("/parameter/rectgreen/lang"):
    langerect1 = user.text
for user in tree.xpath("/parameter/rectgreen/hohe"):
    hoherect1 = user.text
Frame1 = Frame(fenetre,borderwidth=0,relief=GROOVE, width=langerect1, height=hoherect1, bg="lime")
Frame1.pack(padx=0,pady=0)

for user in tree.xpath("/parameter/linerect/lang"):
    langeline1 = user.text
for user in tree.xpath("/parameter/linerect/hohe"):
    hoheline1 = user.text
line1 = Frame(fenetre,borderwidth=0,relief=GROOVE, width=langeline1, height=hoheline1, bg="white")
line1.pack(padx=0,pady=0)



#Une fonction pour le deplacement vers la droite :


"""
dx=0
dy=0
def deplacement():
    global dx, dy
    if Frame2.coords(raquette)[0] > 780:
        dx = -1 * dx
    if Frame2.coords(raquette)[0] < 50:
        dx = -1 * dx
    if Frame2.coords(raquette)[1] > 200:
        dy = -1 * dy
    if Frame2.coords(raquette)[1] < 30:
        dy = -1 * dy
    # On deplace la balle :
    Frame2.move(raquette, dx, dy)
    # On repete cette fonction
    Frame2.after(20, deplacement)
"""

# Une fonction pour modifier le deplacement vers la droite :
def droite(event):
   # if Frame2.coords(raquette[0] < 200):
        global dx, dy
        dx = 1
        dy = 0
def droite(event):
    Frame2.move(raquette,10,0)
    Frame2.move(sensor1, 10, 0)
    Frame2.move(sensor2, 10, 0)
    Frame2.move(sensor3, 10, 0)
    Frame2.move(arc, 10, 0)
    Frame2.move(text, 10, 0)

def gauche(event):
    global dx, dy
    dx = -1
    dy = 0
def gauche(event):
    Frame2.move(raquette,-10,0)
    Frame2.move(sensor2, -10, 0)
    Frame2.move(sensor1, -10, 0)
    Frame2.move(sensor3, -10, 0)
    Frame2.move(arc, -10, 0)
    Frame2.move(text, -10, 0)

def haut(event):
    global dx, dy
    dx = 0
    dy = -1
def haut(event):
    Frame2.move(raquette,0,-10)
    Frame2.move(sensor1, 0, -10)
    Frame2.move(sensor2, 0, -10)
    Frame2.move(sensor3, 0, -10)
    Frame2.move(arc, 0, -10)
    Frame2.move(text, 0, -10)

def bas(event):
    global dx, dy
    dx = 0
    dy = 1
def bas(event):
    Frame2.move(raquette,0,10)
    Frame2.move(sensor3, 0, 10)
    Frame2.move(sensor2, 0, 10)
    Frame2.move(sensor1, 0, 10)
    Frame2.move(arc, 0, 10)
    Frame2.move(text, 0, 10)

def tour(event):
    Frame2.move(raquette,10,5)
def mont(event):
    Frame2.move(raquette,10,-10)

for user in tree.xpath("/parameter/car/carlang"):
    carlang = user.text
for user in tree.xpath("/parameter/car/speedx"):
    dx = user.text
for user in tree.xpath("/parameter/car/speedy"):
    dy = user.text


#x,y,x1,y1,x2,y2,x3,y3,x4,y4,dx,dy,carlang=0,184,200,184,368,100,615,100,700,184,2,0,18

for user in tree.xpath("/parameter/strasse/langstrasse"):
    langstr = user.text
for user in tree.xpath("/parameter/strasse/hohestrasse"):
    hohestr = user.text
for user in tree.xpath("/parameter/strasse/langespuren"):
    langespuren = user.text

Frame2 = Canvas(fenetre, borderwidth=0, relief=GROOVE, width=langstr, height=hohestr, bg ='grey')
Frame2.pack(padx =0, pady =0)
c, r=0.25, 0
while c<40:
    Frame2.create_rectangle((2*c*39, 69), ((2*c+1)*39, 71), fill='white', width=0) #on crée le premier carré, puis le deuxième, et ainsi de suite...
    Frame2.create_rectangle((2 * c * 39, 139), ((2 * c + 1) * 39, 141), fill='white', width=0)                                                             #on passe à al ligne suivante
    c=c+1
    #rect1 = Frame2.create_rectangle(0, 198, 30, 198, outline="white", fill="white", width=10)
   # rect2 = Frame2.create_line(0, 67, 800, 67, fill='white', dash=(100, 100, 100, 100))

# Alerte

stop = Frame2.create_rectangle(335,hohestr,345,200,fill='red', outline='red')
stop1 = Frame2.create_rectangle(335,200,345,190,fill='white', outline='white')
stop2 = Frame2.create_rectangle(335,190,345,180, fill='red', outline='red')
stop3 = Frame2.create_rectangle(335,180,345,170,fill='white', outline='white')
#stop4 = Frame2.create_rectangle(330,171,345,160, fill='red', outline='red')
rects = Frame2.create_rectangle(340, 168, 340, 163, outline="red", fill="red", width=2)
cercle = Frame2.create_oval(334,163,347,152, fill='orange', outline="White")

# Les lignes

coords = [(0,600), (100,348), (88,348), (0,251)]
li1=Frame2.create_line(225,211,355,135,600,135,670,211,fill='orange')
li2=Frame2.create_line(210,140,355,75,640,75,700,140,fill='orange')

# Create object Baustelle
for user in tree.xpath("/parameter/baustelle/pos_x0"):
    b1= user.text
for user in tree.xpath("/parameter/baustelle/pos_y0"):
    b2= user.text
for user in tree.xpath("/parameter/baustelle/finpos_x0"):
    b3= user.text
for user in tree.xpath("/parameter/baustelle/finpos_x0"):
    b4= user.text
for user in tree.xpath("/parameter/baustelle/debut"):
    d1= user.text
for user in tree.xpath("/parameter/baustelle/fin"):
    f1= user.text
baustelle = Frame2.create_arc(b1, b2,b3,b4, start=d1, extent=f1, fill='red')


#Frame2.create_arc((280,280), (60,60), fill='red',
 #                 start=10, extent=70, style='pieslice')
#Construction du radar
xy = 40, 40, 300, 260
#Frame2.create_arc(xy, start=0, extent=270, fill="red")
#Frame2.create_arc(xy, start=270, extent=60, fill="blue")
#Frame2.create_arc(xy, start=335, extent=65, fill="green")

#On cree un object Car:
for user in tree.xpath("/parameter/car/pos_x0"):
    a0= user.text
for user in tree.xpath("/parameter/car/pos_y0"):
    b0= user.text
for user in tree.xpath("/parameter/car/coleur"):
    coleur= user.text
for user in tree.xpath("/parameter/car/pos_y1"):
    z1= user.text

#photo = PhotoImage(file="car.png")
#raquette = Frame2.create_image(0,150, anchor=NW, image=photo)
raquette = Frame2.create_rectangle(0,160,45,190,fill='yellow')
sensor1 = Frame2.create_line(44, 175, 144,145, fill='white')
sensor2 = Frame2.create_line(44, 175, 164,175, fill='white')
sensor3 = Frame2.create_line(44, 175, 144,205,fill='white')
text=Frame2.create_text(85, 175, text="20m2", anchor=SW, font="italic")


arc = Frame2.create_arc(126, 145, 164, 205, start=-90, dash=(3, 5), extent=180, outline='white')



#On associe la touche droite du clavier a la fonction droite():
Frame2.bind_all('<Right>', droite)
Frame2.bind_all('<Left>', gauche)
Frame2.bind_all('<Up>', haut)
Frame2.bind_all('<Down>', bas)
Frame2.bind_all('<u>', tour)
Frame2.bind_all('<o>', mont)





line2 = Frame(fenetre,borderwidth=0,relief=GROOVE, width=langeline1, height=hoheline1, bg="white")
line2.pack(padx=0,pady=0)

Frame3 = Frame(fenetre,borderwidth=0,relief=GROOVE, width=langerect1, height=hoherect1, bg="lime")
Frame3.pack(padx=0,pady=0)


for user in tree.xpath("/parameter/frameechelle/lang"):
    langechel = user.text
for user in tree.xpath("/parameter/frameechelle/hohe"):
    hoheechel = user.text

Frame4 = Frame(fenetre,borderwidth=0,relief=GROOVE, width=langechel, height=hoheechel)
Frame4.pack(padx=0,pady=0)

def maj(nouvelleValeur):
    # nouvelle valeur en argument
    print(nouvelleValeur)
def plus():
    Valeur.set(str(int(Valeur.get())+10))
    print(Valeur.get())
def moins():
    Valeur.set(str(int(Valeur.get())-10))
    print(Valeur.get())
Valeur = StringVar()
Valeur.set(50)


# Création d'un widget Scale
#echelle1 = Scale(fenetre,from_=0,to=200,resolution=50,orient=VERTICAL, length=200,width=10,label="Min_Distance",tickinterval=10,variable=Valeur,command=maj)
#echelle1.pack(side=LEFT, padx=0,pady=0)
echelle2 = Scale(Frame4,from_=0,to=200,resolution=10,orient=VERTICAL, length=200,width=10,label="Min_Distance",tickinterval=20,variable=Valeur,command=maj)
echelle2.pack(side=LEFT, padx=0,pady=0)
echelle2 = Scale(Frame4,from_=0,to=1600,resolution=100,orient=VERTICAL, length=200,width=10,label="D_Speed",tickinterval=200,variable=Valeur,command=maj)
echelle2.pack(side=LEFT, padx=0,pady=0)
echelle3 = Scale(Frame4,from_=0,to=60,resolution=10,orient=VERTICAL, length=200,width=10,label="Max_Acceleration",tickinterval=10,variable=Valeur,command=maj)
echelle3.pack(side=LEFT, padx=0,pady=0)
echelle4 = Scale(Frame4,from_=0,to=60,resolution=10,orient=VERTICAL, length=200,width=10,label="Conf_Deccel",tickinterval=10,variable=Valeur,command=maj)
echelle4.pack(side=LEFT, padx=0,pady=0)
echelle5 = Scale(Frame4,from_=0,to=60,resolution=10,orient=VERTICAL, length=200,width=10,label="Time_Dist",tickinterval=10,variable=Valeur,command=maj)
echelle5.pack(side=LEFT, padx=0,pady=0)
echelle6 = Scale(Frame4,from_=0,to=16,resolution=4,orient=VERTICAL, length=200,width=10,label="Delta",tickinterval=4,variable=Valeur,command=maj)
echelle6.pack(side=LEFT, padx=0,pady=0)
#echelle7 = Scale(fenetre,from_=0,to=60,resolution=10,orient=VERTICAL, length=200,width=10,label="N_Cars",tickinterval=10,variable=Valeur,command=maj)
#echelle7.pack(side=RIGHT, padx=0,pady=0)




fenetre.mainloop()
