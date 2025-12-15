# =========================================
# PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
# Cálculo del promedio semanal del clima
# =========================================

class ClimaSemanal:
    """
    Clase que representa el clima de una semana.
    Contiene las temperaturas diarias y las operaciones
    necesarias para calcular el promedio.
    """

    def __init__(self):
        # Atributo privado que almacena las temperaturas
        # El doble guion bajo aplica encapsulamiento
        self.__temperaturas = []

    def ingresar_temperaturas(self):
        """
        Método que solicita al usuario ingresar
        las temperaturas de los 7 días.
        """
        
        # Bucle para recorrer los 7 días de la semana
        for dia in range(1, 8):
            # Solicita la temperatura del día actual
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            
            # Almacena la temperatura dentro del atributo privado
            self.__temperaturas.append(temp)

    def calcular_promedio(self):
        """
        Método que calcula y retorna el promedio semanal.
        """
        
        # Calcula el promedio usando los datos encapsulados
        promedio = sum(self.__temperaturas) / len(self.__temperaturas)
        
        # Retorna el promedio calculado
        return promedio


# Función principal del programa
def main():
    # Mensaje inicial
    print("Cálculo del promedio semanal del clima (POO)")
    
    # Se crea un objeto (instancia) de la clase ClimaSemanal
    clima = ClimaSemanal()
    
    # Se llaman los métodos del objeto para ingresar datos
    clima.ingresar_temperaturas()
    
    # Se calcula el promedio semanal usando el método de la clase
    promedio = clima.calcular_promedio()
    
    # Se muestra el resultado final en pantalla
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
    