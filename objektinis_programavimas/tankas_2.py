import random


class Tank:
    def __init__(self):
        self.coordinate_x = random.randint(0, 9)
        self.coordinate_y = random.randint(0, 9)
        self.target_x = random.randint(0, 9)
        self.target_y = random.randint(0, 9)
        self.position = "^"
        self.enemy = "0"
        self.total_shoots = 0
        self.acurate_shoots = 0
        self.missed_shoots = 0

    def print_board(self):
        for x in range(10):
            for y in range(10):
                if x == self.coordinate_x and y == self.coordinate_y:
                    print(self.position, end="")
                elif x == self.target_x and y == self.target_y:
                    print(self.enemy, end="")
                else:
                    print("-", end="")
            print()

    def rotate_tank(self, new_position):
        self.position = new_position

    def choose_action(self):
        legal_inputs = ["v", "^", "<", ">", "q", "f", "m"]
        text = """chose action: 
        'v', '^', '<', '>','q', 'f', 'm' """
        value = input(text)
        if value not in legal_inputs:
            print("tokio veiksmo nera")
        return value

    def move(self):
        if self.position == "^":
            self.coordinate_x -= 1
        elif self.position == ">":
            self.coordinate_y += 1
        elif self.position == "v":
            self.coordinate_x += 1
        elif self.position == "<":
            self.coordinate_y -= 1
        else:
            print("wrong direction")

    def fire(self):
        if (
            self.position == ">" and self.coordinate_y < self.target_y
        ) and self.coordinate_x == self.target_x:
            print("Target defeated")
            self.acurate_shoots += 1
            self.total_shoots += 1
            self.target_x = random.randint(0, 9)
            self.target_y = random.randint(0, 9)
        elif (
            self.position == "<" and self.coordinate_y > self.target_y
        ) and self.coordinate_x == self.target_x:
            print("Target defeated")
            self.acurate_shoots += 1
            self.total_shoots += 1
            self.target_x = random.randint(0, 9)
            self.target_y = random.randint(0, 9)
        elif (
            self.position == "v" and self.coordinate_x < self.target_x
        ) and self.coordinate_y == self.target_y:
            print("Target defeated")
            self.acurate_shoots += 1
            self.total_shoots += 1
            self.target_x = random.randint(0, 9)
            self.target_y = random.randint(0, 9)
        elif (
            self.position == "^" and self.coordinate_x > self.target_x
        ) and self.coordinate_y == self.target_y:
            print("Target defeated")
            self.acurate_shoots += 1
            self.total_shoots += 1
            self.target_x = random.randint(0, 9)
            self.target_y = random.randint(0, 9)
        else:
            print("You missed the target!")
            self.missed_shoots += 1
            self.total_shoots += 1

    def main(self):
        try:
            while True:
                value = self.choose_action()
                if value == "q":
                    break
                elif value in ["v", "^", "<", ">"]:
                    self.rotate_tank(value)
                elif value == "m":
                    self.move()
                elif value == "f":
                    self.fire()
                    print(
                        "Pataikyta kartu:",
                        self.acurate_shoots,
                        "prasauta kartu:",
                        self.missed_shoots,
                        "isviso suviu:",
                        self.total_shoots,
                    )
                self.print_board()
        except ValueError:
            print("neteisinga reiksme")


tank = Tank()
tank.main()
