import numpy as np

def MakeTest(arrSize, file_path):
    arr = []
    for each in range(arrSize):
        x = np.random.randint(0, 1000)
        y = np.random.randint(0, 1000)
        point = (x, y)
        arr.append(point)
    with open(file_path, 'w') as file:
        for each in arr:
            file.write(f"{int(each[0])} {int(each[1])} " + '\n')