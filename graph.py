from __future__ import division
from tkinter import *
from math import log, sqrt, e


# This class will be used for inputting number of points to be plotted.
class Form1:
    def __init__(self, master):
        def save():
            self.dat = e1.get()
            e1.delete(0, END)
            master.quit()
        Label(master, text="Number of points").grid(row=0)
        e1 = Entry(master)
        e1.grid(row=0, column=1)
        Button(master, text='OK', command=save).grid(row=3, columnspan=2, pady=4)

while 1:
    try:
        root1 = Tk()
        root1.resizable(width=False, height=False)
        form1 = Form1(root1)
        root1.mainloop()
        root1.destroy()
        n = int(form1.dat)
    except:
        continue
    break

# This class will be used for inputting the points.
tylist = ["Normal", "Semi-log(X)", "Semi-log(Y)", "Log-log"]


class Form2:
    def __init__(self, master):
        def save():
            self.data1 = [float(j.get()) for j in ela]
            self.data2 = [float(j.get()) for j in elb]
            self.orn = tuple([600, 800][::2*orn.get()-1])
            self.ty = tylist.index(ty.get())
            master.quit()

        Label(master, text="Quantity A").grid(row=0)
        Label(master, text="Quantity B").grid(row=0, column=1)
        ela, elb = [None]*n, [None]*n
        for i in range(n):
            ela[i] = Entry(master, borderwidth=1)
            ela[i].grid(row=i+1)
        for i in range(n):
            elb[i] = Entry(master, borderwidth=1)
            elb[i].grid(row=i+1, column=1)
        Button(master, text='Continue', command=save).grid(row=n+2, columnspan=2, pady=4)

        Label(master, text="Type of graph:").grid(row=n+3, sticky='E')
        ty = StringVar()
        ty.set(tylist[0])
        w = OptionMenu(master, ty, *tylist)
        w.grid(row=n+3, column=1, sticky='W')

        orn = IntVar()
        orn.set(0)
        Label(master, text="Orientation:").grid(row=n+4, sticky='W')
        Radiobutton(master, text="Horizontal", value=0, variable=orn).grid(row=n+4, columnspan=2)
        Radiobutton(master, text="Vertical", value=1, variable=orn).grid(row=n+4, columnspan=2, sticky='E')


class Anl:
    def __init__(self, lx, ly, st, typ, *ornt):
        als = [a*10**b for a in [1.0, 2.0, 2.5, 4.0, 5.0] for b in range(-15, 15)]
        als.sort()
        print lx
        print ly
        print ornt
        org = [-min(lx)*ornt[0]/(max(lx)-min(lx)), -min(ly)*ornt[0]/(max(ly)-min(ly))]
        for i, v in enumerate(org):
            org[i] = st*int(round(v/st))
            if v < 2*st: org[i] = 2*st
            if v > ornt[0]-2*st: org[i] = ornt[0]-2*st
        self.org = tuple(org)
        ranx = 1.2*(max(xl)-min(xl))
        rany = 1.2*(max(yl)-min(yl))
        for i in als:
            if i > rany*st/ornt[1]:
                scy = i
                self.scy = scy
                break
        for i in als:
            if i > ranx*st/ornt[0]:
                scx = i
                self.scx = scx
                break
        self.xmin = -org[0]*scx/st
        self.xmax = (ornt[0] - org[0])*scx/st
        self.ymin = -org[1]*scy/st
        self.ymax = (ornt[1] - org[1])*scx/st

        xm = sum(xl)/n
        ym = sum(yl)/n
        try:
            m = sum([(xl[i]-xm)*yl[i] for i in range(n)]) / sum([(xl[i]-xm)**2 for i in range(n)])
        except ZeroDivisionError:
            m = 10**15
        self.m = m
        self.c = ym - m*xm


class Grid:
    def __init__(self, master, width, height, step, *typ):
        global graph
        self.width = width
        self.height = height
        self.step = step
        if typ:
            self.typ = typ[0]
        # The variable typ refers to the type of graph, i.e. 0 for regular,
        # 1 for semi-log along x, 2 for semi-log along y, 3 for log-log
        graph = Canvas(master, width=width, height=height, bg='white')

        if not typ or typ[0] == 0:
            for i in range(0, width, step):
                graph.create_line(i, 0, i, height, fill='#999999')

            for i in range(0, height, step):
                graph.create_line(0, i, width, i, fill='#999999')

        elif typ[0] == 1:
            for i in range(0, height, step):
                graph.create_line(0, i, width, i, fill='#999999')

            divs = typ[1]
            for i in range(0, width, width//divs):
                for j in range(1, 10):
                    k = i + width*(log(j, 10))/divs
                    graph.create_line(k, 0, k, height, fill='#999999')

        elif typ[0] == 2:
            for i in range(0, width, step):
                graph.create_line(i, 0, i, height, fill='#999999')

            divs = typ[1]
            for i in range(0, height, height//divs):
                for j in range(1, 10):
                    k = height - i - height*(log(j, 10))/divs
                    graph.create_line(0, k, width, k, fill='#999999')

        elif typ[0] == 3:
            for i in range(0, height, height//step):
                for j in range(1, 10):
                    k = height - i - height*(log(j, 10))/step
                    graph.create_line(0, k, width, k, fill='#999999')

            divs = typ[1]
            for i in range(0, width, width//divs):
                for j in range(1, 10):
                    k = i + width*(log(j, 10))/divs
                    graph.create_line(k, 0, k, height, fill='#999999')
            graph.pack()

    def axis(self, x, y):
        graph.create_line(x, 0, x, graph1.height, width=1.5)
        graph.create_line(0, graph1.height - y, graph1.width, graph1.height - y, width=1.5)
        graph.pack()

    def label(self, x0, xst, scx, y0, yst, scy, o, w, h):
        for i in range(0, ornt[0], xst):
            graph.create_text(i-10, h-(o[1]-7), text=str(x0+i*scx/xst))
        for i in range(0, ornt[1], yst):
            graph.create_text(o[0]-10, h-(i-7), text=str(y0 + i * scy / yst))
        graph.pack()

    def plot(self, xl, yl, xs, ys, st, h, o):
        for i in range(len(xl)):
            for j in (1,4):
                graph.create_oval(xl[i]*st/xs+o[0]-j, h-(yl[i]*st/ys+o[1]-j), xl[i]*st/xs+o[0]+j, h-(yl[i]*st/ys+o[1]+j))
        """graph.create_line(a.xmin*st/xs+o[0],
                          h-(a.m * a.xmin + a.c)*st/ys+o[1],
                          a.xmax*st/xs+o[0],
                          h-(a.m * a.xmax + a.c)*st/ys+o[1])"""
        graph.pack()

while 1:
    try:
        root2 = Tk()
        root2.resizable(width=False, height=False)
        form2 = Form2(root2)
        root2.mainloop()
        root2.destroy()
        xl = form2.data1
        yl = form2.data2
        typ = form2.ty
        ornt = form2.orn

        a = Anl(xl, yl, 25, typ, ornt[0], ornt[1])
        print vars(a)
        break
        # apply functions here
    except:
        continue
    break

root3 = Tk()
root3.resizable(width=False, height=False)
graph1 = Grid(root3, 800, 600, 25, 0)
graph1.axis(a.org[0], a.org[1])
graph1.label(a.xmin, 25, a.scx, a.ymin, 25, a.scy, a.org, 800, 600)
graph1.plot(xl, yl, a.scx, a.scy, 25, 600, a.org)
root3.mainloop()
