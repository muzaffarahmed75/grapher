from tkinter import *
from math import log, sqrt, e


class Grid:
    def __init__(self, master, width, height, step, *typ):
        global graph
        self.width = width
        self.height = height
        self.step = step
        self.typ = typ[0]
        # the variable typ refers to the type of graph, i.e. 0 for regular,
        # 1 for semi-log along x, 2 for semi-log along y, 3 for log-log
        graph = Canvas(master, width=width, height=height, bg='white')

        if not typ or typ[0] == 0:
            for i in range(0, width, step):
                graph.create_line(i, 0, i, height, fill='#999999')

            for i in range(0, height, step):
                graph.create_line(0, i, width, i, fill='#999999')

            graph.create_text(55, 55, text='random label')

        elif typ[0] == 1:
            for i in range(0, height, step):
                graph.create_line(0, i, width, i, fill='#999999')

            divs = typ[1]
            for i in range(0, width, width/divs):
                for j in range(1, 10):
                    k = i + width*(log(j, 10))/divs
                    graph.create_line(k, 0, k, height, fill='#999999')

        elif typ[0] == 2:
            for i in range(0, width, step):
                graph.create_line(i, 0, i, height, fill='#999999')

            divs = typ[1]
            for i in range(0, height, height/divs):
                for j in range(1, 10):
                    k = height - i - height*(log(j, 10))/divs
                    graph.create_line(0, k, width, k, fill='#999999')

        elif typ[0] == 3:
            for i in range(0, height, height/step):
                for j in range(1, 10):
                    k = height - i - height*(log(j, 10))/step
                    graph.create_line(0, k, width, k, fill='#999999')

            divs = typ[1]
            for i in range(0, width, width/divs):
                for j in range(1, 10):
                    k = i + width*(log(j, 10))/divs
                    graph.create_line(k, 0, k, height, fill='#999999'

        graph.pack()

    def label(self, x0, x1, y0, y1, kink):
        graph.create_text(55, 55, text='random')
        graph.pack()


root = Tk()
root.resizable(width=False, height=False)
graph1 = Grid(root, 800, 600, 25, 2, 5)
root.mainloop()
