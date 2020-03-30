import matplotlib.pyplot as plt

import requests
from bs4 import BeautifulSoup
from plyer import notification
import time

prev_casos = "0"
casosArray =  [721019, 721051, 721056, 721224, 721266, 721273, 721277, 721293, 721300, 721312, 721323, 721324, 721330, 721370, 721412, 721503, 721562, 721902, 721903, 721946, 721951, 721956, 740239, 740685, 740695, 740737, 740743, 741774, 741777, 741907, 741908, 741914, 742283, 742339, 742428, 742444, 742462, 742506, 742531, 742556, 743081, 743147, 743179, 743190, 743255, 743286, 743369, 743370, 743402, 743437, 746056, 746062, 746107, 746111, 746112, 746178, 746218, 748066, 748139, 752189, 752241, 752263, 752288, 752297, 752385, 752444, 752678, 752687, 752733, 752747, 752830, 752854, 752861, 753346, 753367, 753385, 759203, 759302, 759321]

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
  plt.plot(ejey, ejex)
  plt.ylabel('Número de infectados')
  plt.show()

while True:
    graficar()
    time.sleep(1)