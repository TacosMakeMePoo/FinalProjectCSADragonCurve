from manim import *
import numpy as np

class LineExample(Scene):
    def construct(self):

        #All the lines in a group
        lines = VGroup()
        num_iterations = 15
        first_line = Line(start=[-1, 0, 0], end=[1, 0, 0])
        lines.add(first_line)

        for i in range(1 , num_iterations):

            #Declare a new VGroup, set it equal to the previous line
            temp = VGroup()
            temp = lines

            for line in temp:
                line.rotate(PI / 2)

            #Attach to end of temp

            temp.shift(lines[len(lines) - 1].get_end())

            self.play(Create(temp))

            for line in temp:
                lines.add(line)

            #Animate VGroup shifting 90 degrees from the end point


            #First VGroup eats temporary VGroup

