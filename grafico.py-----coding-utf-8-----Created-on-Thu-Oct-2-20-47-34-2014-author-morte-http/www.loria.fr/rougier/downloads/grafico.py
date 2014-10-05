# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 20:47:34 2014

@author: morte

http://www.loria.fr/~rougier/downloads/mlp.py

"""


import sqlite3
import matplotlib.pyplot as plt

db_file = "Valores_anos_completos.db"
conectar = sqlite3.connect(db_file)
cursor = conectar.cursor()

#horarios: 00, 03, 06, 09, 12, 15, 18, 21

lista = cursor.execute("SELECT * FROM valor_anos_completos")
d = 0
lista_temp_ar = []
lista_dias = []
for linha in lista:
  if linha[2] == "2002" and linha[0] == "09":
  #if linha[2] == "2003" and linha[0] == "09":
  #if linha[2] == "2004" and linha[0] == "09": 
    print linha
    d = d + 1
    lista_temp_ar.append(float(linha[6]))
    lista_dias.append(d)
print d

plt.plot(lista_dias,lista_temp_ar, "go", lista_dias, lista_temp_ar,'g')
plt.xlabel("Dias")
plt.ylabel("Umidade relativa")
plt.show()

