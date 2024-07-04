# LindenmayerSystems - L-Systems
This mini-project is about the implementation of different L-Systems which can generate different fractal structures such as the sierpinski triangle.
I made it with Python and the turtle library. The main resources I used for learning were: 
- The Wikipedia page of L-systems: https://en.wikipedia.org/wiki/L-system
- Turtle library: https://docs.python.org/3/library/turtle.html

An L-system is defined by:
V: the alphabet, a set of symbols that contains variables and constants
W: the axiom, it defines the initial state of the system, it's a string
P: which defines the rules and ways that we can transfrom symbols.

So we will formalize this in classes, a main class will have functions for all the generators,
as an example, values from the HoneyComb class would be:
```Python
    variables = ["A", "B"]
    axiom = "A"
    constants = []
    angle = 60
    rules = {
        "A": "AB",
        "B": "A"
    }
```
Which means that We start with A, with an angle of 60 for all the rotations and that we map like so:
- A -> AB
- B -> A
