class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)
    


rectangulo1 = Rectangulo(4, 7)
print(rectangulo1.area()) 
print(rectangulo1.perimetro()) 