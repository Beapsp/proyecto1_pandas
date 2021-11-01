# proyecto1_pandas

RESUMEN: la información de la que parto es un dataframe que me indica valores relacionados con ataques de tiburones.
Tras importarme el csv correspondiente y las librerías que voy a utilizar, lo siguiente que he hecho es presentar mis hipótesis sobre los datos que me proporciona el dataframe. De este modo, necesitaré limpiar los datos facilitados para poder comprobar dichas hipótesis.

--> Comienzo trabajando en un jupyter notebook de limpieza de datos:
     
   Limpieza de datos tras análisis de columnas:
   1. He eliminado todas las filas que tienen todos sus valores NaN
   2. A continuación he borrado las filas que tuvieran TODOS los valores duplicados.
   3. He modificado los nombres de columnas que tenían algún espacio para poder trabajar mejor.
   3. He eliminado las columnas que definitivamente no me iban a aportar ningún valor.
   4. Después he sustituido los valores Nan por Unknown/Invalid para cada una de las columnas, pasando de ser float a ser un string. Para ello reviso primero cuáles de los valores son categóricos.
   5. COMIENZO CON LA LIMPIEZA DE COLUMNAS.
    5.1 Las columnas "Type", "Sex" y "Fatal (Y/N" cuentan con muy pocos valores únicos por lo que puedo hacer un reemplazo de valores directamente.
    5.2 El resto de columnas cuentan con muchos más valores únicos por lo que me valgo de métodos regex para buscar palabras dentro de la lista de valores únicos y agruparlas teniendo en cuenta que se refieran a lo mismo.
        - Columna "Activity"--> agrupo valores renombrando valores únicos mediante regex.Creo una función con un diccionario donde la key es la columna y el value es el patrón de regex. Itero en ese diccionario para que devuelva el valor indicado, si cumple la condición, y sino me devuelva el valor "other".
        - Columna "Species"--> he agrupado valores únicos mediante regex y he utilizado la misma función usada en la columna Activity.
        - Columna "Injury"--> he agrupado valores únicos mediante regex y he utilizado la misma función usada en la columna Activity.
        - Columna "Date"--> en este caso he realizado una función para agrupar las fechas dadas solo por el mes, que es lo que me interesa para mi hipótesis. He creado una nueva columna agrupada por meses a partir de la columna Date.
        - Columna "Area", "Country" y "Location"-->reviso los valores únicos, pero esta columna me da la información que hay, no puego agrupar. Solo necesitaré filtrar la columna Country para que me de los valores de uno de los países para comprobar mi hipótesis.
        - Columna "Name"--> no me da ninguna información relevante para comprobar mis hipótesis.
        - Columna "Time"--> no me da ninguna información relevante la hora de los accidentes.
        - Columna "Investigator or Source"--> no me da ninguna información relevante que se haya investigado por una u otra persona

--> Continúo trabajando en un jupyter notebook para la visualización de los datos ya limpios.

   6. Creo un dataframe nuevo solo con las columnas que necesito para comprobar mis hipótesis.
   7. Agrupo parejas de columnas que necesito para comprobar mis hipótesis.
   8. Genero gráficos que me representen visualmente dichas hipótesis.
    
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
import sys
sns.set_context("poster")
sns.set(rc={"figure.figsize": (12.,6.)})
sns.set_style("whitegrid")
!conda install --yes --prefix {sys.prefix} plotly

CONCLUSIÓN FINAL:

1. Hipótesis 1--> Se refuta mi hipótesis ya que se dan más ataques en hombres realizando la actividad swimming que realizando Wind Surfing.
2. Hipótesis 2--> Se confirma mi segunda hipótesis de que se dan más ataques en el mes de junio que en el mes de febrero.
3. Hipótesis 3--> Se confirma mi hipótesis 3 de que hay más ataques de tiburón blanco en USA que en Australia.