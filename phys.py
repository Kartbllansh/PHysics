import numpy as nppy
import math as math
import matplotlib.pyplot as pltgrah

Lx = 2
Ly = 2
x0 = 1
y0 = 1
R = 0.2
r = 0.05
m = 0.3
u1 = 0.01
u2 = 0.05
u3 = 0.1
g = 9.8
t = 0.001
List = []
Ok = []
for i in range(360):
    Ok.append(i)
for j in range(5):
    List1 = []
    for i in range(360):
        List1.append(0)
    List.append(List1)
for k in range(5):
    if k == 0:
        u1 = u1
    if k == 1:
        u1 = u2
    if k == 2:
        u1 = u3
    for i in range(360):
        x1 = 1.9
        y1 = 0.1
        x2 = 1.9
        y2 = 1.8
        V0 = 2
        V2 = 0
        Ok11 = round(math.radians(i), 5)
        Ok22 = 0
        l = 0
        q = 0
        w = 0
        p = 0
        b = 0
        Vy0 = round(V0 * math.sin(Ok11), 3)
        Vx0 = round(V0 * math.cos(Ok11), 3)
        Vx2 = 0
        Vy2 = 0
        while ((V0 > 0) or (V2 > 0)):
            if (V0 > 0):
                if (Vx0 != 0):
                    x1 = x1 + Vx0 * t
                if (Vy0 != 0):
                    y1 = y1 + Vy0 * t
                V0 = V0 - (u1 * g * t)
                if Ok11 == 0 or Ok11 == round(math.radians(180), 4) or Ok11 == round(math.radians(270),
                                                                                     4) or Ok11 == round(
                        math.radians(90), 4):
                    if Ok11 == 0 or Ok11 == round(math.radians(180), 4):
                        Vy0 = 0
                        if Ok11 == 0:
                            Vx0 = V0
                        else:
                            Vx0 = -V0
                    else:
                        Vx0 = 0
                        if Ok11 == round(math.radians(90), 5):
                            Vy0 = V0
                        else:
                            Vy0 = -V0
                else:
                    Vx0 = round(V0 * math.cos(Ok11), 3)
                    Vy0 = round(V0 * math.sin(Ok11), 3)
                if V0 < 0:
                    V0 = 0
                    Vx0 = 0
                    Vy0 = 0
            if V2 > 0:
                if Vx2 != 0:
                    x2 = x2 + Vx2 * t
                if Vy2 != 0:
                    y2 = y2 + Vy2 * t
                V2 = V2 - (u1 * g * t)
                Vx2 = round(V2 * math.cos(Ok22), 3)
                Vy2 = round(V2 * math.sin(Ok22), 3)
                if V2 < 0:
                    V2 = 0
                    Vx2 = 0
                    Vy2 = 0
            if math.sqrt(math.pow((x1 - x0), 2) + math.pow((y1 - y0), 2)) <= R:
                V0 = 0
                x1 = x0
                y1 = y0
            if math.sqrt(math.pow((x2 - x0), 2) + math.pow((y2 - y0), 2)) <= R:
                List[k][i] = m * V2 * V2 / 2.0
                V2 = 0
                V0 = 0
                continue
            if ((x1 + r) >= Lx or (x1 - r) <= 0) and w == 0:
                Vx0 = -Vx0
                Ok11 = round(math.radians(180) - Ok11, 5)
                w = 1
            else:
                w = 0
            if ((y1 + r) >= Ly or (y1 - r) <= 0) and p == 0:
                Vy0 = -Vy0
                Ok11 = round(Ok11 - math.radians(180), 5)
                p = 1
            else:
                p = 0
            if ((x2 + r) >= Lx or (x2 - r) <= 0) and q == 0:
                Vx2 = -Vx2
                Ok22 = round(math.radians(180) - Ok22, 5)
                q = 1
            else:
                q = 0
            if ((y2 + r) >= Ly or (y2 - r) <= 0) and b == 0:
                Vy2 = -Vy2
                Ok22 = round(Ok22 - math.radians(180), 5)
                b = 1
            else:
                b = 0
            if math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2)) <= (2 * r) and l == 0:
                en = nppy.array([round((x2 - x1) / (2 * r), 3), round((y2 - y1) / (2 * r), 3)])
                et = nppy.array([round((y1 - y2) / (2 * r), 3), round((x2 - x1) / (2 * r), 3)])
                Vvect = nppy.array([Vx0, Vy0])
                V2vect = nppy.array([Vx2, Vy2])
                Vvect = (round(nppy.dot(V2vect, en), 3) * en) + (round(nppy.dot(Vvect, et), 3) * et)
                V2vect = (round(nppy.dot(nppy.array([Vx0, Vy0]), en), 3) * en) + (round(nppy.dot(V2vect, et), 3) * et)
                Vx0 = round(Vvect[0], 3)
                Vy0 = round(Vvect[1], 3)
                Vx2 = round(V2vect[0], 3)
                Vy2 = round(V2vect[1], 3)
                V0 = round(nppy.linalg.norm(Vvect), 3)
                V2 = round(nppy.linalg.norm(V2vect), 3)
                if V0 != 0:
                    Ok11 = round(math.acos(round((Vx0 / V0), 3)), 5)
                else:
                    Vx0 = 0
                    Vy0 = 0
                    Ok11 = 0
                if V2 != 0:
                    Ok22 = round(math.acos(round((Vx2 / V2), 3)), 5)
                else:
                    Vx2 = 0
                    Vy2 = 0
                    Ok22 = 0
                l = 1
            else:
                l = 0
pltgrah.figure()
pltgrah.plot(Ok, List[0], 'o-b', label="µ1", lw=1)
pltgrah.plot(Ok, List[1], 'o-r', label="µ2", lw=1)
pltgrah.plot(Ok, List[2], 'o-g', label="µ3", lw=1)
pltgrah.xlabel('Угол α (град)')
pltgrah.ylabel('Энергия шара Е (Дж)')
pltgrah.legend()
pltgrah.grid(True)
pltgrah.show()
