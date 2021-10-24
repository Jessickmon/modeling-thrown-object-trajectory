import turtle
import math


class Projectile:
    def __init__(self, y_o, v_o, theta):
        self.height = y_o
        self.init_velocity = v_o
        self.angle = theta * (math.pi / 180)  # convert angle from degrees to radians

    def next_y_point(self, time):
        acc = -9.81

        # use trig to solve for initial y-velocity
        initial_y_vel = math.sin(self.angle) * self.init_velocity

        # use displacement kinematic equation to solve for y-displacement
        y_displacement = self.height + initial_y_vel * time + (1 / 2) * acc * time ** 2
        return y_displacement

    def next_x_point(self, time):
        # use trig to solve for initial x-velocity
        initial_x_vel = math.cos(self.angle) * self.init_velocity
        x_displacement = initial_x_vel * time
        return x_displacement

    def pos_zero_of_func(self):
        # same as line 14
        initial_y_vel = math.sin(self.angle) * self.init_velocity

        # use quadratic formula to solve for the zeroes of the object thrown
        first_zero = (-initial_y_vel + math.sqrt((initial_y_vel ** 2) - (4 * -4.905 * self.height))) / (2 * -4.905)
        second_zero = (-initial_y_vel - math.sqrt((initial_y_vel ** 2) - (4 * -4.905 * self.height))) / (2 * -4.905)

        # accounts for instances where zeroes may be negative because negative time is not possible
        if first_zero <= 0:
            return second_zero
        return first_zero

    def time_of_max(self):
        # same as line 14
        initial_y_vel = math.sin(self.angle) * self.init_velocity

        # use acc = vel/time to solve for t at maximum
        time_of_maximum = (0 - initial_y_vel) / -9.81
        return time_of_maximum

    def draw_projectile(self, turt):
        # divides the zero into 100 equal iterations
        iterated_zero = self.pos_zero_of_func() / 100

        # make x-values (which represent time)
        times = [x * iterated_zero for x in range(0, 101)]

        # plug in x-values from list of times into function to plot position of object thrown
        for index in times:
            turt.penup()
            turt.goto(self.next_x_point(index), self.next_y_point(index))
            turt.stamp()


# assume that we are kept within quadrant I by having positive inputs 
object_thrown = Projectile(2, 10, 45)  # y_o, v_o, theta: in that order

# makes the graph proportional to the length of the arc to keep it within view
zero_of_func = object_thrown.pos_zero_of_func()
time_of_max_height = object_thrown.time_of_max()
urx_of_window = object_thrown.next_x_point(zero_of_func)
ury_of_window = object_thrown.next_y_point(time_of_max_height)

jess = turtle.Turtle()
jess.shape("circle")
window = turtle.Screen()

window.setworldcoordinates(0, 0, urx_of_window * 1.1, ury_of_window * 1.1)

object_thrown.draw_projectile(jess)

window.exitonclick()
