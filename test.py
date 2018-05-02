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






tree = etree.parse("setup.xml")
root = tree.getroot()


# Création de la fenêtre principale

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




def deplacement():
    global dx, dy,mytest,ve,T
    # On deplace la balle :

    moveCarAndRadar(dx, dy)

    detectObstacle()
    # On repete cette fonction
    fenetre.after(int(T), deplacement)

#fonction qui permet de deplacer l'ensemble (car + radar)

def moveCarAndRadar(x,y):
    Frame2.itemconfigure(vitesse, text=str(ve))
    Frame2.move(raquette, x, y)
    for el in rayon:
        Frame2.move(el, x, y)
        #Frame2.move(sensor2, x, y)
        #Frame2.move(sensor3, x, y)
   # Frame2.move(arc, x, y)
    Frame2.move(text, x, y)

def changeDirection(fx,fy,T):
    old =T
    T=old *3

    if(T>0):
        c = (dx / T) * 1000
        ve = round(c, 2)
        Frame2.itemconfigure(vitesse, text=str(ve))






    Frame2.move(raquette, fx, fy)
    for el in rayon:
        Frame2.move(el, fx, fy)
    #Frame2.move(arc, fx, fy)
    Frame2.move(text, fx, fy)




def detectObstacle():

    if(mytest ==0):
        Frame2.itemconfigure(text, text="radar on")
        for el in rayon:
            if (Frame2.coords(el)[3] > Frame2.coords(courbe)[1]) and (
                    Frame2.coords(el)[0] < Frame2.coords(courbe)[2]) and (
                    Frame2.coords(el)[2] > Frame2.coords(courbe)[0]):
                distance = Frame2.coords(courbe)[0] - Frame2.coords(el)[2] + 100
                dis = round(distance, 2)

                t = "obstacle no 1 à " + str(dis)
                Frame2.itemconfigure(text, text=t)
                changeDirection(0, -1, T)

        for el in rayon:
            if (Frame2.coords(el)[3] > Frame2.coords(baustelle)[1]) and (
                    Frame2.coords(el)[0] < Frame2.coords(baustelle)[2]) and (
                    Frame2.coords(el)[2] > Frame2.coords(baustelle)[0]):
                distance = Frame2.coords(baustelle)[0] - Frame2.coords(el)[2] + 100
                dis = round(distance, 2)

                t = "obstacle no 2 à " + str(dis)
                Frame2.itemconfigure(text, text=t)
                changeDirection(0, -1, T)




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
#creation de l'obstacle


rects = Frame2.create_rectangle(340, 168, 345, 200, outline="red", fill="blue", width=2)
#cercle = Frame2.create_oval(334,163,347,152, fill='orange', outline="White")

# Les lignes

coords = [(0,600), (100,348), (88,348), (0,251)]
#li1=Frame2.create_line(225,211,355,135,600,135,670,211,fill='orange')
#li2=Frame2.create_line(210,140,355,75,640,75,700,140,fill='orange')


coord = 200,275,500, 130
courbe = Frame2.create_arc(coord, start=0, extent=150, outline="gray")

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
baustelle = Frame2.create_arc(500, b2,b3,b4, start=d1, extent=f1, fill='red')


#fin de #creation du deuxième obstacle



#On cree un object Car:


photo = PhotoImage(file="red_car.png")


raquette = Frame2.create_image(0,150, anchor=NW, image=photo)

#raquette = Frame2.create_rectangle(0,160,45,190,fill='yellow')
for user in tree.xpath("/parameter/radar/angle"):
    angle= user.text

new_angle = float(angle)/2

angle_in_radians = new_angle * math.pi / 180
angle_in_radians = -1*angle_in_radians
angle_in_radians2 = new_angle * math.pi / 180
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

rayon=[];
rayon.append(sensor1)
rayon.append(sensor2)
rayon.append(sensor3)













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


def draw_figure(canvas, figure, loc=(0, 0)):
    """ Draw a matplotlib figure onto a Tk canvas

    loc: location of top-left corner of figure on canvas in pixels.
    Inspired by matplotlib source: lib/matplotlib/backends/backend_tkagg.py
    """
    figure_canvas_agg = FigureCanvasAgg(figure)
    figure_canvas_agg.draw()
    figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)

    photo = tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)


    # Position: convert from top-left anchor to center anchor
    canvas.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image=photo)

    # Unfortunately, there's no accessor for the pointer to the native renderer
    tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)

    # Return a handle which contains a reference to the photo object
    # which must be kept live or else the picture disappears
    return photo



# Generate some example data
X = np.linspace(0, 1* np.pi, 20)
Y = np.sin(X)


# Create the figure we desire to add to an existing canvas
fig = mpl.figure.Figure(figsize=(7, 1.8))
ax = fig.add_axes([0, 0, 1, 1],facecolor='gray')

for item in [fig, ax]:
    item.patch.set_visible(False)

#fig.patch.set_visible(False)
ax.axis('off')


ax.plot(X, Y,color='yellow')

# Keep this handle alive, or else figure will disappear
fig_x, fig_y = 55, 125
fig_photo = draw_figure(Frame2, fig, loc=(fig_x, fig_y))
fig_w, fig_h = fig_photo.width(), fig_photo.height()






deplacement()




fenetre.mainloop()
