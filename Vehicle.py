import sys, io


class Vehicle(object):

    def __init__(self, v_ref, v, s_ref, dt, a, b, x, l, delta, length, colorOfCar):

        def getv_ref():
            return v_ref

        def setv_ref(v_ref):
            self.v_ref = v_ref

        def gets_ref():
            return s_ref

        def sets_ref(s_ref):
            self.s_ref = s_ref

        def getdt():
            return dt
        def setdt(t):
            self.dt = t

        def geta():
            return a
        def seta(a):
            self.a = a

        def getb():
            return b
        def setb(b):
            self.b = b

        def getx():
            return x
        def setx(x):
            self.x = x

        def getl():
            return l

        def setl(l):
            self.l = l

        def getv():
            return v
        def setv(v):
            self.v = v

        def getdelta():
            return delta

        def setdelta(delta):
            self.delta = delta

        def getlength():
            return length

        def setlength(length):
            self.length = length

        def getcolorOfCar():
            return colorOfCar

        def setcolorOfCar(colorOfCar):
            self.colorOfCar = colorOfCar

    def vehicle(self, i, v_ref, v, s_ref, dt, a, b, x, l, delta, length ):

        self.setv_ref(v_ref)
        self.setv(v)
        self.sets_ref(s_ref)
        self.seta(a)
        self.setb(b)
        self.setx(x)
        self.setl(l)
        self.setdt(dt)
        self.setdelta(delta)
        self.setlength(length)