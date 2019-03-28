# Fractals
A *fractal* is a curve or geometric figure, each part of which has the same statistical character as the whole. In other words, it looks the same at any magnification. Fractals are useful in modeling structures (such as eroded coastlines or snowflakes) in which similar patterns recur at progressively smaller scales, and in describing partly random or chaotic phenomena such as crystal growth, fluid turbulence, and galaxy formation.

Read more about fractals at [Wikipedia](https://en.wikipedia.org/wiki/Fractal) <br><br>

## Drawing Fractals Using Python
Turtles are perhaps the easiest way to draw things in Python. After you add the following line of code at the top of your program  <br>
`from turtle import * ` <br>
then you have a turtle that can move around the screen drawing lines with a pen.  

In real life, fractals are infinitely precise; you can zoom in forever. However, in drawing a fractal on the screen, there must be some point at which the program stops drawing. A Python turtle, after all, can't move forward less than one pixel or turn less than one degree.
