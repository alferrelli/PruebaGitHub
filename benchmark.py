# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 08:42:53 2021

@author: aferrelli
"""

import pandas as pd


def market_Data():
    df = pd.read_csv('GGAL.csv')
    return df


def RSI(df, periodos):
    
    #RSI tiene 2 formulas
    
    #====FORMULA RSI PASO 1 Fuerza Relativa de 14 ruedas=======
    #diff() calcula la diferencia entre el valor de esta fila
    #y el de la fila anterior,para toda la serie de datos
    diferencia_cierre = df['Close'].diff()
    
    #ver dataframe
    #print(diferencia_cierre)
    
    #cierres positivos y negativos normalizados
    #clip() evita que los valores de una serie superen o
    #esten debajo de un valor especifico
    #la serie tiene valores negativos,se fuerzan a 0
    #solo se aceptan valores positivos en cada serie
    cierres_positivos = diferencia_cierre.clip(lower=0)
    cierres_negativos = -1 * diferencia_cierre.clip(upper=0)
    
    #print(cierres_negativos)
    
    #usar media exponencial
    #para suavizar los resultados   
    #IMPORTANTE: Hay varias maneras de suavizar una media exponencial
    #usando el factor de decaimiento (explicado en clase)
    #esta implementacion es la que mejor se acerca a TradingView en las pruebas que hice
    #con mi playlist. En otras plataformas o incluso otros activos puede no ser exactamente 
    #igual. En tales casos, la formula del alpha (decaimiento) deberia ser modificada para matchear
    #siempre verificar calculos vs plataforma donde se mete el trade. SIEMPRE.
    cierres_positivos_suave = cierres_positivos.ewm(alpha = 1/(periodos), adjust=False, min_periods = periodos).mean()
    cierres_negativos_suave = cierres_negativos.ewm(alpha = 1/(periodos), adjust=False, min_periods = periodos).mean()
    
    
    rsi = cierres_positivos_suave / cierres_negativos_suave
    
    
    #====FORMULA RSI PASO 2 Obtener Indice de Fuerza Relativa =======
    rsi = 100 - (100/(1 + rsi))
    return rsi



############################ PROGRAMA PRINCIPAL ############################

periodos = 14
df_activo = market_Data()


df_activo['Rsi']= RSI(df_activo, periodos)

df_activo = df_activo.set_index(df_activo['Date'])
df_activo.drop('Date',inplace=True, axis=1)

posicion_historica =  pd.DataFrame()
tengo_posicion = False



i = 0
for rsi in df_activo['Rsi']:
    
    if rsi < 30:
          if not tengo_posicion:
              
              print('compre')
              print(rsi)
              tengo_posicion = True
        
    if rsi > 70:
          if tengo_posicion:
              
              print('vendi')
              print(rsi)
              tengoPosicion = False
   
    i = i + 1
    





















