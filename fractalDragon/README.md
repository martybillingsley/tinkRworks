# Dragon Curve
A dragon curve is another example of a *self-similar*, or *fractal*, curve. This one is a space-filling curve that never crosses over itself. (It might appear to, but that's only when the line runs into itself at a 90&deg; corner.)
![Dragon Curve](https://raw.githubusercontent.com/martybillingsley/images/master/dragon15iterations.png) 

Dragon curve explained (sort of):
{% video https://www.youtube.com/watch?v=wCyC-K_PnRY %}

## Algorithm
We can draw this curve using only iteration - no need for recursion - by first coming up with a rule that defines the path that the curve follows. The rule is made up of 'R's and 'L's, each of which determine whether the curve bends to the right or left at as it is drawn. As before, the user determines the depth, or complexity, of the curve by specifying the number of iterations the rule undergoes.

The rule is built as follows:
for each iteration, take the result of the previous iteration and make a copy of it
take the copy, reverse it and replace each 'R' with an 'L' and each 'L' with an 'R'
join the two copies, with an 'R' in between

Eample: the next iteration after R R L R R L L
Step 1: Make a copy of the rule, so there are two copies. 
orig: R R L R R L L
copy: R R L R R L L
Step 2: Reverse the copy
copy: L L R R L R R
Step 3: In the copy, replace 'R' with 'L' and 'L' with 'R'
copy: R R L L R L L
Step 4: join the original and the copy together with an 'R' inbetween
nextIteration: R R L R R L L R R R L L R L L

To draw this curve, take the final iteration of the rule and move the turtle as follows
for each letter in the rule: move forward and if the letter is 'R', turn right 90&deg;, and if the letter is 'L', turn left 90&deg;.

Write a function to generate the rule. It should have arguments for the number of iterations and the starting rule. It should return the ending rule.
Example 1: makeRule(1, 'RRLRRLL') should return RRLRRLLRRRLLRLL (this is the example shown above).
Example 2: makeRule(4, 'R') should return RRLRRLLRRRLLRLLRRRLRRLLLRRLLRLL

Next, write a function that takes a rule and a size as arguments, and has the turtle draw the shape defined by the rule, moving forward the number of steps dictated by the size argument.
The curve that results from example 1 looks like this:
![Dragon Curve](https://raw.githubusercontent.com/martybillingsley/images/master/dragon4Iterations.png) 
The the curve that results from example 2 is more interesting:
![Dragon Curve 4 iterations](https://raw.githubusercontent.com/martybillingsley/images/master/dragon4iterations.png) 
The curve at the top of the page is 15 iterations, with a starting rule of 'R'
