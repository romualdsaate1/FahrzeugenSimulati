import sys
#import java.applet
#from jinfo import *
from java.awt import windows
from java.awt import Color

class Controller(object):

    serialVersionUID = 1
    tau = 0.1
    L = 3
    dt = 3
    n_veh = 35
    n_pkw = 30
    n_lkw = 0
    h = 0.001
    a_pkw = 0.3
    b_pkw = 2
    s_ref_pkw = 6
    v_ref_pkw = 120 / 3.6
    a_lkw = 0.3
    b_lkw = 3.5
    v_ref_lkw = 100 / 3.6
    delta = 4
    length_lkw = 6
    length_pkw = 3
    framerate = 900
    repaintRate = 1

    x0_pkw = 15
    v0_pkw = 120 / 3.6
    x0_lkw = 15
    v0_lkw = 100 / 3.6
    rand = 10

    window = None

    bStart = JButton('Start')
    bPause = JButton('Pause')
    bReset = JButton('Reset')

    sDesiredDistances0 = JSlider(JSlider.VERTICAL, 0, 200, (s_ref_pkw * 10))
    sDesiredSpeed0 = JSlider(JSlider.VERTICAL, 0, 1600, (v_ref_pkw * 36))
    sMaximalAcellerrationA = JSlider(JSlider.VERTICAL, 0, 50, (a_pkw * 10))
    sComfortAcsllerationB = JSlider(JSlider.VERTICAL, 0, 5, (b_pkw * 10))
    sTimeDistance = JSlider(JSlider.VERTICAL, 0, 50, (dt * 10))
    sDelta = JSlider(JSlider.VERTICAL, 0, 5, delta)
    sNumberOfCarsn = JSlider(JSlider.VERTICAL, 0, 50, n_pkw)
    sNumberOfTrucksp1 = JSlider(JSlider.VERTICAL, 0, 25, n_lkw)
    sNumberOfTrucksp = JSlider(JSlider.VERTICAL, 0, 25, n_lkw)

    class DrawSurface(width, height, vehicleArray):

        def __init__(self):

            self.setSize(width, height)
            bStart.addActionListener(self)
            bPause.addActionListener(self)
            bReset.addActionListener(self)

            sDesiredDistances0.addChangeListener(self)
            sDesiredSpeedv0.addChangeListener(self)
            sMaximalAcellerationA.addChangeListener(self)
            sComfortAcellerationB.addChangeListener(self)
            sTimeDistance.addChangeListener(self)
            sDelta.addChangeListener(self)
            sNumberOfCarsn.addChangeListener(self)
            sNumberOfTrucksp1.addChangeListener(self)

            sDesiredDistances0.setMaximumSize(Dimension(width * 0.6), Short.MAX_VALUE)
            sDesiredSpeedv0.setMaximumSize(Dimension(width * 0.6), Short.MAX_VALUE)
            sMaximalAcellerationA.setMaximumSize(Dimension(width * 0.6), Short.MAX_VALUE)
            sComfortAcellerationB.setMaximumSize(Dimension(width * 0.6), Short.MAX_VALUE)
            sTimeDistance.setMaximumSize(Dimension(width * 0.6), Short.MAX_VALUE)
            sDelta.setMaximumSize(Dimension((int)(width * 0.6), Short.MAX_VALUE))
            sNumberOfCarsn.setMaximumSize(Dimension((int)(width * 0.6), Short.MAX_VALUE))
            sNumberOfTrucksp1.setMaximumSize(Dimension((int)(width * 0.6), Short.MAX_VALUE))

            sDesiredDistances0.setPaintLabels(true)
            sDesiredSpeedv0.setPaintLabels(true)
            sMaximalAcellerationA.setPaintLabels(true)
            sComfortAcellerationB.setPaintLabels(true)
            sTimeDistance.setPaintLabels(true)
            sDelta.setPaintLabels(true)
            sNumberOfCarsn.setPaintLabels(true)
            sNumberOfTrucksp1.setPaintLabels(true)

            DeltaTable = Hashtable()
            DeltaTable.put(0, JLabel("0.0"))
            DeltaTable.put(4, JLabel("1.0"))
            DeltaTable.put(8, JLabel("2.0"))
            DeltaTable.put(12, JLabel("3.0"))
            DeltaTable.put(16, JLabel("4.0"))
            DeltaTable.put(20, JLabel("5.0"))

            sMaximalAcellerationA.setLabelTable(DeltaTable)
            sComfortAcellerationB.setLabelTable(DeltaTable)


            DistanceTable = Hashtable()
            DistanceTable.put(0, JLabel("0"))
            DistanceTable.put(50, JLabel("5"))
            DistanceTable.put(100, JLabel("10"))
            DistanceTable.put(150, JLabel("15"))
            DistanceTable.put(200, JLabel("20"))

            sDesiredDistance0.setLabelTable(DistanceTable)


            SpeedTable = Hashtable()
            SpeedTable.put(0, JLabel("0"))
            SpeedTable.put(200, JLabel("20"))
            SpeedTable.put(400, JLabel("40"))
            SpeedTable.put(600, JLabel("60"))
            SpeedTable.put(800, JLabel("80"))
            SpeedTable.put(1000, JLabel("100"))
            SpeedTable.put(1200, JLabel("120"))
            SpeedTable.put(1400, JLabel("140"))
            SpeedTable.put(1600, JLabel("160"))

            sDesiredSpeedv0.setLabelTable(SpeedTable)

            AccTable = Hashtable()
            AccTable.put(0, JLabel("0"))
            AccTable.put(10, JLabel("10"))
            AccTable.put(20, JLabel("20"))
            AccTable.put(30, JLabel("30"))
            AccTable.put(40, JLabel("40"))
            AccTable.put(50, JLabel("50"))
            AccTable.put(60, JLabel("60"))

            sTimeDistance.setLabelTable(AccTable)
            sComfortAcellerationB.setLabelTable(AccTable)
            sMaximalAcellerationA.setLabelTable(AccTable)

            CarTable = Hashtable()
            CarTable.put(0, JLabel("0"))
            CarTable.put(10, JLabel("10"))
            CarTable.put(20, JLabel("20"))
            CarTable.put(30, JLabel("30"))
            CarTable.put(40, JLabel("40"))
            CarTable.put(50, JLabel("50"))
            CarTable.put(60, JLabel("60"))

            sNumeberOfCarsn.setLabelTable(CarTable)

            sDesiredDistances0.setMajorTickSpacing(50)
            sDesiredSpeedv0.setMajorTickSpacing(200)
            sMaximalAcellerationA.setMajorTickSpacing(10)
            sComfortAcellerationB.setMajorTickSpacing(10)
            sTimeDistance.setMajorTickSpacing(10)
            sDelta.setMajorTickSpacing(1)
            sNumberOfCarsn.setMajorTickSpacing(5)
            sNumberOfTrucksp1.setMajorTickSpacing(5)

            minorTickSpacing = 1
            sDesiredDistances0.setMinorTickSpacing(10)
            sDesiredSpeedv0.setMinorTickSpacing(50)
            sMaximalAcellerationA.setMinorTickSpacing(minorTickSpacing)
            sComfortAcellerationB.setMinorTickSpacing(minorTickSpacing)
            sTimeDistance.setMinorTickSpacing(minorTickSpacing)
            #sDelta.setMinorTickSpacing(1)
            sNumberOfCarsn.setMinorTickSpacing(minorTickSpacing)
            sNumberOfTrucksp1.setMinorTickSpacing(minorTickSpacing)

            sDesiredDistances0.setPaintTicks(true)
            sDesiredSpeedv0.setPaintTicks(true)
            sMaximalAcellerationA.setPaintTicks(true)
            sComfortAcellerationB.setPaintTicks(true)
            sTimeDistance.setPaintTicks(true)
            sDelta.setPaintTicks(true)
            sNumberOfCarsn.setPaintTicks(true)
            sNumberOfTrucksp1.setPaintTicks(true)

            sDesiredDistances0.setPaintLabels(true)
            sDesiredSpeedv0.setPaintLabels(true)
            sMaximalAcellerationA.setPaintLabels(true)
            sComfortAcellerationB.setPaintLabels(true)
            sTimeDistance.setPaintLabels(true)
            sDelta.setPaintLabels(true)
            sNumberOfCarsn.setPaintLabels(true)
            sNumberOfTrucksp1.setPaintLabels(true)

            buttonpane = JPanel ()
            buttonpane.setLayout(BoxLayout(buttonpane, BoxLayout.X_AXIS))

            buttonpane.add(Box.createHorizontalGlue())
            buttonpane.add(bStart)
            buttonpane.add(bPause)
            buttonpane.add(bReset)
            buttonpane.add(Box.createHorizontalGlue())

            dist = 5
            minSize = Dimension(dist, dist)
            prefSize = Dimension(dist, dist)
            maxSize = Dimension(Short.MAX_VALUE, dist)

            sliderPanel = JPanel() #for the content
            sliderPanel.setLayout(BoxLayout(sliderPanel, BoxLayout.X_AXIS))
            sliderPanel.add(sDesiredDistances0, BorderLayout.SOUTH)
            sliderPanel.add(sDesiredSpeedv0, BorderLayout.SOUTH)
            sliderPanel.add(sMaximalAcellerationA, BorderLayout.SOUTH)
            sliderPanel.add(sComfortAcellerationB, BorderLayout.SOUTH)
            sliderPanel.add(sTimeDistance, BorderLayout.SOUTH)
            sliderPanel.add(sDelta, BorderLayout.SOUTH)
            sliderPanel.add(sNumberOfCarsn, BorderLayout.SOUTH)
            sliderPanel.add(sNumberOfTrucksp1, BorderLayout.SOUTH)

            self.add(sliderPanel)

            mySimulation = simulationPanel(width, height, L, vehicleArray)

            labelPanel = JPanel()
            labelPanel.setLayout(GridLayout(1, 8))
            labelPanel.add(JLabel("<html><div style=\"text-align: center;\">" + "Minimal Distance" + "</html>"))
            labelPanel.add(JLabel("<html><div style=\"text-align: center;\">" + "Desired Speed" + "</html>"))
            labelPanel.add(JLabel("<html><div style=\"text-align: center;\">" + "Max Accelleration" + "</html>"))
            labelPanel.add(JLabel("<html><div style=\"text-align: center;\">"+ "Comfort Deccelleration" + "</html>"))
            labelPanel.add(Box.Filler(minSize, prefSize, maxSize))
            labelPanel.add(JLabel("<html><div style=\"text-align: center;\">" + "Time Distance" + "</html>"))
            labelPanel.add(JLabel("<html><div style=\"text-align: center;\">" + "Delta" + "</html>"))
            labelPanel.add(JLabel("<html><div style=\"text-align: center;\">" + "Number of Cars" + "</html>"))
            labelPanel.add(JLabel("<html><div style=\"text-align: center;\">" + "Number of Trucks" + "</html>"))
            labelPanel.setBorder(BorderFactory.createLineBorder(Color.black))

            temp = JPanel()
            temp.setLayout(BoxLayout(temp, BoxLayout.Y_AXIS))
            temp.add(labelPanel)
            temp.add(sliderPanel)

            contentPane = self.getContentPane()
            contentPane.add(buttonPane, BorderLayout.PAGE_START)
            contentPane.add(temp, BorderLayout.SOUTH)
            contentPane.add(mySimulation, BorderLayout.CENTER)
            contentPane.validate()
            # End Surface Draw

        class actionPerformed:

            def ActionEvent(self, e):
                if e.getSource() == bStart:
                    print("Start Pressed")
                    pause = false
                if e.getSource() == bPause :
                    print("Pause Pressed")
                    pause = true
                if e.getSource() == bReset :
                    pause = true
                    print("Reset Pressed")

                i = 0
                while i < L :
                    vehicleArray [i].clear()
                    i+=1
                    vehicleArry = InitialiseVehicles()
                    self.repaint()

        class stateChanged :

            def ChangeEvent(self, e):

                if e.getSource() == sDesiredDistance0 :

                        if sDesiredDistances0.getValue() == 0:
                            sDesireddistances0.setValue(1)
                        s_ref_pkw = sDesiredDistances0.getValue() / 10
                        print("Desired Distance" + s_ref_pkw)
                        updatevehicles()

                if e.getSource() == sDesiredSpeedv0:
                    if sDesiredSpeedv0.getValue() ==0:
                        sDesiredSpeedv0.setvalue(1)
                    v_ref_pkw = sDesiredSpeedv0.getValue() / 10 / 3.6
                    print("Desired Speed" + self.v_ref_pkw)
                    v0_pkw = sDesiredSpeedv0.getValue() / 10 / 3.6
                    updatevehicles()

                if e.getSource() == sMximalAcellerationA:
                    if sMximalAcellerationA.getValue() == 0:
                        sMximalAcellerationA.setvalue(1)
                    a_pkw = sMximalAcellerationA.getValue() / 10
                    print("Maximal Acceleration" + a_pkw)
                    updatevehicles()

                if e.getSource() == sComfortAcellerationB:
                    if sComfortAcellerationB.getValue() == 0:
                        sComfortAcellerationB.setvalue(1)
                    a_pkw = sComfortAcellerationB.getValue() / 10
                    print("Comfort Acceleration" + b_pkw)
                    updatevehicles()

                if e.getSource() == sTimeDistance:
                    if sTimeDistance.getValue() == 0:
                        sTimeDistance.setvalue(1)
                    a_pkw = sTimeDistance.getValue() / 10
                    print("Time Distance" + dt)
                    updatevehicles()

                if e.getSource() == sDelta:
                    if sDelta.getValue() == 0:
                        sDelta.setvalue(1)
                    a_pkw = sDelta.getValue()
                    print("Delta" + delta)
                    updatevehicles()

                if e.getSource() == sNumberOfCarsn:
                    if sNumberOfCarsn.getValue() == 0:
                        sNumberOfCarsn.setvalue(1)

                    pause = true
                    if sNumberOfCarsn.getValue() + n_lkw <= 50:
                        n_pkw = sNumberOfCarsn.getValue()
                        print("Number of cars" + n_pkw)

                        n_veh = n_pkw + n_lkw
                        i=0
                        while i < L:
                            vehicleArray[i].clear()
                            i+=1
                        vehicleArray = InitialiseVehicles()
                    else:
                        sNumberOfCarsn.setvalue(50 - n_lkw)
                self.repaint()
                #self.__repr__()

                if e.getSource() == sNumberOfTrucksp1:
                    if NumberOfTrucksp1.getValue() == 0:
                        NumberOfTrucksp1.setvalue(1)

                    pause = true
                    if NumberOfTrucksp1.getValue() + n_pkw <= 50:
                        n_lkw = NumberOfTrucksp1.getValue()
                        print("Number of Trucks" + n_lkw)

                        n_veh = n_pkw + n_lkw
                        i=0
                        while i < L:
                            vehicleArray[i].clear()
                            i+=1
                        vehicleArray = InitialiseVehicles()
                    else:
                        sNumberOfCarsn.setvalue(50 - n_pkw)
                self.repaint()
                #self.__repr__()


    class simulationPanel:
        def __init__(self, width, height, numberOfLanes, vehicleArray):
            self.width = width
            self.height = height
            self.numberOfLanes = numberOfLanes
            self.vehicleArray = vehicleArray

        def paint(self, g):
            widthOfLane = 40
            g.setColor(Color.green)
            g.drawRect(0, 0, self.width, 20)
            g.fillRect(0, 0, self.width, 20)

            g.setColor(Color.gray)
            g.drawRect(0, 0, self.width, widthOfLane*self.numberOfLanes)
            g.fillRect(0, 20, self.width, widthOfLane*self.numberOfLanes)

            g.setColor(Color.white)
            g.fillRect(0, 22, self.width, 2)
            g.fillRect(0, 26, self.width, 2)

            j=0
            while j < self.numberOfLanes:
                i=0
                while i < (self.width /50):
                    g.fillRect(50*i + j*widthOfLane, 20, 2)
                    i+=1
                j+=1
            g.fillRect(0, 20 + numberOfLanes * widthOfLane - 6, width, 2)
            g.fillRect(0, 20 + numberOfLanes * widthOfLane - 2, width, 2)

            g.setColor(Color.green)
            g.drawRect(0, 20 + numberOfLanes * widthOfLane, width, 20)
            g.fillRect(0, 20 + numberOfLanes * widthOfLane, width, 20)

            j=0
            while j < numberOfLanes:
                posx = 40 * (j + 1)
                i = 0
                while i < n_veh:
                    temp = vehicleArray[j].get(i)
                    posx = Math.round(temp.getx())
                    g.setColor(temp.getColorOfCar())
                    g.fillRect(posx - temp.getlength(), posy - 10, temp.getlength(), 20)
                    i+=1
                j+=1

        class InitialiseVehicles():

            createdLKW = 0
            p = n_lkw / n_veh

            j = 0
            while j < L:
                lastvehicle = 0
                createdLKW = 0
                i = 0
                while i < n_veh:
                    if (Math.random() <= p) & (createdLKW < n_lkw):
                        lastvehicle = lastvehicle + x0_lkw + rand * (0.5 - Math.random)
                        vehicleArray[j].add(LKW(i, v_ref_lkw, v0_lkw, s_ref_lkw, dt, a_lkw, b_lkw, lastvehicle, L, delta, length_lkw))
                        createdLKW+=1
                    elif (n_pkw + createdLKW) <= n_veh:
                        lastvehicle = lastvehicle + x0_pkw + rand * (0.5 - Math.random)
                        vehicleArray[j].add(Car(i, v_ref_pkw, v0_pkw, s_ref_pkw, dt, a_pkw, b_pkw, lastvehicle, L, delta, length_pkw))
                    else:
                        lastvehicle = lastvehicle + x0_lkw + rand * (0.5 - Math.random())
                        vehicleArray[j].add(LKW(i, v_ref_lkw, v0_lkw, s_ref_lkw, dt, a_lkw, b_lkw, lastvehicle, L, delta, length_lkw))
                        createdLKW+=1
                    i+=1
                j+=1

            print("Arraylänge:/t" + vehicleArray[0].size())

    class updatevehicles():
        temp = Null
        j = 0
        while j < L:
            i = 0
            while i < n_veh:
                temp = vehicleArray[j].get(i)
                if temp.getColorOfCar() == Color.blue:
                    temp.seta(a_pkw)
                    temp.setb(b_pkw)
                    temp.setdelta(delta)
                    temp.setdt(dt)
                    temp.sets_ref(s_ref_pkw)
                    temp.setv_ref_pkw
                i+=1
            j+=1


    class init() :
        positionvelocity = [60][2]
        singleLaneVehicles = [60]
        winwidth = 800
        winheigth = 500

        vehicleArray = InitialiseVehicles()

        DrawSurface(winwidth, winheigth, vehicleArray)
        self.setSize(winwidth, winheigth)
        self.validate()
        self.setVisible(True)

        pause = True

        while not Thread.interrupted():
            while self.pause:
                try:
                    self.wait()
                except Exception :
                    break


            temp = None
            j=0
            while j < self.L:
                i=0
                while i < n_veh:
                    temp = vehicleArray[j].get(i)
                    positionvelocity[i][0] = temp.getx()
                    positionvelocity[i][1] = temp.getv()
                    i+=1
                k=0
                while k < n_veh:
                    singleLaneVehicles[k] = vehicleArray[j],get(k)
                    k+=1

                positionvelocity = Model.update(positionvelocity, h, singleLaneVehicles)

                while i < n_veh:
                    temp = vehicleArray[j].get(i)
                    temp.setx(positionvelocity[i][0])
                    temp.setv(positionvelocity[i][1])
                    i+=1

                self.repaint()

if __name__ == '__main__':
    Controller()