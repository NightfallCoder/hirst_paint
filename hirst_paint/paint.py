#import colorgram

#rgb_color=[]
#colors = colorgram.extract('hirst_paint/download.jpg', 16)
#print(colors)
#for color in colors:
#    r=color.rgb.r
#    g=color.rgb.g
#    b=color.rgb.b
#    new_color=(r,g,b)
#    rgb_color.append(new_color)
#print(rgb_color)
import turtle as t
import random
yoon=t.Turtle()
yoon.speed('fastest')
yoon.penup()
yoon.hideturtle()
t.colormode(255)
color_list=[ (245, 235, 46), (195, 12, 34), (220, 160, 71), (42, 80, 177), (237, 40, 138), (32, 40, 156), (238, 229, 5), (40, 215, 69), (21, 150, 23), (209, 73, 21), (204, 32, 96), (66, 10, 28)]


yoon.setheading(225)
yoon.fd(300)
yoon.setheading(0)
number_of_dots=100
for counts in range(1,number_of_dots+1):
    yoon.dot(20,random.choice(color_list)) #chooses random color from color_list
    yoon.fd(50)

    if counts%10==0:
        yoon.setheading(90)
        yoon.fd(50)  
        yoon.setheading(180)
        yoon.fd(500)
        yoon.setheading(0)
screen=t.Screen()
screen.exitonclick()