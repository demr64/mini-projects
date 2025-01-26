# LFractals - L-Systems
<img align="left" src="https://github.com/DennisAmiranda/minor-projects/assets/81851888/101bda43-0ec1-4e68-9b33-9de6507aca21" alt="My Image">
This mini-project is about the implementation of different L-Systems which can generate different fractal structures such as the sierpinski triangle.
I made it with Python and the turtle library. The main resources I used for learning were:
<br><br>

- The Wikipedia page of L-systems: https://en.wikipedia.org/wiki/L-system
- Turtle library: https://docs.python.org/3/library/turtle.html

An L-system is defined by:
V: the alphabet, a set of symbols that contains variables and constants
W: the axiom, it defines the initial state of the system, it's a string
P: which defines the rules and ways that we can transfrom symbols.

So we will formalize this in classes, which will contain fundamental information
about the fractal object, such as the actions that have to be taken when a symbol is fond or the axiom.
As an example, values from the SierpinskiRules class would be:

```Python
    axiom = "A"
    constants = ["+", "-"]
    angle = 60
    mov_value = 3
    rules = {
        "A": "B-A-B",
        "B": "A+B+A",
    }
    actions = {
        "A":["FORW"],
        "B":["FORW"],
        "+":["ROTL"],
        "-":["ROTR"],
    }
```
The particular curves available are:
1. Sierpinski's triangle
2. Dragon curve
3. Koch curve
4. Hilbert curve
5. Koch snowflake

# TODO
1. add stack for plant fractal generation
