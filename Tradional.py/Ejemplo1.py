# =========================================
# PROGRAMACIÓN TRADICIONAL
# Cálculo del promedio semanal del clima
# =========================================

def ingresar_temperaturas():
    """
    Función encargada de solicitar al usuario
    las temperaturas de los 7 días de la semana.
    """
    
    # Lista vacía donde se almacenarán las temperaturas
    temperaturas = []
    
    # Bucle que se repite 7 veces (una por cada día)
    for dia in range(1, 8):
        # Se solicita la temperatura del día actual
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        
        # Se agrega la temperatura ingresada a la lista
        temperaturas.append(temp)
    
    # Se retorna la lista completa de temperaturas
    return temperaturas


def calcular_promedio(temperaturas):
    """
    Función que calcula el promedio semanal
    a partir de una lista de temperaturas.
    """
    
    # Se suman todas las temperaturas de la lista
    suma_temperaturas = sum(temperaturas)
    
    # Se divide la suma para el número de días
    promedio = suma_temperaturas / len(temperaturas)
    
    # Se retorna el promedio calculado
    return promedio


# Función principal del programa
def main():
    # Mensaje inicial
    print("Cálculo del promedio semanal del clima (Programación Tradicional)")
    
    # Se llama a la función para ingresar las temperaturas
    temperaturas = ingresar_temperaturas()
    
    # Se calcula el promedio semanal llamando a la función correspondiente
    promedio_semanal = calcular_promedio(temperaturas)
    
    # Se muestra el resultado final en pantalla
    print(f"El promedio semanal de temperatura es: {promedio_semanal:.2f} °C")


# Verifica si el archivo se ejecuta directamente
# y no como un módulo importado
if __name__ == "__main__":
    main()
