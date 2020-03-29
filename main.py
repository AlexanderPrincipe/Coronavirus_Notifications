import requests
from bs4 import BeautifulSoup
from plyer import notification
import time

prev_casos = "0"
aumentos = []
def extract():
  global prev_casos
  # Casos confirmados en Perú
  #res = requests.get('https://www.worldometers.info/coronavirus/country/peru').text

  # Casos confirmados de Coronavirus en el mundo
  res = requests.get('https://www.worldometers.info/coronavirus/').text
  soup = BeautifulSoup(res, 'html.parser')
  soup.encode('utf-8')
  casos = (soup.find("div", { "class": "maincounter-number" }).get_text().strip()).replace(',',"")
  
  if(casos == prev_casos):
      print('['+ time.strftime('%l:%M:%S %p on %b %d, %Y') + ' ] SIN CAMBIOS EN EL NÚMERO DE CASOS')

  else:
    notifyMe('Total número de casos de CORONAVIRUS', casos)
    if(prev_casos != "0"):
      print('[' + time.strftime('%l:%M:%S %p on %b %d, %Y') + ' ] casos ROSE FROM ' + prev_casos + ' TO ' + casos)
      notifyMe('El total de número de casos aumentó en {}'.format(int(float(casos)) - int(float(prev_casos))))

      aumentos.append[int(float(casos)) - int(float(prev_casos))]
      print(aumentos)
    prev_casos = casos

def notifyMe(title, message):
  notification.notify(title=title, message=message, timeout=6)

while True:
  extract()
  time.sleep(10)