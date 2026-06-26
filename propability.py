import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []

        for color, number in kwargs.items():
            for _ in range(number):
                self.contents.append(color)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn_balls = self.contents.copy()
            self.contents.clear()
            return drawn_balls

        drawn_balls = []

        for _ in range(num_balls):
            index = random.randrange(len(self.contents))
            drawn_balls.append(self.contents.pop(index))

        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):
        # Copy the hat so original contents are not changed
        new_hat = Hat()

        new_hat.contents = hat.contents.copy()

        drawn_balls = new_hat.draw(num_balls_drawn)

        drawn_count = {}

        for ball in drawn_balls:
            if ball in drawn_count:
                drawn_count[ball] += 1
            else:
                drawn_count[ball] = 1

        success = True

        for color, number in expected_balls.items():
            if drawn_count.get(color, 0) < number:
                success = False
                break

        if success:
            successful_experiments += 1

    return successful_experiments / num_experiments