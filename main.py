import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500,400)
screen.bgcolor("orange")
screen.title("Turtle Race")
user_bet = screen.textinput(title="Bet on!", prompt="Which turtle will win the race?")
colors=["red","purple","yellow","green","blue",""]
y_pos=[-100,-50,0,50,100]
turtle_list=[]
def CreateTurtles():
    for turtle_index in range(len(colors)-1):
        turtle = Turtle(shape="turtle")
        turtle.color(colors[turtle_index])
        turtle.penup()
        turtle.goto(x=-230, y=y_pos[turtle_index])
        turtle_list.append(turtle)
if user_bet:
    CreateTurtles()
    is_race_on = True

while is_race_on == True:
    for turtle in turtle_list:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet.lower():
                print(f"You won! The {winning_color} wins the race!")
            else:
                print(f"You lost! The {winning_color} wins the race!")
screen.exitonclick()