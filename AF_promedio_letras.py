
def promedio_letras(frase:str):
    separadores = [' ',',',':',';','-','*']
    frase_sin_espacios = frase
    print(frase)

    if len(frase)>0:    
        for separador in separadores:  
                    frase_sin_espacios = frase_sin_espacios.replace(separador, '') 
                    # reemplazo espacios, comas, punto y coma, dos puntos por un string vacio
                    # quedan solo las letras


        cantidad_letras = len(frase_sin_espacios)
        cantidad_palabras = len(frase.split())
        
        return (round(cantidad_letras/cantidad_palabras,4))
    else:
        raise Exception


frase = 'En AlgoTrading mostramos como la market data es todo'
try:
    promedio = promedio_letras(frase)
    print ('Promedio de Letras: ', promedio)
except:
    print("Debe ingresar una Frase")




