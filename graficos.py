import matplotlib.pyplot as plt
import time
from main import *

def graficar():
    ejex = casosArray
    ejey = range(len(ejex))
    plt.plot(ejey, ejex)
    plt.ylabel('Número de infectados')
    plt.show()


while True:
    graficar()
    time.sleep(10)