# Fractals
A *fractal* is a curve or geometric figure, a never-ending pattern that is self-similar across different scales. In other words, it looks the same at any magnification. Fractals are useful in modeling structures (such as eroded coastlines or snowflakes) in which similar patterns recur at progressively smaller scales, and in describing partly random or chaotic phenomena such as crystal growth, fluid turbulence, and galaxy formation.

The term *fractal* (from the Latin *fractus*, meaning “broken”) was coined by the mathematician Benoit Mandelbrot in 1975. In his book *The Fractal Geometry of Nature*, Mandelbrot defines a fractal as “a rough or fragmented geometric shape that can be split into parts, each of which is (at least approximately) a reduced-size copy of the whole.”

This can be demonstrated by looking at a tree (which you'll write code to draw). The tree has a branching structure, as shown in the image on the left. At the end of the trunk are two branches; at the end of each of those branches are two more branches. At the end of those branches are two more branches, and so on to infinity. If you zoom in to the end of one branch, as we do in the image on the right, you'll see that the end of a branch resembles a tree. This is what is meant by *self similarity*.

![Tree Details](https://raw.githubusercontent.com/martybillingsley/images/master/treeDetail.jpg)

 <br><br>
Fractals are more than a mathematical curiosity, but are found in nature and can be put to use:
{% video https://www.youtube.com/watch?v=WFtTdf3I6Ug %}

Read more about fractals at [Wikipedia](https://en.wikipedia.org/wiki/Fractal) <br><br>
<br>
## Drawing Fractals Using Python
Turtles are perhaps the easiest way to draw things in Python. After you add the following line of code at the top of your program  <br>
`from turtle import * ` <br>
then you have a turtle that can move around the screen drawing lines with a pen.  

In real life, fractals are infinitely precise; you can zoom in forever. However, in drawing a fractal on the screen, there must be some point at which the program stops drawing. A Python turtle, after all, can't move forward less than one pixel or turn less than one degree.

Because fractals go on to infinity, they are drawn using recursion. If you haven't used recursion in Python, warm up with this Recursion Example.

If you haven't used turtles, warm up with this Turtle Example.
<br><br>
## Fractal Challenges
[Trees](https://lab.cs50.io/martybillingsley/tinkRworks/master/fractalTrees/) <br>
[Koch Snowflake](https://lab.cs50.io/martybillingsley/tinkRworks/master/fractalKoch/) <br>
[Torn Line Fractal](https://lab.cs50.io/martybillingsley/tinkRworks/master/fractalTornLine/) <br>
Dragon Curve<br>
