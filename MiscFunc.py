from ClassPoint import Point
import math

# Возвращает значение после вершины стека
def nextToTop(S):
    return S[-2]

# Функция, возвращающая квадрат расстояния между p1 и p2
def distSq(p1, p2):
    return ((p1[0] - p2[0]) * (p1[0] - p2[0]) +
            (p1[1] - p2[1]) * (p1[1] - p2[1]))

def left_index(points):
    minn = 0
    for i in range(1, len(points)):
        if points[i][0] < points[minn][0]:
            minn = i
        elif points[i][0] == points[minn][0]:
            if points[i][1] < points[minn][1]:
                minn = i
    return minn

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def angle(p0, p1):
    x, y = p1[0] - p0[0], p1[1] - p0[1]
    return math.atan2(y, x)

# Возвращает площадь треугольника по трем точкам
def squareTriangle(p1, p2, p3):
    return 0.5 * (p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1]))

# Функция, которая находит максимальную площадь треугольника по трем точкам
def maxSquare(arrpoints, min_point, max_point):
    maxSquarePoint = None
    maxSquare = 0
    for i in range(len(arrpoints)):
        curSquare = squareTriangle(min_point, max_point, arrpoints[i])
        if maxSquare < curSquare:
            maxSquare = curSquare
            maxSquarePoint = arrpoints[i]
    return maxSquarePoint

def sidePoint(l, r, p):
    x, y = p
    x1, y1 = l
    x2, y2 = r
    D = (y2 - y1) * (x - x1) - (y - y1) * (x2 - x1)
    if D < 0:
        return 1
    if D > 0:
        return 0