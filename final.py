import random
import tkinter as tk
from tkinter import *
import os
import math
from lxml import etree

import matplotlib as mpl
import numpy as np
import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_agg import FigureCanvasAgg

#get setup file
tree = etree.parse("setup.xml")
root = tree.getroot()


# Create main screen


fenetre = Tk()

#main screen title
fenetre.title("Simulation Fahrzeugen")


# main Frame creation


for elt in tree.xpath("/parameter/rectbouton/lang"):
    langrectb = elt.text
for elt in tree.xpath("/parameter/rectbouton/hohe"):
    hoherectb = elt.text

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

def resetPosition():
    if(Frame2.coords(raquette)[0] > 1085 and Frame2.coords(raquette)[1] <165):
        changeDirection(0.1, 0.9, T)

def deplacement():
    global dx, dy,ve,T
    # On deplace la balle :



    moveCarAndRadar(dx, dy)

    #distance = Frame2.coords(rects)[0] - Frame2.coords(raquette)[0] -60
    #dis = round(distance, 2)

    detectObstacle()
    resetPosition()


    # On repete cette fonction
    fenetre.after(int(T), deplacement)

#fonction qui permet de deplacer l'ensemble (car + radar)

def moveCarAndRadar(x,y):

    Frame2.itemconfigure(vitesse, text=str(ve))#permet d'afficher la nouvelle vitesse
    Frame2.move(raquette, x, y)

    for el in rayon:
        Frame2.move(el, x, y)
        #Frame2.move(sensor2, x, y)
        #Frame2.move(sensor3, x, y)
   # Frame2.move(arc, x, y)
    Frame2.move(text, x, y)

"""
fx c'est la distance à laquelle on deplacera x et fy celle de y
T ici représente la nouvelle frequence d'affichage de la fenetre principale (elle permet de simuler le déplacement de la voiture) mais elle ne change pas.
"""

def changeDirection(fx,fy,T):
    old =T
    T=old *6

    if(T>0):
        c = (dx / T) * 1000
        ve = round(c, 2)
        Frame2.itemconfigure(vitesse, text=str(ve))



    Frame2.move(raquette, fx, fy)
    for el in rayon:
        Frame2.move(el, fx, fy)
    #Frame2.move(arc, fx, fy)
    Frame2.move(text, fx, fy)

"""
ici rayon est le tableau contenant tous les rayons du radar
tabOb est le tableau contenant tous les obstacles
li1 est la ligne rouge superieure collée à la route
li2 est la ligne rouge inférieure collée à la route
firstindex est la postion du rayon supérieur dans le tableau des rayons
lastindex est la postion du rayon inférieur dans le tableau des rayons

ces lignes me permettent de savoir de quel coté la voiture peut passer

la fonction fait ceci:

#1 pour chaque rayon contenu dans le tableau de rayon,
je regarde si l'extremité supérieure de mon rayon rencontre l'extremité gauche d'un obstacle et si l'extrémité inférieure 
 ne rencontre pas celle de l'obstacle(ceci se fait en regardant
l'axe des abscisses et ça me permet de savoir si la voiture est encore derrière l'obstacle)

#2 ensuite je calcule la distance entre le coté supérieur de la route et le coté inférieure de la route avec l'obstacle

 ensuite je determine par où la voiture doit passer

#3si la voiture doit passer par le haut:
  
  #4 je regarde d'abord si le rayon extreme est en dessous de l'obstacle:
    si oui, la voiture continue tout droit car elle ne rencontrera pas l'obstacle
    
    #5si non la voiture doit alors changer de direction.
    
le principe est pareil pour le bas
  



"""
def detectObstacle():



    Frame2.itemconfigure(text, text="radar on")

    for el in rayon:
        for ob in tabOb:
            if (Frame2.coords(el)[2] > Frame2.coords(ob)[0]) and (#1
                    Frame2.coords(el)[0] < Frame2.coords(ob)[2] + 60) :#1
                first = Frame2.coords(ob)[1] - Frame2.coords(li1)[1]#2
                second = Frame2.coords(li2)[1] - Frame2.coords(ob)[3]#2
                if (first > second):#3

                    if(Frame2.coords(rayon[firstindex])[3] > Frame2.coords(ob)[1])and(Frame2.coords(rayon[firstindex])[3] > Frame2.coords(ob)[3]):
                        te=1#4
                    else:
                        te=0#5
                    if(te ==0):

                        if(Frame2.coords(rayon[lastindex])[3] > Frame2.coords(ob)[1]):#5

                        #if (Frame2.coords(el)[3] > Frame2.coords(ob)[1]):
                            distance = Frame2.coords(ob)[0] - Frame2.coords(raquette)[0] - 60
                            dis = round(distance, 2)

                            t = "obstacle at " + str(dis)
                            Frame2.itemconfigure(text, text=t)

                            changeDirection(0.1, -0.5, T)
                else:#3
                    if (Frame2.coords(rayon[lastindex])[3] < Frame2.coords(ob)[1]) and (
                            Frame2.coords(rayon[lastindex])[3] < Frame2.coords(ob)[3]):
                        te = 1
                    else:
                        te = 0
                    if (te == 0):


                        if (Frame2.coords(rayon[firstindex])[3] < Frame2.coords(ob)[3]):

                        #if (Frame2.coords(el)[3] < Frame2.coords(ob)[3]):
                            distance = Frame2.coords(ob)[0] - Frame2.coords(raquette)[0] - 60
                            dis = round(distance, 2)

                            t = "obstacle at " + str(dis)
                            Frame2.itemconfigure(text, text=t)

                            changeDirection(0.1, 0.5, T)





















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
    #Frame2.move(arc, 10, 0)
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
   # Frame2.move(arc, -10, 0)
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
   # Frame2.move(arc, 0, -10)
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
    #Frame2.move(arc, 0, 10)
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

