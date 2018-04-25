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
#fenetre.geometry(largeurxhauteur)
#fenetre.attributes('-fullscreen', 1)
fenetre.title("Simulation Fahrzeugen")



# Creation Interface
for user in tree.xpath("/parameter/rectbouton/lang"):
    langrectb = user.text
for user in tree.xpath("/parameter/rectbouton/hohe"):
    hoherectb = user.text

Frame0 = Frame(fenetre,borderwidth=0,relief=GROOVE, width=langrectb, height=hoherectb)
Frame0.pack(padx=0,pady=0)

#fin de la fenetre principale


for user in tree.xpath("/parameter/rectgreen/lang"):
    langerect1 = user.text
for user in tree.xpath("/parameter/rectgreen/hohe"):
    hoherect1 = user.text
Frame1 = Frame(fenetre,borderwidth=0,relief=GROOVE, width=langerect1, height=hoherect1, bg="lime")
Frame1.pack(padx=0,pady=0)


#fin de la creation de la 1ere bordure verte

for user in tree.xpath("/parameter/linerect/lang"):
    langeline1 = user.text
for user in tree.xpath("/parameter/linerect/hohe"):
    hoheline1 = user.text
line1 = Frame(fenetre,borderwidth=0,relief=GROOVE, width=langeline1, height=hoheline1, bg="white")
line1.pack(padx=0,pady=0)

#fin de la creation du 1er espacement



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


def deplacement():
    global dx, dy,mytest,ve,V
    # On deplace la balle :
    c = dx/V*1000
    ve =round(c,2)

    moveCarAndRadar(dx, dy)

    detectObstacle(V)
    # On repete cette fonction
    fenetre.after(V, deplacement)

#fonction qui permet de deplacer l'ensemble (car + radar)

def moveCarAndRadar(x,y):
    Frame2.move(raquette, x, y)
    Frame2.move(sensor1, x, y)
    Frame2.move(sensor2, x, y)
    Frame2.move(sensor3, x, y)
    Frame2.move(arc, x, y)
    Frame2.move(text, x, y)

def changeDirection(fx,fy,V):
    old =V
    V=old *2/3

    Frame2.move(raquette, fx, fy)
    Frame2.move(sensor1, fx, fy)
    Frame2.move(sensor2, fx, fy)
    Frame2.move(sensor3, fx, fy)
    Frame2.move(arc, fx, fy)
    Frame2.move(text, fx, fy)


def detectObstacle(V):

    if(mytest ==0):
        Frame2.itemconfigure(text, text="radar on")
    if (Frame2.coords(arc)[3] > Frame2.coords(rects)[1]) and (
            Frame2.coords(arc)[0] < Frame2.coords(rects)[2]) and (
            Frame2.coords(arc)[2] > Frame2.coords(rects)[0]):
        distance = Frame2.coords(rects)[0]-Frame2.coords(arc)[2] +125
        dis = round(distance, 2)

        t = "obstacle no 1 à " + str(dis)
        Frame2.itemconfigure(text, text=t)
        changeDirection(0, -1,V)

    else:
        if (Frame2.coords(sensor1)[3] > Frame2.coords(rects)[1]) and (
                Frame2.coords(sensor1)[0] < Frame2.coords(rects)[2]) and (
                Frame2.coords(sensor1)[2] > Frame2.coords(rects)[0]):
            distance = Frame2.coords(rects)[0] - Frame2.coords(sensor1)[2] + 100
            dis = round(distance, 2)

            t = "obstacle no 1 à " + str(dis)
            Frame2.itemconfigure(text, text=t)
            changeDirection(0, 1, V)

        else:
            if (Frame2.coords(sensor2)[3] > Frame2.coords(rects)[1]) and (
                    Frame2.coords(sensor2)[0] < Frame2.coords(rects)[2]) and (
                    Frame2.coords(sensor2)[2] > Frame2.coords(rects)[0]):
                distance = Frame2.coords(rects)[0] - Frame2.coords(sensor2)[2] + 100
                dis = round(distance, 2)

                t = "obstacle no 1 à " + str(dis)
                Frame2.itemconfigure(text, text=t)
                changeDirection(0, -1, V)

            else:
                if (Frame2.coords(sensor3)[3] > Frame2.coords(rects)[1]) and (
                        Frame2.coords(sensor3)[0] < Frame2.coords(rects)[2]) and (
                        Frame2.coords(sensor3)[2] > Frame2.coords(rects)[0]):
                    distance = Frame2.coords(rects)[0] - Frame2.coords(sensor3)[2] + 100
                    dis = round(distance, 2)

                    t = "obstacle no 1 à " + str(dis)
                    Frame2.itemconfigure(text, text=t)
                    changeDirection(0, -1, V)








    if (Frame2.coords(arc)[3] > Frame2.coords(baustelle)[1]) and (
            Frame2.coords(arc)[0] < Frame2.coords(baustelle)[2]) and (
            Frame2.coords(arc)[2] > Frame2.coords(baustelle)[0]):
        distance = Frame2.coords(baustelle)[0] - Frame2.coords(arc)[2]+125
        dis = round(distance, 2)
        t = "obstacle no 2 à " + str(dis)

        Frame2.itemconfigure(text, text=t)
        changeDirection(0, -1, V)
    else:
        if (Frame2.coords(sensor1)[3] > Frame2.coords(baustelle)[1]) and (
                Frame2.coords(sensor1)[0] < Frame2.coords(baustelle)[2]) and (
                Frame2.coords(sensor1)[2] > Frame2.coords(baustelle)[0]):
            distance = Frame2.coords(baustelle)[0] - Frame2.coords(sensor1)[2] + 100
            dis = round(distance, 2)

            t = "obstacle no 2 à " + str(dis)
            Frame2.itemconfigure(text, text=t)
            changeDirection(0, -1, V)

        else:
            if (Frame2.coords(sensor2)[3] > Frame2.coords(baustelle)[1]) and (
                    Frame2.coords(sensor2)[0] < Frame2.coords(baustelle)[2]) and (
                    Frame2.coords(sensor2)[2] > Frame2.coords(baustelle)[0]):
                distance = Frame2.coords(baustelle)[0] - Frame2.coords(sensor2)[2] + 100
                dis = round(distance, 2)

                t = "obstacle no 2 à " + str(dis)
                Frame2.itemconfigure(text, text=t)
                changeDirection(0, -1, V)

            else:
                if (Frame2.coords(sensor3)[3] > Frame2.coords(baustelle)[1]) and (
                        Frame2.coords(sensor3)[0] < Frame2.coords(baustelle)[2]) and (
                        Frame2.coords(sensor3)[2] > Frame2.coords(baustelle)[0]):
                    distance = Frame2.coords(baustelle)[0] - Frame2.coords(sensor3)[2] + 100
                    dis = round(distance, 2)

                    t = "obstacle no 2 à " + str(dis)
                    Frame2.itemconfigure(text, text=t)
                    changeDirection(0, -1, V)




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

    if (Frame2.coords(arc)[3] > Frame2.coords(baustelle)[1]) and (
            Frame2.coords(arc)[0] < Frame2.coords(baustelle)[2]) and (
            Frame2.coords(arc)[2] > Frame2.coords(baustelle)[0]):

        print ("obstacle 2")
        Frame2.itemconfigure(text, text="obstacle 2")



    #Frame2.itemconfigure(text, text="hello")





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

    if (Frame2.coords(arc)[3] > Frame2.coords(baustelle)[1]) and (
            Frame2.coords(arc)[0] < Frame2.coords(baustelle)[2]) and (
            Frame2.coords(arc)[2] > Frame2.coords(baustelle)[0]):
        print ("obstacle 2")
        Frame2.itemconfigure(text, text="obstacle 2")


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

    if (Frame2.coords(arc)[3] > Frame2.coords(baustelle)[1]) and (
            Frame2.coords(arc)[0] < Frame2.coords(baustelle)[2]) and (
            Frame2.coords(arc)[2] > Frame2.coords(baustelle)[0]):
        print ("obstacle 2")
        Frame2.itemconfigure(text, text="obstacle 2")


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

