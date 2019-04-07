import math
import time
import platform
import os
import my_modul as my  #псевдоним my

#print(math.fabs(-5))
#print(math.pi)
#print(os.getcwd()) #путь к файлу
#print("\n",platform.uname()) #инфа про операционку
#print(time.time()) #кол секунд из 1970
'''
print(my.some) #вывод перепеной из файла
my.printfd(my.some) #тоже вывод через встроеную функцию
res= my.summ(5,6,7,8,3)
print(res)
'''
#импортировать кусок
from my_modul import printfd as pr, some # as псевдоним
pr(some)
from math import pi
pr(pi)
