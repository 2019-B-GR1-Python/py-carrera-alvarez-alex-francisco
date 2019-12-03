# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 07:54:57 2019

@author: LaLeS
"""

import pandas as pd
import numpy as np
import os
import sqlite3

path_guardado_bin = "D://RESPALDOS//EPN//Python//py-carrera-alvarez-alex-francisco//05_Python_Pandas//data//artwork_data_completo.pickle"
df5 = pd.read_pickle(path_guardado_bin)
df = df5.iloc[49980:50519,:].copy()
#  Tipos archivos
#  JSON
#  EXCEL
#  SQL

### EXCEL ##
path_guardado = 'D://RESPALDOS//EPN//Python//py-carrera-alvarez-alex-francisco//05_Python_Pandas//data////mi_df_completo.xlsx'
df.to_excel(path_guardado)
df.to_excel(path_guardado, index=False)
columnas = ['artist','title','year']
df.to_excel(path_guardado, columns=columnas)

### Multiples hojas de trabajo ###

path_multiple = 'D://RESPALDOS//EPN//Python//py-carrera-alvarez-alex-francisco//05_Python_Pandas//data////mi_df_multiple.xlsx'
writer = pd.ExcelWriter(path_multiple,
                        engine='xlsxwriter')

df.to_excel(writer, sheet_name = 'Primera')

df.to_excel(writer, sheet_name = 'Segunda',
            index=False)

df.to_excel(writer, sheet_name = 'Tercera',
            columns=columnas)

writer.save()


### Multiples hojas de trabajo ###

num_artistas = df['artist'].value_counts()
path_colores = 'D://RESPALDOS//EPN//Python//py-carrera-alvarez-alex-francisco//05_Python_Pandas//data////mi_df_colores.xlsx'

writer = pd.ExcelWriter(path_colores,
                        engine='xlsxwriter')

num_artistas.to_excel(writer, 
                      sheet_name='Artistas')


hoja_artistas = writer.sheets['Artistas']

rango_celdas = 'B2:B{}'.format(len(num_artistas.index) + 1)

formato_artistas = {
        "type": "2_color_scale",
        "min_value": "10",
        "min_type": "percentile",
        "max_value": "99",
        "max_type": "percentile"}

hoja_artistas.conditional_format(rango_celdas,
                                 formato_artistas)

writer.save()



