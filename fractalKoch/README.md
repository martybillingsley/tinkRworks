# Koch Snowflake
The Koch snowflake is a fractal curve made by taking a triangle and replacing each straight line segment with a pattern of three line segments. Repeated over and over (to infinity, in theory) you end up with a shape that has an infinitely long perimeter, but is contained in a finite area. 

## Try drawing one side of the triangle 
Write a function to draw one line segment (one side of the triangle).  As with the fractal trees, it's easiest to use a depth argument to control the complexity of the curve:

depth 0: ![Koch depth 0](https://raw.githubusercontent.com/martybillingsley/images/master/koch1.png) 
depth 1: ![Koch depth 1](https://raw.githubusercontent.com/martybillingsley/images/master/koch2.png) 
depth 2:![Koch depth 2](https://raw.githubusercontent.com/martybillingsley/images/master/koch3.png) 
depth3: ![Koch depth 3](https://raw.githubusercontent.com/martybillingsley/images/master/koch4.png) 

<br>
To run your program, type `python koch.py` in the terminal window at the bottom of your screen.<br>

{% spoiler "Turtle Reference" %}
You'll need these commands:
`forward (`distance in pixels`)`<br>
`right (`degrees`)`<br>
`left (`degrees`)`<br>
[Click here for more Turtle commands](https://lab.cs50.io/martybillingsley/tinkRworks/master/fractalTrees/turtleReference.pdf) <br>
{% endspoiler %}

{% spoiler "Algorithm" %}
go forward 1/3 of the size<br>
turn left 60 degrees<br>
draw a Koch line segment 1/3 of the size<br>
turn right 120 degrees<br>
draw a Koch line segment 1/3 of the size<br>
turn left 60 degrees<br>
go forward 1/3 of the size<br>
{% endspoiler %}

{% spoiler "Code" %}
`def drawLineSegment(size,depth):`<br>
 &nbsp;&nbsp; `forward(size)`<br>
 &nbsp;&nbsp; `left(60)`<br>
 &nbsp;&nbsp; `drawLineSegment(size/3,depth-1)`<br>
 &nbsp;&nbsp; `right(120)`<br>
 &nbsp;&nbsp; `drawLineSegment(size/3,depth-1)`<br>
 &nbsp;&nbsp; `left(60)`<br>
 &nbsp;&nbsp; `forward(size)`<br>
{% endspoiler %}

{% next  %}
## Put the whole triangle together
Draw three Koch line segments, turning the turtle after each one, so that they join up to make a triangle.
![Koch Snowflake](https://raw.githubusercontent.com/martybillingsley/images/master/kochFull2.png) 
