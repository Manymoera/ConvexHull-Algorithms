from Algorithms import *
from Visualzation import *
from MakeTest import *
import datetime
def read_file(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            coordinates = line.split(' ')
            x = float(coordinates[0])
            y = float(coordinates[1])
            point = (x, y)
            points.append(point)

    return points

MakeTest(500, 'ConvexHullTaskRand.txt')

points=read_file('ConvexHullTask.txt')
points_rand = read_file('ConvexHullTaskRand.txt')

#----------Джарвис----------#
print('Jarvis Algorithm is running...')
cur_time = datetime.datetime.now()
convexHullJarvis(points_rand, 'ConvexHullResJr.txt')
res_time = datetime.datetime.now()
elapsed_time = res_time - cur_time
print('Execution time of Jarvis Algorithm:', elapsed_time, 'seconds')
#---------------------------#

#----------Грэхэм----------#
print('Graham Algorithm is running...')
cur_time = datetime.datetime.now()
GrahamHull(points_rand, 'ConvexHullResGr.txt')
res_time = datetime.datetime.now()
elapsed_time = res_time - cur_time
print('Execution time of Graham Algorithm:', elapsed_time, 'seconds')
#--------------------------#

#----------Быстрая оболочка----------#
print('Quick Hull Algorithm is running...')
cur_time = datetime.datetime.now()
QuickHullAlg(points_rand, 'ConvexHullResQuickAlg.txt')
res_time = datetime.datetime.now()
elapsed_time = res_time - cur_time
print('Execution time of Quick Hull Algorithm:', elapsed_time, 'seconds')
#------------------------------------#

drawAlgo(points_rand, read_file('ConvexHullResJr.txt'), "Алгоритм Джарвиса")
drawAlgo(points_rand, read_file('ConvexHullResGr.txt'), "Алгоритм Грэхэма")
drawAlgo(points_rand, read_file('ConvexHullResQuickAlg.txt'), "Алгоритм быстрой оболочки")