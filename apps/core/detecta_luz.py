#!/usr/bin/env python3

import smbus
import time
import paho.mqtt.client as mqtt
from time import sleep

# Definicoes do datasheet do sensor

ENDERECO = 0x23 # Endereco I2C padrao

CANAL = 1 # Canal onde o sensor esta.

# Uma medicao com resolucao de 1 lx a cada

# 120 ms.

ONE_TIME_HIGH_RES_MODE_1 = 0x20

i2c = smbus.SMBus(CANAL) # Inicia um canal.

# Esta funcao converte um valor dividido em 2 bytes

# em um valor decimal.

def converteParaNumero(dado):
        resultado = (dado[1] + (256 * dado[0])) / 1.2
        return (resultado)
# Le os dados da interface I2C

def leLuz(endereco):
        dado = i2c.read_i2c_block_data(endereco,ONE_TIME_HIGH_RES_MODE_1)
        return converteParaNumero(dado)

TOPICO = "/dev_iot_impacta/grupo/106/controle"
TOPICO1 = "/dev_iot_impacta/grupo/106/sensor/02/"

client = mqtt.Client()
lient.connect("mqtt.eclipse.org", 1883, 60)

while True:
   nivelLuz = leLuz(ENDERECO)
   print("Nivel de iluminacao : " + str(nivelLuz) + " lx")
   time.sleep (0.5)
   if nivelLuz < 100:
      aviso = '0'
   else:
      aviso = '1'
   dado = aviso.encode()
   client.publish(TOPICO, dado, qos=0)
   dado = str(nivelLuz).encode()
   client.publish(TOPICO1, dado, qos=0)
   sleep(2)
