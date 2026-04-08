class Temperatura:
    def __init__(self, temp):
        self._celcius = temp

    def leerCelcius(self):
        return self._celcius

    def leerFahrenheit(self):
        return self._celcius * 9/5 + 32

t1 = Temperatura(38)
t2 = Temperatura(24)

print(t1.leerCelcius(), t1.leerFahrenheit())
print(t2.leerCelcius(), t2.leerFahrenheit())