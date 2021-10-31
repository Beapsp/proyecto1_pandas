# proyecto1_pandas

RESUMEN: la información de la que parto es un dataframe que me indica valores relacionados con ataques de tiburones.
Tras importarme el csv correspondiente y las librerías que voy a utilizar, lo siguiente que he hecho es presentar mis hipótesis sobre los datos que me proporciona el dataframe. De este modo, necesitaré limpiar los datos facilitados para poder comprobar dichas hipótesis.

   Limpieza de datos tras análisis de columnas:
   1. He eliminado las columnas que definitivamente no me iban a aportar ningún valor.
   2. A continuación he borrado las filas que tuvieran TODOS los valores duplicados.
   3. Después he sustituido los valores Nan por Unknown/Invalid para cada una de las columnas, pasando de ser float a ser un string. Para ello reviso primero cuáles de los valores son categóricos.
   4. COMIENZO CON LA LIMPIEZA DE COMLUMNAS.
    4.1 Las columnas "Type", "Sex" y "Fatal" cuentan con muy pocos valores únicos por lo que puedo hacer un reemplazo de valores directamente.
    4.2 El resto de columnas cuentan con muchos más valores únicos por lo que me valgo de métodos regex para buscar palabras dentro de la lista de valores únicos y agruparlas teniendo en cuenta que se refieran a lo mismo.
    
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