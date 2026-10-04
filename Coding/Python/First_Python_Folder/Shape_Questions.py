import inquirer as iq

class Shape:
    def __init__(self, parameter):
        self.parameter = parameter
        self.shape = []

    def Shape_Name(self, shape):
        self.shape.append(shape)

Square = Shape(parameter="Square")
Square.Shape_Name("Square")

Triangle = Shape(parameter="Triangle")
Triangle.Shape_Name("Triangle")

Square = Square.shape
Triangle = Triangle.shape

questions = [
    iq.List('Shape',
        message="Choose a shape",
        choices=Square + Triangle,
        carousel=True,
        ),
    iq.List("Sides",
            message="Choose the number of sides",
            choices=["3", "4", "5", "6", "7", "8"],
            carousel=True,
            ),
]
answers = iq.prompt(questions)

if answers.get("Shape") in Square and answers.get("Sides") == "4" or answers.get("Shape") in Triangle and answers.get("Sides") == "3":
    print("Congratulations! You got it right!")
else:
    print("Sorry, that answer was incorrect for the selected shape. Please try again.")