#creation de la route
Frame2 = Canvas(fenetre, borderwidth=0, relief=GROOVE, width=langstr, height=hohestr, bg ='grey')
Frame2.pack(padx =0, pady =0)
c, r=0.25, 0




#creation des separations de la route
while c<40:
    Frame2.create_rectangle((2*c*39, 69), ((2*c+1)*39, 71), fill='white', width=0) #on crée le premier carré, puis le deuxième, et ainsi de suite...
    Frame2.create_rectangle((2 * c * 39, 139), ((2 * c + 1) * 39, 141), fill='white', width=0)  #on passe à al ligne suivante
    c=c+1


# Alerte
#creation de l'obstacle no 1


rects = Frame2.create_rectangle(280, 168, 310, 200, outline="red", fill="blue", width=2)
rects2 = Frame2.create_rectangle(530, 118, 560, 180, outline="red", fill="blue", width=2)
rects3 = Frame2.create_rectangle(740, 5, 800, 90, outline="red", fill="blue", width=2)
rects4 = Frame2.create_rectangle(1000, 100, 1080, 130, outline="red", fill="blue", width=2)

tabOb =[]
tabOb.append(rects)
tabOb.append(rects2)
tabOb.append(rects3)
tabOb.append(rects4)

# Les lignes

#coords = [(0,600), (100,348), (88,348), (0,251)]
li1=Frame2.create_line(0,2,1400,2,fill='red')
li2=Frame2.create_line(0,210,1400,210,fill='red')

resetdistance=2000
lastobject=0


#coord = 200,275,500, 155
#courbe = Frame2.create_line(coord, fill='grey')
#courbe = Frame2.create_arc(coord, start=0, extent=150, outline="grey")



"""def generateroad(width):
    coord=[0,210,50,210,100,210,150,210,200,210,250,185,300,165,390,155,480,165,530,185,580,210,635,210,690,210,745,210,800,210]

    coord1=[]

    red=50

    l = len(coord)


    for x in range(0, l):

        if (x%2 ==0):
            coord1.append(coord[x])



        else:
            coord1.append(coord[x]-width)


    li1 = Frame2.create_line(coord, fill='white', width='2')
    li2 = Frame2.create_line(coord1, fill='white', width='2')

    c=6

    while c <= l-7:
        Frame2.create_line(coord[c],coord[c+1],coord[c+2],coord[c+3], fill='orange', width='2')
        Frame2.create_line(coord1[c],coord1[c+1],coord1[c+2],coord1[c+3], fill='orange', width='2')

        c = c + 4

    return [li1,li2];

re=generateroad(140)
li1 =re[0]
li2 = re[1]
"""








#create road
#li2=Frame2.create_line(0,210,200,210,250,180,300,160,330,155,390,150,450,155,480,160,530,180,580,210,800,210,fill='orange',width='2')
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
#baustelle = Frame2.create_arc(500, b2,b3,b4, start=d1, extent=f1, fill='red')


#fin de #creation du deuxième obstacle



#On cree un object Car:




#raquette = Frame2.create_rectangle(0,160,45,190,fill='yellow')



#arc = Frame2.create_arc(end_x+25, end_y, end_x2-25, end_y2, start=-90, dash=(3, 5), extent=180, outline='white')



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

def stopCar():
    global T
    if(T>0):
        T=4000


def startCar():
    global T
    if (T >100):
        T=100


Button(Frame0,text="Slow",fg='navy',command=lambda: stopCar()).pack(side=LEFT, padx=10,pady=10)
Button(Frame0,text="normal",fg='navy',command=lambda: startCar()).pack(side=LEFT, padx=10,pady=10)





dx=1.7 #déplacement initial:je suppose que c'est en mètre
dy=0
mytest = 0
T=100 #la position de la voiture est actualisée après chaque 100ms au départ

V = 1.7*1000/T #vitesse initiale en m/s
ve = str(V)

vitesse=Frame2.create_text(85, 55, text=ve, anchor=SW, font="italic")
unite=Frame2.create_text(120, 55, text=" m/s", anchor=SW, font="italic")




photo = PhotoImage(file="red_car.png")


raquette = Frame2.create_image(0,165, anchor=NW, image=photo)

for user in tree.xpath("/parameter/radar/angle"):
    angle= user.text

new_angle = float(angle)/2

angle_in_radians = new_angle * math.pi / 180
angle_in_radians = -1*angle_in_radians
angle_in_radians2 = new_angle * math.pi / 180
line_length = 105
center_x = 60
center_y = 180
end_x = center_x + line_length * math.cos(angle_in_radians)
end_y = center_y + line_length * math.sin(angle_in_radians)
end_x2 = center_x + line_length * math.cos(angle_in_radians2)
end_y2 = center_y + line_length * math.sin(angle_in_radians2)


sensor1 = Frame2.create_line(60, 180, end_x ,end_y, fill='white')
sensor2 = Frame2.create_line(60, 180, 160,180, fill='white')
sensor3 = Frame2.create_line(60, 180, end_x2,end_y2,fill='white')
text=Frame2.create_text(85, 180, text="20 m", anchor=SW, font="italic")

rayon=[];
rayon.append(sensor1)
rayon.append(sensor2)
rayon.append(sensor3)

firstindex=0
lastindex=2




deplacement()




fenetre.mainloop()
