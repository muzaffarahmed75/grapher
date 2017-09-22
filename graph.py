from tkinter import *
from math import log, sqrt, e


class Grid:
    def __init__(self, master, width, height, step, *typ):
        global graph
        self.width = width
        self.height = height
        self.step = step
        if typ:
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
                    graph.create_line(k, 0, k, height, fill='#999999')
            graph.pack()

    def axis(self, x, y):
        graph.create_line(x, 0, x, graph1.height, width=1.5)
        graph.create_line(0, graph1.height - x, graph1.width, graph1.height - x, width=1.5)
        graph.pack()

    def label(self, x0, xs, y0, ys, kink):
        graph.create_text(55, 55, text='random')
        graph.pack()


class Form1:
    def __init__(self, master):
        def save():
            self.dat = e1.get()
            e1.delete(0, END)
            master.quit()
        Label(master, text="Number of points").grid(row=0)
        e1 = Entry(master)
        e1.grid(row=0, column=1)
        Button(master, text='OK', command=save).grid(row=3, column=1, sticky=W, pady=4)


while 1:
    try:
        root1 = Tk()
        form1 = Form1(root1)
        root1.mainloop()
        root1.destroy()
        n = int(form1.dat)
    except:
        continue
    break


class Form2:
    def __init__(self, master):
        Label(master, text="Quantity A").grid(row=0)
        Label(master, text="Quantity B").grid(row=0, column=1)
        ela,elb = [None]*n,[None]*n
        for i in range(n):
            ela[i] = Entry(master)
            ela[i].grid(row=i+1)
        for i in range(n):
            elb[i] = Entry(master)
            elb[i].grid(row=i+1, column=1)


root2 = Tk()
form2 = Form2(root2)
root2.mainloop()


root3 = Tk()
root3.resizable(width=False, height=False)
graph1 = Grid(root3, 800, 600, 25, 2, 6)
graph1.axis(50, 50)

root3.mainloop()
