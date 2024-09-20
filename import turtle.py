import turtle

# Configurar la pantalla
s = turtle.Screen()
s.bgcolor("black")

# Crear un objeto turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(2)

# Colores
colors = ("red", "blue", "cyan", "purple", "orange", "green")

# Función para dibujar patrones
def draw_pattern():
    for n in range(20):  # Aumentar el número de capas
        t.pencolor(colors[n % len(colors)])
        for x in range(12):  # Aumentar el número de repeticiones
            for i in range(2):
                t.circle(100 + n * 15, 90)  # Aumentar el radio base
                t.left(90)
            t.left(30)  # Mantener el ángulo para un diseño fluido

# Dibujar el patrón
draw_pattern()

# Finaliza
s.exitonclick()

