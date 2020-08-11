import turtle

shelly = turtle.Turtle()



for i in range(12):
    shelly.color('red')
    shelly.circle(100)
    shelly.left(360/12)
    print(i)

square_length = 400

shelly.penup()
shelly.goto(-(square_length/2), (square_length/2))
shelly.pendown()

shelly.color('green')

square_width = 400

for i in range(4):
    shelly.forward(square_length)
    shelly.left(-90)

# shelly.forward(100)

# shelly.home()

turtle.mainloop()

