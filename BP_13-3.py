from turtle import*

class Car:
    def __init__(self, speed, color,model):
        self.speed=speed
        self.color=color
        self.model=model
        self.turtle=Turtle()
        self.turtle.shape("car.gif")

    def drive(self):
        self.turtle.forward(self.speed)

    def left_turn(self):
        self.turtle.left(90)

register_shape("C:\Users\82107\Desktop\새 폴더 (2)\car.gif.png")
myCar=Car(200, "red", "E-class")
for i in range(100):
    myCar.drive()
    myCar.left_turn()
   
