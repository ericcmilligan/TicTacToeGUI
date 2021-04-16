from turtle import onscreenclick, Screen, shape
import turtle

screen = Screen()
screen.title("Tic Tac Toe Grid")
image = "grid.gif"
screen.addshape(image)
shape(image)
runforever = True

def get_mouse_click_coor(x, y):
    print(x, y)



onscreenclick(get_mouse_click_coor)

turtle.mainloop()

screen.exitonclick()




