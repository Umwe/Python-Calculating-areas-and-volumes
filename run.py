
print("\n")
print("Chapter 4 Test  by Kwizera Africa Hubert Bonaparte")
print("--------------------------------------------------")

class Rectangle:
    def __init__(self, vertical, horizontal, height):
        self.vertical = vertical
        self.horizontal = horizontal
        self.height = height

    def calc_area(self):
        area = self.vertical * self.horizontal
        print(f"Area: {area}")

    def calc_volume(self):
        area = self.vertical * self.horizontal
        volume = area * self.height
        print(f"Volume: {volume}")


class Rectangular(Rectangle):
    pass 


def create_instance():
    squares = [
        Rectangle(3, 4, 5),
        Rectangle(50, 60, 70),
        Rectangular(333, 444, 555)
    ]
    return squares


def play():
    squares = create_instance()

    for idx, square in enumerate(squares, start=1):
        print(f"\nCalculations for Square {idx}:")
        square.calc_area()
        square.calc_volume()


if __name__ == "__main__":
    play()
    
    print("\n")
