#-----------
#bibliotecas
#-----------
import esp
esp.osdebug(None)
#essa classe garante que toda memoria em desuso vai ser liberada
import gc
gc.collect() 
import network
import time
from util import open_json, web_register_uix

#-------------------
#Conectar com o wifi
#-------------------

#Coleta das de dados variaveis
survey_data = open_json()

ssid = survey_data['ssid']
password = survey_data['pwd']

#sistema que vai conectar a EPS ao wifi determnado em vars
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
time.sleep(5)

#Caso de tudo certo vai conectar e notificar
if station.isconnected() == True:
    print('Conectado com Sucesso ------------------------------')
    print(station.ifconfig())
    
#Se der errado ela vai gerar uma rede propria, nessa rede vai ser possivel atualizar qualquer dado
else:
    ap = network.WLAN(network.AP_IF)     
    ap.active(True)                      
    ap.config(essid='ESP32-IoT-BlueShift',password=b"Be@Loved", channel=11, authmode=network.AUTH_WPA_WPA2_PSK)
    print('Falha ao se conectar, acesse a Rede IP e reconfigure a conex閼肩幈')
    ap.ifconfig(('192.168.15.5', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
    print('http://192.168.15.5')
    web_register_uix() #Sitema que ativa a pagina web para atualizar os dados
    time.sleep(350)
    print('Reiniciando após 5 minutos')
    machine.reset()
    

#---
#OTA
#---

# Usamos o protocolo OTA para atualizar nosso sistema remotamente, basta redefinir os dados presentes abaixo e n閼肩幈 mexer nunca no senko.py
from senko import Senko
OTA = Senko(user="Badprofusion", repo="esp32nutritec", working_dir="/data", files=["boot.py", "main.py", "robust.py", "simple.py", "util.py", "vars.json"])

try:
    if OTA.update():
        print("Updated to the latest version! Rebooting...")
        machine.reset()
        #if __name__ == "__main__":
        #  main()
except:
    print('Sem Att no momento')
    None



