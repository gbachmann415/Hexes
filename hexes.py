"""
Gunnar Bachmann
8/27/2019
Hexes.py
Homework 1
Program that draws the figure (The overlapped series of hexagons) from instructions.
"""
import turtle as t

def hexagon():
    """
    Draws a single hexagon from the initial starting position (east, pendown, at origin)
    :return:
    """
    t.forward(30)
    t.left(60)
    t.forward(30)
    t.left(60)
    t.forward(30)
    t.left(60)
    t.forward(30)
    t.left(60)
    t.forward(30)
    t.left(60)
    t.forward(30)
    t.left(60)

def single_shape():
    """
    Uses the predefined hexagon function to draw a figure from a bunch of hexagons.
    :return:
    """
    hexagon()
    t.forward(30)
    t.right(60)
    hexagon()
    t.forward(30)
    t.right(60)
    hexagon()
    t.forward(30)
    t.right(60)
    hexagon()
    t.forward(30)
    t.right(60)
    hexagon()
    t.forward(30)
    t.right(60)
    hexagon()
    t.forward(30)
    t.right(60)

def final_shape():
    """
    Using the single_shape function to draw the final figure and return to the initial starting position.
    (east, pendown, origin)
    :return:
    """
    single_shape()
    t.forward(30)
    single_shape()
    t.back(30)

if __name__ == '__main__':
    final_shape()
    t.done()

