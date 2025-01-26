import turtle
import os


#screen settings 
dt = turtle.Turtle()
screen = turtle.Screen()
width, height, color = 3000, 3000, 'black'
turtle.setup()
turtle.screensize(width, height, color)


class Rules:
    axiom = ""
    constants = []
    angle = 0
    mov_value = 0
    rules = {}
    actions = {}
    def compute(self, n):
        result = ""
        for k in range(0, n):
            result = ""
            for i in range(0, len(self.axiom)):
                if self.axiom[i] not in self.constants:
                    result += self.rules[self.axiom[i]]
                else:
                    result += self.axiom[i]
                
            self.axiom = result
        return result
    
    def l_draw(self, x):
        for i in self.actions[x]: 
            if i == "FORW":
                dt.forward(self.mov_value)
            elif i == "ROTL":
                dt.left(self.angle)
            elif i == "ROTR":
                dt.right(self.angle)


class Sierpinski(Rules):
    axiom = "A"
    constants = ["+", "-"]
    angle = 60
    mov_value = 2
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
    
    
class DragonCurve(Rules):
    axiom = "F"
    constants = ["+", "-"]
    angle = 90
    mov_value = 6
    rules = {
        "F": "F+G",
        "G": "F-G"
    }
    actions = {
        "F":["FORW"],
        "G":["FORW"],
        "+":["ROTL"],
        "-":["ROTR"],
    }


class KochCurve(Rules):
    axiom = "F"
    constants = ["+", "-"]
    angle = 90
    mov_value = 6
    rules = {
        "F":"F+F-F-F+F"
    }
    actions = {
        "F":["FORW"],
        "+":["ROTL"],
        "-":["ROTR"],
    }

class HilbertCurve(Rules):
    axiom = "A"
    constants = ["F", "+", "-"]
    mov_value = 6
    angle = 90
    rules = {
        "A": "+BF-AFA-FB+",
        "B": "-AF+BFB+FA-"
    }
    actions = {
        "F":["FORW"],
        "+":["ROTL"],
        "-":["ROTR"],
        "A":[],
        "B":[],
    }

class KochSnowflake(Rules):
    axiom = "F--F--F"
    constants = ["+", "-"]
    mov_value = 6
    angle = 60
    rules = {
        "F":"F+F--F+F"
    }
    actions = {
        "F":["FORW"],
        "+":["ROTR"],
        "-":["ROTL"],
    }

def generate_menu():
    screen.clear()
    dt.clear()
    dt.hideturtle()
    dt.speed(0)
    screen.tracer(17)
    turtle.Screen().bgcolor("black")
    os.system('cls')
    dt.color("white") 
    for i in range(0, 10):
        print("*", end="")
    print(" MENU ", end="")
    for i in range(0, 10):
        print("*", end="")
    print()
    print("*      LFractals         *")
    print("*      - Demr            *")
    for i in range(0, 26):
        print("*", end='')
    print()
    print("Fractals are more than just a mathematical curiosity,\n"
          "or a computer hobbyist's plaything:\nthey shape us and the world we live in.\n- Bill Hirst")
    print()
    print("Choose a value to insert")
    for i in range(0, 25):
        print("-", end="")
    print()
    print("1. Sierpinski")
    print("2. Dragon Curve")
    print("3. Koch Curve")
    print("4. Hilbert Curve")
    print("5. Koch snowflake")
    print("0. Exit program")
    for i in range(0, 25):
        print("-", end="")
    print()
    

def main():
    running = True
    intervals = []
    while running:    
        generate_menu()
        size = 0
        try:
            option = int(input("Choose the number of the curve: "))
            assert option >= 0 and option <= 5
        except AssertionError:
            print("ERROR: Inserted value is out of bounds.")
            option = 0
        except ValueError:
            print("ERROR: Inserted value is not an integer.")
            option = 0
        if option != 0:
            print("Insert shape size: ")

        try:
            match option:
                case 1:
                    shape = Sierpinski()
                    size = int(input())
                    assert size <= 8 and size >= 1
                case 2:
                    shape = DragonCurve()
                    size = int(input())
                    assert size <= 13 and size >= 1
                case 3:
                    shape = KochCurve()
                    size = int(input())
                    assert size <= 4 and size >= 1
                case 4:
                    shape = HilbertCurve()
                    size = int(input())
                    assert size <= 7 and size >= 1
                case 5:
                    shape = KochSnowflake()
                    size = int(input())
                    assert size <= 4 and size >= 1 
                case 0:
                    return 1
                
        except AssertionError:
            print("ERROR: Inserted value is out of bounds.")
            size = 0
        except ValueError:
            print("ERROR: Inserted value is not an integer.")
            
        drawing = shape.compute(size)
        for i in drawing:
            shape.l_draw(i)
        print()
        print("Press enter key to continue . . .", end="")
        input()
        dt.reset()
    return 1


if __name__ == "__main__":
    main()
