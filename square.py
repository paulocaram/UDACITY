import turtle


def draw_circle():
    circulo = turtle.Turtle()
    circulo.shape("classic")
    circulo.color("blue")
    circulo.circle(100)

def draw_triangle():
    triangulo = turtle.Turtle()
    triangulo.shape("triangle")
    triangulo.color("yellow")

    for i in range(0,3):
        triangulo.forward(100)
        triangulo.left(120)

def draw_square():
    brad = turtle.Turtle()
    brad.shape("classic")
    brad.color("white", "blue")
    brad.speed(2)
    inicio =0
    fim = 3

    while (inicio <= 3):
        brad.forward(100)
        brad.right(90)
        inicio += 1


if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor("red")
    draw_square()
    draw_circle()
    draw_triangle()
    window.exitonclick()
