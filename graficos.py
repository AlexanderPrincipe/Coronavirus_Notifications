import matplotlib.pyplot as plt
from main import *

def graficar2():
    ejex = ['13', '2599', '39', '161', '370', '2', '54', '15', '173', '25', '69', '2262', '3', '1', '94', '19', '828', '53', '1105', '99', '698', '114', '12', '7', '3', '1', '55', '191']
    ejey = range(len(ejex))

    plt.plot(ejex, ejey)
    plt.show()

graficar2()