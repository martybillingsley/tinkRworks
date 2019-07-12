# Turtle Drawing
## Start with drawing some shapes. 

Let's examine the draw.py program in the window on the left:<br>
`import turtle` tells Python to load a whole bunch of functions that allow us to create turtles and move them around. <br>
`win = turtle.Screen()` creates and opens a new window that we are calling **win**. Every window contains a canvas that is the part of the window a turtle can move around in and draw on.<br>
`alex = turtle.Turtle()` creates a turtle that we are calling **alex**. Technically, alex is a variable that refers to this new turtle.<br>
<br>
<h4>Turtle commands</h4>
`forward (`distance in pixels`)` makes a turtle go forward some distance. <br>
example: `alex.forward(50)` will make the turtle called alex move forward 50 pixels<br>
`backward` works in much the same way<br>
<br>
`right (`degrees`)` makes a turtle turn to the right some number of degrees<br>
example: `alex.right(45)` will make the turtle called alex turn right 45 degrees<br>
`left` works in much the same way<br>
<br>
[Click here for more Turtle commands](https://lab.cs50.io/martybillingsley/tinkRworks/master/turtleDraw/turtleReference.pdf) <br>
<br>
<h4>Try it out</h4>
Add commands to make alex move and turn and move again.<br>
To run your program, type `python draw.py` in the terminal window at the bottom of your screen.<br>


{% spoiler "Help" %}
Add these lines to the program draw.py, after the line `alex = turtle.Turtle()` and before the line `turtle.done()`:<br>
`alex.forward(50)`<br>
`alex.right(90)`<br>
`alex.forward(30)`<br>
`alex.left(45)`<br>
`alex.forward(50)`<br>
The turtle should draw a shape that looks like this:<br>
![Simple tree](https://raw.githubusercontent.com/martybillingsley/images/turtleDrawImages/master/turtleDraw1.png) 
![First drawing](https://raw.githubusercontent.com/martybillingsley/images/turtleDrawImages/master/turtleDraw1.png) <br>
![Tree](https://raw.githubusercontent.com/martybillingsley/images/master/tree3.png) <br>
{% endspoiler %}



{% next  %}

## Add commands to make alex draw a square
{% spoiler "Help" %}
help goes here, along with questions:
how many degrees in a circle
how many sides to a square, etc.
{% endspoiler %}
