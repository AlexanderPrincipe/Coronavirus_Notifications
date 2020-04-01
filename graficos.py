import matplotlib.pyplot as plt

import requests
from bs4 import BeautifulSoup
from plyer import notification
import time

prev_casos = "0"
casosArray = [721019, 721051, 721056, 721224, 721266, 721273, 721277, 721293, 721300, 721312, 721323, 721324, 721330, 721370, 721412, 721503, 721562, 721902, 721903, 721946, 721951, 721956, 740239, 740685, 740695, 740737, 740743, 741774, 741777, 741907, 741908, 741914, 742283, 742339, 742428, 742444, 742462, 742506, 742531, 742556, 743081, 743147, 743179, 743190, 743255, 743286, 743369, 743370, 743402, 743437, 746056, 746062, 746107, 784392, 784440, 784794, 784832, 784978, 785217, 785218, 785219, 785320, 785378, 785409, 785534, 785551, 785678, 785684, 785686, 785712, 785713, 785715, 785720, 785774, 785775, 785777, 785779, 785780, 785797, 785807, 858674, 858678, 858722, 858753, 858755, 858756, 858797, 858892, 858916, 858938, 859031, 859032, 859025, 859145, 859338]

def graficar():
  global prev_casos

  # Casos confirmados de Coronavirus en el mundo
  res = requests.get('https://www.worldometers.info/coronavirus/').text
  soup = BeautifulSoup(res, 'html.parser')
  soup.encode('utf-8')
  casosint = int((soup.find("div", { "class": "maincounter-number" }).get_text().strip()).replace(',',""))
  
  casosArray.append(casosint)

  ejex = casosArray
  ejey = range(len(ejex))

  #ejey = ['28/03/2020','29/03/2020','30/03/2020']

  plt.plot(ejey, ejex)
  plt.title('Gráfica de infectados')
  plt.ylabel('Número de infectados')
  plt.show()

while True:
    graficar()
    time.sleep(0.001)