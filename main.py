class GCDCalculator:
    def __init__(self, a, b):
        """
        Inicializa el GCDCalculator con dos números enteros a y b.
        """
        self._a = None
        self._b = None
        self.a = a  # Utiliza el setter para inicializar con validación
        self.b = b  # Utiliza el setter para inicializar con validación

    @property
    def a(self):
        """
        Getter para obtener el valor de 'a'.
        """
        return self._a

    @a.setter
    def a(self, value):
        """
        Setter para establecer el valor de 'a' con validación.
        """
        if not isinstance(value, int):
            raise ValueError("El valor de 'a' debe ser un entero.")
        self._a = value

    @property
    def b(self):
        """
        Getter para obtener el valor de 'b'.
        """
        return self._b

    @b.setter
    def b(self, value):
        """
        Setter para establecer el valor de 'b' con validación.
        """
        if not isinstance(value, int):
            raise ValueError("El valor de 'b' debe ser un entero.")
        self._b = value

    def compute_gcd(self):
        """
        Calcula el MCD de los números a y b utilizando el algoritmo de divisiones sucesivas (Euclides).
        """
        x = abs(self.a)  # Tomar el valor absoluto para evitar problemas con números negativos
        y = abs(self.b)  # Tomar el valor absoluto para evitar problemas con números negativos

        while y != 0:
            remainder = x % y
            x = y
            y = remainder

        return x

# Ejemplo de uso
gcd_calculator = GCDCalculator(48, 18)
print(f"El MCD de 48 y 18 es: {gcd_calculator.compute_gcd()}")  # Salida: 6

# Utilizando los setters para cambiar los valores
gcd_calculator.a = 56
gcd_calculator.b = 98
print(f"El MCD de 56 y 98 es: {gcd_calculator.compute_gcd()}")  # Salida: 14

# Intentar establecer un valor no entero para 'a' o 'b' generará un error
try:
    gcd_calculator.a = 56.5
except ValueError as e:
    print(e)  # Salida: El valor de 'a' debe ser un entero.
