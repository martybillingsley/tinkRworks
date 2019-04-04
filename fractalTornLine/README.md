# Cesaro Torn Line Fractals
A torn line fractal is a spacefilling curve that looks like a square has lots of little tears in it . Like the Koch snowflake, if the drawing is continuted to infinity you end up with a shape that has an infinitely long perimeter contained in a finite area. Because we can't draw to infinity, it's easiest to specify the depth to which the fractal should be drawn.

## Try drawing one torn line segment
Write a function to draw one line segment.  As with the fractal trees, it's easiest to use a depth argument to control the complexity of the curve:

depth 0: ![Cesaro Torn Line Segment depth 0](https://raw.githubusercontent.com/martybillingsley/images/master/tornLine1.png) <br>
depth 1: ![Cesaro Tornn Line Segment depth 1](https://raw.githubusercontent.com/martybillingsley/images/master/tornLine2.png) <br>
depth 2:![Cesaro Tornn Line Segment depth 2](https://raw.githubusercontent.com/martybillingsley/images/master/tornLine3.png) <br>
depth3: ![Cesaro Tornn Line Segment depth 3](https://raw.githubusercontent.com/martybillingsley/images/master/tornLine4.png) <br>
depth4: ![Cesaro Tornn Line Segment depth 4](https://raw.githubusercontent.com/martybillingsley/images/master/tornLine5.png) <br>

<br>
To run your program, type `python tornLine.py` in the terminal window at the bottom of your screen.<br>

{% spoiler "Turtle Reference" %}
You'll need these commands:
`forward (`distance in pixels`)`<br>
`right (`degrees`)`<br>
`left (`degrees`)`<br>
[Click here for more Turtle commands](https://lab.cs50.io/martybillingsley/tinkRworks/master/fractalTrees/turtleReference.pdf) <br>
{% endspoiler %}

{% spoiler "Algorithm" %}
<br>
if the depth is 0, draw a straight line (this is to stop the recursion)<br>
otherwise:<br>
draw a torn line segment 1/2 of the size<br>
turn left almost 90 degrees (say 85)<br>
draw a torn line segment 1/2 of the size<br>
turn left almost 180 degrees (say 170)<br>
draw a torn line segment 1/2 of the size<br>
turn right almost 90 degrees (say 85)<br>
draw a torn line segment 1/2 of the size<br>
*note:* the degrees must match up; if the turtle turns 80 degrees instead of 85, then turn around 160 degrees instead of 170.
{% endspoiler %}

{% spoiler "Code" %}
`def drawTornLineSegment(size,depth):`<br>
 &nbsp;&nbsp; `if depth <= 0:`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `forward(size)`<br>
 &nbsp;&nbsp; `else:`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `forward(size/3)`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `left(60)`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `drawLineSegment(size/3,depth-1)`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `right(120)`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `drawLineSegment(size/3,depth-1)`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `left(60)`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `forward(size/3)`<br>
{% endspoiler %}

{% next  %}
## Put a whole square together
Draw three Koch line segments, turning the turtle after each one, so that they join up to make a square.<br>
![Torn Square](https://raw.githubusercontent.com/martybillingsley/images/master/tornLineFull2.png) 
