# Два поезда движутся на скорости V1 и V2 навстречу друг другу. Между ними 10 км. пути.
# Через 4 км пути первый поезд может свернуть на запасной путь. При заданных скоростях узнать столкнутся ли поезда.
# def have_trains_crashed(v1, v2): # returns boolean value
#			pass

v1 = int(input("Insert the speed of the first train = "))
v2 = int(input("Insert the speed of the second train = "))

def have_trains_crashed(v1, v2):
    d = 10
    spare_path = 4
    if v2 / v1 >= (d - spare_path) / spare_path:
        return True #Trains will collide
    else:
        return False #Trains will not collide

print(have_trains_crashed(v1, v2))