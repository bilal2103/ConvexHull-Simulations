import tkinter as tk
import math as mp
from tkinter import messagebox
import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - \
          (q.x - p.x) * (r.y - q.y)

    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def distance(p, q):
    return mp.sqrt((p.x - q.x) ** 2 + (p.y - q.y) ** 2)
def left_most() -> int:
    minn = 0
    for i in range(1, len(points)):
        if points[i].x < points[minn].x:
            minn = i
        elif points[i].x == points[minn].x:
            if points[i].y > points[minn].y:
                minn = i
    return minn
def Generate_Points():
    while len(points) < 10:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        point = Point(x, y)
        is_unique = all((point.x != p.x or point.y != p.y) for p in points)
        if is_unique:
            points.append(point)
def Add_Line(p1, p2, c, color):
    return c.create_line(p1.x, p1.y, p2.x, p2.y, fill=color)

class MainMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.DisplayMenu()
    def DisplayJarvis(self):
        self.root.destroy()
        obj.JarvisMarch()
    def DisplayMenu(self):
        self.root.geometry("900x900")
        self.root.title("Main Menu")
        jarvis_btn = tk.Button(self.root,text="Simulate Jarvis March", font=('Comic Sans',18),command=self.DisplayJarvis)
        jarvis_btn.pack()
        self.root.mainloop()

class ConvexHull:
    Hull = []
    Points = []
    updated_points = {}

    def __init__(self, p):
        self.Points = p
        self.circle_radius = 10
        self.start = Point(300,500)
        self.screenheight = 700
        self.screenwidth = 700
    def display_Hull(self):
        print('Displaying points that are part of the hull')
        for point in self.Hull:
            print(str(point.x) + ',' + str(point.y))

    def JarvisMarch(self):
        def proceed():
            result_var.set(False)
        def CloseWindow():
            root.destroy()
            MainMenu()
        root = tk.Tk()
        root.geometry(f"{self.screenheight}x{self.screenwidth}")
        root.protocol("WM_DELETE_WINDOW", CloseWindow)
        result_var = tk.BooleanVar()
        root.configure(bg="Black")
        root.title('Jarvis March')
        c = tk.Canvas(root, bg="black", height=700, width=700)
        title_label = tk.Label(c,text="Simulation for Jarvis March Algorithm",font=('Comic Sans',15), bg="black", fg="white")
        c.create_window(350,20,window=title_label,anchor="center")
        origin_index = left_most()
        origin = self.Points[origin_index]
        print(origin)
        for point in self.Points:
            temp = Point(point.x, point.y)
            temp.x = abs(origin.x - temp.x) * 30 + self.start.x
            temp.y = self.start.y - abs(origin.x + temp.y) * 30
            self.updated_points[point] = temp
            c.create_oval(temp.x, temp.y, temp.x + self.circle_radius, temp.y + self.circle_radius, fill="red")
            coordinates = tk.Label(c, text=f"{point.x},{point.y}", font=('Comic Sans', 5), bg="black", fg="white")
            label_window = c.create_window(temp.x, temp.y - 5, window=coordinates)

        # perform Jarvis March
        n = len(self.Points)
        l = origin_index
        p = l
        q = 0
        simulation_speed = 1
        while True:
            self.Hull.append(self.Points[p])
            q = (p + 1) % n
            line_id = Add_Line(self.updated_points[self.Points[p]], self.updated_points[self.Points[q]], c, "white")
            c.pack()
            for i in range(n):
                if p == i or q == i or p == i:
                    continue
                result_var.set(False)
                root.after(simulation_speed, proceed)
                root.wait_variable(result_var)
                line_id2 = Add_Line(self.updated_points[self.Points[q]], self.updated_points[self.Points[i]], c,
                                    "purple")
                c.pack()
                result_var.set(False)
                root.after(simulation_speed, proceed)
                root.wait_variable(result_var)
                o = orientation(self.Points[p], self.Points[i], self.Points[q])
                if o == 2:
                    print('Orientation is counter clockwise')
                    c.delete(line_id)
                    c.delete(line_id2)
                    q = i
                    line_id = Add_Line(self.updated_points[self.Points[p]], self.updated_points[self.Points[q]], c,
                                       "white")
                else:
                    c.delete(line_id2)
                c.pack()
            p = q
            if p == l:
                break
        c.pack()
        root.mainloop()





points = []
Generate_Points()
obj = ConvexHull(points)
Main = MainMenu()

