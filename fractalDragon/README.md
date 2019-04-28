# Dragon Curve
A dragon curve is another example of a *self-similar*, or *fractal*, curve. This one is a space-filling curve that never crosses over itself; it might appear to, but that's only when the line runs into itself at a 90&deg; corner.

Dragon curve explained (sort of):
{% video https://www.youtube.com/watch?v=wCyC-K_PnRY %}

## Algorithm
We can draw this curve using only iteration - no need for recursion - by first coming up with a rule that defines the path that the curve follows. The rule is made up of 'R's and 'L's, each of which determine whether the curve bends to the right or left at as it is drawn. As before, the user determines the depth, or complexity, of the curve by specifying the number of iterations the rule undergoes.

The rule is as follows:
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

