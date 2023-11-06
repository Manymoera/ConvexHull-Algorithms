import  matplotlib.pyplot as plt
def drawAlgo(arrpoints: list, out, name):
    # Разделение координат точек на отдельные списки
    x_coords = [point[0] for point in arrpoints]
    y_coords = [point[1] for point in arrpoints]

    # Создание графика
    fig, ax = plt.subplots()

    plt.title(f"{name}")
    # Отображение точек на графике
    ax.scatter(x_coords, y_coords, color='red')

    # Делаем спетку для графика
    plt.grid(True)

    # Отображение линий образующих выпуклую оболочку
    for i in range(len(out)):
        ax.plot([out[i][0], out[(i + 1) % len(out)][0]],
                [out[i][1], out[(i + 1) % len(out)][1]], color='blue')

    # Отображения графика
    plt.show()