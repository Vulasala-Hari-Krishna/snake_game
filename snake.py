from turtle import Turtle
INITIAL_POSITIONS = [(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.all_segments = []
        self.create_snake()

    def create_snake(self):
        for seg in INITIAL_POSITIONS:
            self.add_segment(seg)

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.all_segments.append(new_segment)
    def move(self):
        for i in range(len(self.all_segments)-1,0,-1):
            new_x = self.all_segments[i-1].xcor()
            new_y = self.all_segments[i-1].ycor()
            self.all_segments[i].goto(new_x,new_y)
        self.all_segments[0].forward(20)

    def extend(self):
        self.add_segment(self.all_segments[-1].position())
    def left(self):
        self.all_segments[0].left(90)
    def right(self):
        self.all_segments[0].right(90)
    def up(self):
        if self.all_segments[0].heading() != 270:
            self.all_segments[0].setheading(90)
    def down(self):
        if self.all_segments[0].heading() != 90:
            self.all_segments[0].setheading(270)



