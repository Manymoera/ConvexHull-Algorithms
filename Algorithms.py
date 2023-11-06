from MiscFunc import *
from functools import cmp_to_key

def convexHullJarvis(points, file_path):
    l = left_index(points)
    hull = []
    prev_p = l
    q = 0
    n = len(points)
    while (True):
        hull.append(prev_p)
        # Ищем точку q, такую чтобы угловой коэф между
        # (prev_p, i, q) был отрицательным и наименьшим
        q = (prev_p + 1) % n
        for i in range(n):
            if (orientation(points[prev_p],
                            points[i], points[q]) == 2):
                q = i
        prev_p = q
        if (prev_p == l):
            break
    hull.reverse()
    with open(file_path, 'w') as file:
        for each in hull:
            file.write(str(int(points[each][0])) + ' ' + str(int(points[each][1])) + '\n')

def GrahamHullAlg(points, file_path):
    n = len(points)
    ymin = points[0][1]
    min = 0
    for i in range(1, n):
        y = points[i][1]
        if ((y < ymin) or (ymin == y and points[i][0] < points[min][0])):
            ymin = points[i][1]
            min = i

    points[0], points[min] = points[min], points[0]

    p0 = points[0]

    sorted_points = sorted(points, key = lambda p: (angle(p0, p), distSq(p0, p)))

    # Создаем пустой стэк и пушим в него первые три точки
    S = []
    S.append(sorted_points[0])
    S.append(sorted_points[1])
    S.append(sorted_points[2])

    # Обрабатываем оставшиеся n - 3 точек
    for i in range(3, n):

        #Продолжаем убирать точки с вершины пока угол, образующийся из
        #точек next-to-top, top и points[i] образуют
        #не левый поворот
        while ((len(S) > 1) and (orientation(nextToTop(S), S[-1], sorted_points[i]) != 2)):
            S.pop()
        S.append(sorted_points[i])

    #Теперь стэк имеет все нужны нам точки
    #Выводим содержимое стэка
    with open(file_path, 'w') as file:
        while S:
            p = S[-1]
            file.write(str(int(p[0])) + ' ' + str(int(p[1])) + '\n')
            S.pop()
def GrahamHull(arrPoints: list, file_path):

    if len(arrPoints) < 3:
        return arrPoints

    # Выбираем минимальную точку, которая будет входить в выпуклую оболочку
    startPoint = min(arrPoints, key=lambda p: (p[0], p[1]))

    # Сортируем точки по полярному углу и если полярный угол одинаковый, то сортируем по длине
    sorted_points = sorted(arrPoints, key=lambda p: (angle(startPoint, p), distSq(startPoint, p)))

    # Добавляем первые два элемента в нашу выпуклую оболочку
    convuxHull = [startPoint, sorted_points[0]]

    for i in range(1, len(sorted_points)):

        # Проходим циклом, пока три точки образуют не левый поворот или три точки лежат на прямой, убираем из стека последнюю точку
        while len(convuxHull) > 1 and ((orientation(nextToTop(convuxHull), convuxHull[-1], sorted_points[i]) != 2)):
            convuxHull.pop()

        # Иначе добавляем её в выпуклую оболочку
        convuxHull.append(sorted_points[i])

    convuxHull.reverse()

    with open(file_path, 'w') as file:
        for each in convuxHull:
            file.write(f"{int(each[0])} {int(each[1])} " + '\n')
def quickAlgorithm(arrPoints, leftPoint, rightPoint, side):
    newArrPoints = []
    result = []

    if side == 1:
        # Проходим по каждой точке нашего массива и добавляем её в верхнюю часть оболочки
        for point in arrPoints:
            if sidePoint(leftPoint, rightPoint, point) == 1:
                newArrPoints.append(point)
        if len(newArrPoints) > 0:
            # Вычисляем максимальную площать треугольника, которая образовалось
            # Благодаря трем точкам
            topPoint = maxSquare(newArrPoints, leftPoint, rightPoint)
            # Добавляем точку в наш массив и повторяем наш алгоритм для
            # Следующих треугольников
            result.append(topPoint)
            result.extend(quickAlgorithm(newArrPoints, leftPoint, topPoint, side))
            result.extend(quickAlgorithm(newArrPoints, topPoint, rightPoint, side))
    else:
        # Проходим по каждой точке нашего массива и добавляем её в верхнюю часть оболочки
        for point in arrPoints:
            if sidePoint(leftPoint, rightPoint, point) == 0:
                newArrPoints.append(point)
        # Если в массиве есть хотя-бы одна точка выполняем
        if len(newArrPoints) > 0:
            # Вычисляем максимальную площать треугольника, которая образовалось
            # Благодаря трем точкам
            downPoint = maxSquare(newArrPoints, rightPoint, leftPoint)
            # Добавляем точку в наш массив и повторяем наш алгоритм для
            # Следующих треугольников
            result.append(downPoint)
            result.extend(quickAlgorithm(newArrPoints, leftPoint, downPoint, side))
            result.extend(quickAlgorithm(newArrPoints, downPoint, rightPoint, side))

    return result
def QuickHullAlg(arrPoints, file_path):

    if len(arrPoints) < 3:
        return arrPoints

    # Берем минимальную точку и максимальную
    minPoint = min(arrPoints, key=lambda p: (p[0], p[1]))
    maxPoint = max(arrPoints, key=lambda p: (p[0], p[1]))

    result = []
    result1 = []
    convexHull = []

    convexHull.append(minPoint)
    # Вызываем и добавляем точки из нижней части
    result.extend(quickAlgorithm(arrPoints, minPoint, maxPoint, -1))
    result.sort()
    convexHull.extend(result)
    convexHull.append(maxPoint)

    # Вызываем и добавляем точки из верхней части
    result1.extend(quickAlgorithm(arrPoints, minPoint, maxPoint, 1))
    result1.sort()
    result1.reverse()
    convexHull.extend(result1)
    convexHull.reverse()

    with open(file_path, 'w') as file:
        for each in convexHull:
            file.write(f"{int(each[0])} {int(each[1])} " + '\n')