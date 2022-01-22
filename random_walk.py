from random import choice

class RandomWalk:
    def __init__(self,number_points=5000):
        self.number_points = number_points
        #walk starts in position [0,0]
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.number_points:
            x_direction = choice([-1,1])
            x_distance = choice([1,2,3,4,5])
            x_step = x_direction * x_distance

            y_direction = choice([-1,1])
            y_distance = choice([1,2,3,4,5])
            y_step = y_direction * y_distance

            #Reject moves, that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