#creation de la route
Frame2 = Canvas(fenetre, borderwidth=0, relief=GROOVE, width=langstr, height=hohestr, bg ='grey')
Frame2.pack(padx =0, pady =0)
c, r=0.25, 0

#creation des separations de la route
while c<40:
    Frame2.create_rectangle((2*c*39, 69), ((2*c+1)*39, 71), fill='white', width=0) #on crée le premier carré, puis le deuxième, et ainsi de suite...
    Frame2.create_rectangle((2 * c * 39, 139), ((2 * c + 1) * 39, 141), fill='white', width=0)                                                             #on passe à al ligne suivante
    c=c+1
    #rect1 = Frame2.create_rectangle(0, 198, 30, 198, outline="white", fill="white", width=10)
   # rect2 = Frame2.create_line(0, 67, 800, 67, fill='white', dash=(100, 100, 100, 100))

# Alerte
#creation de l'obstacle

#stop = Frame2.create_rectangle(335,hohestr,345,200,fill='red', outline='red')
#stop1 = Frame2.create_rectangle(335,200,345,190,fill='white', outline='white')
#stop2 = Frame2.create_rectangle(335,190,345,180, fill='red', outline='red')
#stop3 = Frame2.create_rectangle(335,180,345,170,fill='white', outline='white')
#stop4 = Frame2.create_rectangle(330,171,345,160, fill='red', outline='red')
rects = Frame2.create_rectangle(340, 168, 345, 200, outline="red", fill="blue", width=2)
#cercle = Frame2.create_oval(334,163,347,152, fill='orange', outline="White")

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
baustelle = Frame2.create_arc(590, b2,b3,b4, start=d1, extent=f1, fill='red')


#fin de #creation du deuxième obstacle



#On cree un object Car:


photo = PhotoImage(file="red_car.png")

raquette = Frame2.create_image(0,150, anchor=NW, image=photo)

#raquette = Frame2.create_rectangle(0,160,45,190,fill='yellow')

angle_in_radians = -15 * math.pi / 180
angle_in_radians2 = 15 * math.pi / 180
line_length = 105
center_x = 60
center_y = 165
end_x = center_x + line_length * math.cos(angle_in_radians)
end_y = center_y + line_length * math.sin(angle_in_radians)
end_x2 = center_x + line_length * math.cos(angle_in_radians2)
end_y2 = center_y + line_length * math.sin(angle_in_radians2)
sensor1 = Frame2.create_line(60, 165, end_x ,end_y, fill='white')
sensor2 = Frame2.create_line(60, 165, 160,165, fill='white')
sensor3 = Frame2.create_line(60, 165, end_x2,end_y2,fill='white')
text=Frame2.create_text(85, 175, text="20 m", anchor=SW, font="italic")








arc = Frame2.create_arc(end_x+25, end_y, end_x2-25, end_y2, start=-90, dash=(3, 5), extent=180, outline='white')



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

dx=1.7
dy=0
mytest = 0
V=100



deplacement()




fenetre.mainloop()
