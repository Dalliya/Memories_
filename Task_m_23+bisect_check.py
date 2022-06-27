# Согласно древней индийской легенде создатель шахмат за своё изобретение попросил у раджи незначительную, на первый взгляд, награду:
# столько пшеничных зёрен, сколько окажется на шахматной доске, если на первую клетку положить одно зерно, на вторую — два зерна,
# на третью — четыре зерна и т. д. Оказалось, что такого количества зерна нет на всей планете (оно равно 2**64 − 1 зерен).
# Посчитайте, начиная с какой клетки по счету, общее количество зерен, которое должен был бы отдать раджа изобретателю было больше
# 1 000 000 зерен и сколько конкретно зерен он должен был бы отдать.
#      def chess_reward(): # returns 2 ints (cell number and total number of corns)
# 		pass
#
#    23* Разобраться с Enum и переписать игру с его использованием.

from bisect import bisect_left

def chess_reward():
    total_number_of_corns = 2 ** 64 - 1
    cells = []
    for i in range(64):
        cells.append(2 ** i)
    print(cells)

    index = bisect_left(cells, 1000000)
    if index < len(cells):
        return index + 1, cells[index], total_number_of_corns

print(chess_reward())



