# proyecto1_pandas

RESUMEN: la información de la que parto es un dataframe que me indica valores relacionados con ataques de tiburones.
Tras importarme el csv correspondiente y las librerías que voy a utilizar, lo siguiente que he hecho es presentar mis hipótesis sobre los datos que me proporciona el dataframe. De este modo, necesitaré limpiar los datos facilitados para poder comprobar dichas hipótesis.

   Limpieza de datos tras análisis de columnas:
   1. He eliminado las columnas que definitivamente no me iban a aportar ningún valor.
   2. A continuación he borrado las filas que tuvieran TODOS los valores duplicados.
   3. Después he sustituido los valores Nan por Unknown/Invalid para cada una de las columnas, pasando de ser float a ser un string. Para ello reviso primero cuáles de los valores son categóricos.
   4. COMIENZO CON LA LIMPIEZA DE COMLUMNAS.
    4.1 Las columnas "Type", "Sex" y "Fatal (Y/N" cuentan con muy pocos valores únicos por lo que puedo hacer un reemplazo de valores directamente.
    4.2 El resto de columnas cuentan con muchos más valores únicos por lo que me valgo de métodos regex para buscar palabras dentro de la lista de valores únicos y agruparlas teniendo en cuenta que se refieran a lo mismo.
        - Columna "Activity"--> agrupo valores renombrando valores únicos mediante regex. Compruebo la frecuencia en la que se repiten los valores únicos que me han quedado, y hay muchos con frecuencia 1 por lo que me creo un diccionario solo con las valores unicos de frecuencia =1. Mi intención es conseguir que para todos los valores de mi lista_actividad_unknown(lista con valores de frecuencia 1) que se encuentran en mi lista Actividad_limpio (lista con todos los valores únicos de la columna Activity), me devuelva el valor "Unknown".
        - Columna "Species"--> he agrupado valores únicos mediante regex.
        - Columna "Date"--> en este caso he realizado una función para agrupar las fechas dadas solo por el mes, que es lo que me interesa para mi hipótesis. He creado una nueva columna agrupada por meses a partir de la columna Date.
        - Columna "Area", "Country" y "Location"-->reviso los valores únicos, pero esta columna me da la información que hay, no puego agrupar. Solo necesitaré filtrar la columna Country para que me de los valores de uno de los países para comprobar mi hipótesis.
        - Columna "Name"--> Reviso la frecuencia de los valores únicos, y valoro que cuando la frecuencia es mayor que 3, no son nombres y quiero que me lo reemplace por "Other". Para ello uso la misma función que para la columna Activity.
        - Columna "Injury"--> he agrupado valores únicos mediante regex.
        - Columna "Time"--> no me da ninguna información relevante la hora de los accidentes.
        - Columna "Investigator or Source"--> no me da ninguna información relevante que se haya investigado por una u otra persona
        
   5. Creo un dataframe nuevo con las columnas que necesito para comprobar mis hipótesis.
   6. Agrupo parejas de columnas que necesito para comprobar mis hipótesis.
    
OBJETIVO DEL PROYECTO: demostrar las hipótesis indicadas inicialmente.

ESTRUCTURA DEL PROYECTO: 
- Un documento jupyter de limpieza 
- Un docuemnto jupyter de visualizacion
- Una carpeta gitignore
- Una carpeta src con archivos de limpieza de código
- Un archivo Readme

LIBRERÍAS USADAS:

import numpy as np
import pandas as pd
import seaborn as sb
import re
import src.cleaning_functions as cf

CONCLUSIÓN FINAL: