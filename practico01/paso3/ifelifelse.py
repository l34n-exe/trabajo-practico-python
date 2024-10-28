calificacion = int(input("Ingrese calificación del 0 al 100: "))

if 0 <= calificacion <= 19:
    print("Calificación: A")
elif 20 <= calificacion <= 39:
    print("Calificación: B")
elif 40 <= calificacion <= 59:
    print("Calificación: C")
elif 60 <= calificacion <= 79:
    print("Calificación: D")
elif 80 <= calificacion <= 100:
    print("Calificación: F")
else:
    print("ERROR, ingrese un valor dentro del rango")
