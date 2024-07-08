import turtle
import os


#screen settings 
dt = turtle.Turtle()
screen = turtle.Screen()
width, height, color = 2000, 2000, 'black'
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
    
    
class Honeycomb(Rules):
    axiom = "A"
    constants = []
    angle = 60
    mov_value = 10
    rules = {
        "A": "AB",
        "B": "A",
    }
    actions = {
        "A":["ROTR","FORW"],
        "B":["ROTL","FORW"],
    }
    
    
def generate_menu():
    screen.clear()
    dt.clear()
    dt.hideturtle()
    dt.speed(0)
    screen.tracer(19)
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
    print("Choose a value to insert")
    for i in range(0, 20):
        print("-", end="")
    print()
    print("1. Honeycomb")
    print("2. Sierpinski")
    print("0. Exit program")
    for i in range(0, 20):
        print("-", end="")
    print()
    

def main():
    running = True
    while running:    
        generate_menu()
        size = 0
        try:
            option = int(input("Insert which to visualize: "))
            assert option >= 0 and option <= 2
            print("Insert shape size: ")
        except AssertionError:
            print("ERROR: Inserted value is out of bounds")
            option = 0
        
        try:
            match option:
                case 1:
                    shape = Honeycomb()
                    size = int(input())
                    assert size <= 20 and size >= 1
                case 2:
                    shape = Sierpinski()
                    size = int(input())
                    assert size <= 10 and size >= 1
                    
                case 0:
                    return 1
                
        except AssertionError:
            print("ERROR: Inserted value is out of bounds")
            size = 0
            
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
