class numeroEntero:
    def MCD(self, a, b):
        x = abs(a)
        y = abs(b)

        while y != 0:
            remainder = x % y
            x = y
            y = remainder
        return x

    def mcm(self, a, b):
        # mcd*mcm =a * b
        return a * b / self.MCD(a, b)


if __name__ == '__main__':
    operacion = numeroEntero()
    print(f"MCD de {5} {10} es {operacion.MCD(5, 10)}")