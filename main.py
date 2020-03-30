import matplotlib.pyplot as plt

import requests
from bs4 import BeautifulSoup
from plyer import notification
import time

prev_casos = "0"
aumentos = [358, 32, 5, 168, 42, 7, 4, 16, 7, 12, 11, 1, 6, 40, 42, 91, 59, 340, 1]
casosArray = [721019, 721051, 721056, 721224, 721266, 721273, 721277, 721293, 721300, 721312, 721323, 721324, 721330, 721370, 721412, 721503, 721562, 721902, 721903, 721946, 721951, 721956, 740239, 740685, 740695, 740737, 740743, 741774, 741777, 741907, 741908, 741914, 742283, 742339, 742428, 742444, 742462, 742506, 742531, 742556]
def extract():
  global prev_casos
  # Casos confirmados de Coronavirus en Perú
  # res = requests.get('https://www.worldometers.info/coronavirus/country/peru').text

  # Casos confirmados de Coronavirus en el mundo
  res = requests.get('https://www.worldometers.info/coronavirus/').text
  soup = BeautifulSoup(res, 'html.parser')
  soup.encode('utf-8')
  casos = (soup.find("div", { "class": "maincounter-number" }).get_text().strip())
  casosint = int((soup.find("div", { "class": "maincounter-number" }).get_text().strip()).replace(',',""))
  
  if(casos == prev_casos):
      print('['+ time.strftime('%l:%M:%S %p on %b %d, %Y') + '] SIN CAMBIOS EN EL NÚMERO DE CASOS (' + casos + ')')
  else:
    notifyMe('Total número de casos de CORONAVIRUS', casos)

    if(prev_casos != "0"):
      prev_casosint = int(prev_casos.replace(',', ""))
      print('[' + time.strftime('%l:%M:%S %p on %b %d, %Y') + '] aumentó de ' + prev_casos + ' a ' + casos)
      aumentostr = str(casosint - prev_casosint)
      aumentoint = (casosint - prev_casosint)
      print('El total de número de casos aumentó en', aumentostr)

      aumentos.append(aumentoint)
      casosArray.append(casosint)
      print(aumentos)
      print(casosArray)
      
      #plt.plot(aumentos, range(len(aumentos)))
      #plt.show()
    
    prev_casos = casos
    
    if(casosint >= 1000000):
      notifyMe('Superamos el millón de infectados con Coronavirus!!!!!', casosint)


def notifyMe(title, message):
  notification.notify(title=title, message=message, timeout=6)



while True:
  extract()
  time.sleep(30)

