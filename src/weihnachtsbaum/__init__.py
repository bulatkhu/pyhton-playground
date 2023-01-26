import turtle

angle = 117


def drawTree(h, size):
    if h < 0:
        return
    length = size * 1.35 ** h
    turtle.forward(length)
    drawTree(h - 1, size)
    turtle.right(angle)
    drawTree(h - 2, size)
    turtle.right(2 * -angle)
    drawTree(h - 2, size)
    turtle.right(angle)
    turtle.forward(-length)
# Example usage
# turtle.penup()
# turtle.goto(0, -200)
# turtle.pendown()
