#Evaluación del 6 de octubre del 2023
#Realizar una clase en la cuál se declaren los valores por teclado

class Calculadora:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def suma(self):
        return self.n1 + self.n2

    def resta(self):
        return self.n1 - self.n2

    def multiplicacion(self):
        return self.n1 * self.n2

    def division(self):
        return self.n1 / self.n2


def main():
    n1 = int(input("Ingrese el primer número: "))
    n2 = int(input("Ingrese el segundo número: "))

    calculadora = Calculadora(n1, n2)

    print("Suma: ", calculadora.suma())
    print("Resta: ", calculadora.resta())
    print("Multiplicación: ", calculadora.multiplicacion())
    print("División: ", calculadora.division())


if __name__ == "__main__":
    main()

    #Explicación del código: El código funciona con la Clase: Calculadora y con los métodos __init__ que sirve para que 
    #el proceso se inicialice y con los métodos definidos suma, resta, multiplicación y división. Con los atributos self y los valores
    #n1 y n2 lo que se hace es tomar los dos números ingresados por el usuario y operarlos utilizando el operador respectivo para
    #cada operación, por ejemplo; cuando el usiario le de el valor 5 a n1 y 6 a n2, self va a tomar esos valores y los va a 
    #operar, si es suma sería n1 + n2 y así con las 4 operaciones establecidas
    #si no se cumple la condición de que haya al menos un carácter numerico, mostrar error. y con main se crea el punto de entrada
    #donde se pide al usuario ingresar los números y posterior a esto mostrar los resultados.
