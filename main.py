import matplotlib.pyplot as plt

import requests
from bs4 import BeautifulSoup
from plyer import notification
import time

prev_casos = "0"
aumentos = ['13', '2599', '39', '161', '370', '2', '54', '15', '173', '25', '69', '2262', '3', '1', '94', '19', '828', '53', '1105', '99', '698', '114', '12', '7', '3', '1', '55', '191', '22', '105', '26']
casosArray = []


def extract():
  global prev_casos
  global aumentos
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
      print('[' + time.strftime('%l:%M:%S %p on %b %d, %Y') + ' ] aumentó de ' + prev_casos + ' a ' + casos)
      aumento = str(casosint - prev_casosint)
      caso = prev_casos
      notifyMe('El total de número de casos aumentó en', aumento)

      aumentos.append(aumento)
      casosArray.append(caso)
      print(aumentos)
      print(casosArray)
      
      #plt.plot(aumentos, range(len(aumentos)))
      #plt.show()
    
    prev_casos = casos

def notifyMe(title, message):
  notification.notify(title=title, message=message, timeout=6)

while True:
  extract()
  time.sleep(30)

