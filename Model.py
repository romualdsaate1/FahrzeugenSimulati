
class Model:

    def update(positionvelocity, h, vehicleArray):

        numbervehicles = Controller.n_veh

        positionvelocitynew = [positionvelocity.length][2]

        i = 0
        while (i < numbervehicles - 1):
            temp = Model.f(positionvelocity[i][0], positionvelocity[i][1], positionvelocity[i + 1][0],
                           positionvelocity[i + 1][1], vehicleArray[i])
            k1 = h * temp[0]
            w1 = h * temp[1]

            temp = Model.f(positionvelocity[i][0], positionvelocity[i][1] + w1 / 2, positionvelocity[i + 1][0],
                           positionvelocity[i + 1][1], vehicleArray[i])
            k2 = h * (temp[0] + w1 / 2)
            w2 = h * temp[1]

            temp = Model.f(positionvelocity[i][0], positionvelocity[i][1] + w2 / 2, positionvelocity[i + 1][0],
                           positionvelocity[i + 1][1], vehicleArray[i])
            k3 = h * (temp[0] + w2 / 2)
            w3 = h * temp[1]

            temp = Model.f(positionvelocity[i][0], positionvelocity[i][1] + w3, positionvelocity[i + 1][0],
                           positionvelocity[i + 1][1], vehicleArray[i])
            k4 = h * (temp[0] + w3)
            w4 = h * temp[1]

            positionvelocitynew[i][0] = positionvelocity[i][0] + k1 / 6 + k2 / 3 + k3 / 3 + k4 / 6
            positionvelocitynew[i][1] = positionvelocity[i][1] + w1 / 6 + w2 / 3 + w3 / 3 + w4 / 6

            # Teste ob Auto recht herausfährt:
            if positionvelocitynew[i][0] > (Controller.winwidth + vehicleArray[i].getlength()):
                positionvelocitynew[i][0] = positionvelocitynew[i][0] - Controller.winwidth


            # Teste ob Auto rückwärts fährt
            if positionvelocitynew[i][1] < 0:
                positionvelocitynew[i][1] = 0
            i += 1

        temp = Model.f(positionvelocity[numbervehicles - 1][0], positionvelocity[numbervehicles - 1][1],
                       positionvelocity[0][0], positionvelocity[0][1], vehicleArray[numbervehicles - 1])
        k1 = h * temp[0]
        k2 = h * temp[1]

        temp = Model.f(positionvelocity[numbervehicles - 1][0], positionvelocity[numbervehicles - 1][1] + w1 / 2,
                       positionvelocity[0][0], positionvelocity[0][1], vehicleArray[numbervehicles - 1])
        k2 = h * (temp[0] + w1 / 2)
        w2 = h * temp[1]

        temp = Model.f(positionvelocity[numbervehicles - 1][0], positionvelocity[numbervehicles - 1][1] + w2 / 2,
                       positionvelocity[0][0], positionvelocity[0][1], vehicleArray[numbervehicles - 1])
        k3 = h * (temp[0] + w2 / 2)
        w3 = h * temp[1]

        temp = Model.f(positionvelocity[numbervehicles - 1][0], positionvelocity[numbervehicles - 1][1] + w3,
                       positionvelocity[0][0], positionvelocity[0][1], vehicleArray[numbervehicles - 1])
        k4 = h * (temp[0] + w3)
        w4 = h * temp[1]

        positionvelocitynew[numbervehicles - 1][0] = positionvelocity[numbervehicles - 1][0] + k1 / 6 + k2 / 3 + k3 / 3 + k4 / 6
        positionvelocitynew[numbervehicles - 1][1] = positionvelocity[numbervehicles - 1][1] + w1 / 6 + w2 / 3 + w3 / 3 + w4 / 6

        # test ob Auto rescht herausfährt

        if positionvelocitynew[numbervehicles -1][0] > (Controller.winwidth + vehicleArray[numbervehicles - 1].getlength()):
            positionvelocitynew[numbervehicles - 1][0] = positionvelocitynew[numbervehicles - 1][0] - Controller.winwidth

        # Test ob Auto rückwärts fährt

        if positionvelocitynew[numbervehicles - 1][1] < 0 :
            positionvelocitynew[numbervehicles - 1][1] = 0

        return positionvelocitynew

    class f(object):
        def __init__(self, x1, x2, v2, auto):

            a = auto.geta()
            b = auto.getb()
            T = auto.getdt()
            s_ref = auto.gets_ref()
            v_ref = auto.getv_ref()
            length = auto.getlength()
            delta = auto.getdelta()

            deltav = v1 - v2
            salpha = x2 - length - x1

            #Falls diese auto am rechten rand ist

            if salpha < 0:
                salpha = x2 - length + Controller.winwidth - x1

            sfunk = (s_ref + v1 * T + v1 * deltav) / (2 * Math.sqrt(a * b))
            result = {v1, a * (1 - Math.pow(v1 / v_ref, delta) - Math.pow(sfunk / salpha, 2))}

            return result


