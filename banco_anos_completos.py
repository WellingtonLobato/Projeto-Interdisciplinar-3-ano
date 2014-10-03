# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 20:41:30 2014

@author: morte
"""

import xlrd
import os
import sqlite3


file_work = "Barcarena PCD.xls"
db_file = "Valores_anos_completos.db"

db_is_new = not os.path.exists(db_file)

if db_is_new:
  conectar = sqlite3.connect(db_file)
  cursor = conectar.cursor()
  try:
    cursor.execute("CREATE TABLE IF NOT EXISTS valor_anos_completos(hora TEXT NOT NULL, mes TEXT NOT NULL, ano TEXT NOT NULL, temp_ar TEXT, temp_max TEXT, temp_min TEXT, umi TEXT, pluvio TEXT)");
    print "Tabela criada com sucesso!"
  except:
    pass
else:
  conectar = sqlite3.connect(db_file)
  cursor = conectar.cursor()
 
work = xlrd.open_workbook(file_work)
sheet = work.sheet_by_index(0)
linhas_total = sheet.nrows
colunas_total = sheet.ncols

for l in range(1, linhas_total):
  hora = sheet.cell_value(l,0)
  temperatura_ar = sheet.cell_value(l,1)
  temperatura_max = sheet.cell_value(l,2)
  temperatura_min = sheet.cell_value(l,3)
  umidade_rel = sheet.cell_value(l,4)
  velocidade_vento = sheet.cell_value(l,5)
  velocidade_vento_max = sheet.cell_value(l,6)
  radiacao_sol = sheet.cell_value(l,7)
  pluvio = sheet.cell_value(l,8)
  pressao = sheet.cell_value(l,9)
  mes = sheet.cell_value(l,10)
  ano = sheet.cell_value(l,11)
  if str(ano) == "2002" or str(ano) == "2003" or str(ano) == "2004":
      print "Hora: ",hora," Temperatura do ar: ",temperatura_ar," Umidade: ",umidade_rel," Pluviosidade: ",pluvio," Mes: ",mes," Ano: ",ano
      cursor.execute("INSERT INTO valor_anos_completos VALUES(?,?,?,?,?,?,?,?)",(str(hora),str(mes),str(ano),str(temperatura_ar),str(temperatura_max),str(temperatura_min),str(umidade_rel),str(pluvio)))

conectar.commit()
cursor.close()
conectar.close()
