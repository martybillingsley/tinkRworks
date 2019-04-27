# Fractal Trees
## Start with drawing a simple tree. 
A tree is made of a trunk and branches. Write a `drawTree()` function that draws a simple tree with a trunk and two branches. The turtle must end up where it started, facing the way it was when it started.

![Simple tree](https://raw.githubusercontent.com/martybillingsley/images/master/tree1.png) 

<br>
To run your program, type `python tree.py` in the terminal window at the bottom of your screen.<br>

{% spoiler "Turtle Reference" %}
You'll need these commands:
`forward (`distance in pixels`)`<br>
`backward (`distance in pixels`)`<br>
`right (`degrees`)`<br>
`left (`degrees`)`<br>
[Click here for more Turtle commands](https://lab.cs50.io/martybillingsley/tinkRworks/master/fractalTrees/turtleReference.pdf) <br>
{% endspoiler %}

{% spoiler "Algorithm" %}
Go forward<br>
Turn right<br>
Go forward<br>
Go backward the same number of steps<br>
Turn left the same number of degrees that you turned right<br>
Turn left<br>
Go forward<br>
Go backward the same number of steps<br>
Turn right the same number of degrees that you turned left<br>
Go backward the same number of steps as the first forward<br>
{% endspoiler %}

{% spoiler "Code" %}
`def drawTree():`<br>
 &nbsp;&nbsp; `forward(100)`<br>
 &nbsp;&nbsp; `left(30)`<br>
 &nbsp;&nbsp; `forward(100)`<br>
 &nbsp;&nbsp; `backward(100)`<br>
 &nbsp;&nbsp; `right(30)`<br>
 &nbsp;&nbsp; `right(30)`<br>
 &nbsp;&nbsp; `forward(100)`<br>
 &nbsp;&nbsp; `backward(100)`<br>
  &nbsp;&nbsp;`left(30)`<br>
 &nbsp;&nbsp; `backward(100)`
{% endspoiler %}

{% next  %}

## Add an argument to the `drawTree()` function that specifies the size of the tree
Try it out with the following commands:
`drawTree(100)`
and
`drawTree(50)`

{% spoiler "Details" %}
In each `forward` and `backward` command, use the argument variable instead of a number
{% endspoiler %}

{% spoiler "Code" %}
`def drawTree(size):`<br>
 &nbsp;&nbsp; `forward(size)`<br>
 &nbsp;&nbsp; `left(30)`<br>
 &nbsp;&nbsp; `forward(size)`<br>
 &nbsp;&nbsp; `backward(size)`<br>
 &nbsp;&nbsp; `right(30)`<br>
 &nbsp;&nbsp; `right(30)`<br>
 &nbsp;&nbsp; `forward(size)`<br>
 &nbsp;&nbsp; `backward(size)`<br>
 &nbsp;&nbsp; `left(30)`<br>
 &nbsp;&nbsp; `backward(size)`
{% endspoiler %}

{% next  %}
## At the end of each branch, draw another tree 3/4 the size of the original
Try to draw a tree like this:<br>
![Tree](https://raw.githubusercontent.com/martybillingsley/images/master/tree3.png) <br>
<br>Note: think about when to stop!
{% spoiler "Recursion Explained" %}
Sometimes it is helpful to think of a recursive algorithm in terms of a diagram of function calls. This figure shows that the recursive calls are always made going to the left. The active functions are outlined in black, and the inactive function calls are in gray. The farther you go toward the bottom of the figure, the smaller the branches. The function finishes drawing one level at a time; once it is finished with the bottom left it moves to the bottom right, and so on.<br>
![Recursion Tree](https://raw.githubusercontent.com/martybillingsley/images/master/treeRecursionDiagram.png) <br>
{% endspoiler %}
<br>
{% spoiler "Algorithm" %}
Draw the trunk<br>
Turn and draw a branch<br>
Draw a tree on the end of that branch<br>
Go backward to the trunk<br>
Turn left and draw another branch<br>
Draw a tree on the end of that branch<br>
Go backward to the trunk<br>
Turn right and go backward down the trunk<br>
{% endspoiler %}
<br>
{% spoiler "Problems?" %}
Does your tree look like this?<br>
![Tree gone wrong](https://raw.githubusercontent.com/martybillingsley/images/master/tree2.png) <br>
Add another argument to the `drawTree()` function to indicate the depth of the tree.<br>
Every time you draw another tree, make it smaller **and** reduce the depth by one.
{% endspoiler %}

{% spoiler "Code" %}
`def drawTree(size, depth):`<br>
 &nbsp;&nbsp; `if depth > 0:`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `forward(size)`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `left(30)`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `forward(size)`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `drawTree(size*0.75, depth-1)`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `backward(size)`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `right(30)`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `right(30)`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `forward(size)`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `drawTree(size*0.75, depth-1)`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `backward(size)`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `left(30)`<br>
 &nbsp;&nbsp;&nbsp;&nbsp; `backward(size)`<br>
 The tree above was drawn with the command `drawTree(50,6)`
{% endspoiler %}
{% next  %}
## Add some variety to your tree (just for fun)

Trees aren't symmetric in real life. Instead of always turning a set number of degrees (30 in the example), choose a random number between 10 and 40 each time you draw a new branch.
![Random tree](https://raw.githubusercontent.com/martybillingsley/images/master/tree4.png) <br>
{% spoiler "Notes" %}
Import the random library:<br>
`from random import *`<br>
`randint(10,40)`  will give you a random integer between 10 and 40<br>
Be sure to turn right the same amount you turn left<br>
{% endspoiler %}

Make the tree even more realistic. Set the turtle shape to 'turtle' and stamp a green leaf every time you draw a tree of depth 0.
![Green tree](https://raw.githubusercontent.com/martybillingsley/images/master/tree5.png) <br>

{% spoiler "Code" %}
 `if depth > 0:`<br>
  code for drawing tree<br>
  `else:`<br>
  &nbsp;&nbsp; `color('green')`<br>
  &nbsp;&nbsp; `stamp()`<br>
  &nbsp;&nbsp; `color('black')`<br>
{% endspoiler %}

Even more realistic: make the branches brown, with the thickness depending on the depth (`depth*2` works well). Choose leaf colors at random from a list.
![Fall tree](https://raw.githubusercontent.com/martybillingsley/images/master/tree6.png) <br>

{% spoiler "Code" %}
Before drawing the trunk:<br>
`color('brown')`<br>
`pensize(depth*2)`<br>
(you'll have to do this more than once)<br><br>
Before stamping:<br>
`colors=['red', 'orange', 'yellow', 'darkred', 'gold']`<br>
`color(choice(colors))`<br>
{% endspoiler %}
