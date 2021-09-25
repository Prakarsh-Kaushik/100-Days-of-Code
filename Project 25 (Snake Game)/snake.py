from turtle import Turtle

SEGMENT_INDEX = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT  = 0


class Snake():
    def __init__(self):
        self.segment_list = []
        self.create_snake()
        self.head = self.segment_list[0]

    def create_snake(self):
        for segment in SEGMENT_INDEX:
            self.add_seg(segment)

    def add_seg(self, segment):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(segment)
        self.segment_list.append(new_segment)

    def reset(self):
        for seg in self.segment_list:
            seg.goto(1000, 1000)
        self.segment_list.clear()
        self.create_snake()
        self.head = self.segment_list[0]

    def extend(self):
        self.add_seg(self.segment_list[- 1].position())

    def move(self):
        for seg_num in range(len(self.segment_list) - 1, 0, -1):
            new_x = self.segment_list[seg_num - 1].xcor()
            new_y = self.segment_list[seg_num - 1].ycor()
            self.segment_list[seg_num].goto(new_x, new_y)
        self.head.fd(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
