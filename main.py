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
        self.obj = ConvexHull(points)
        self.DisplayMenu()
    def DisplayJarvis(self):
        self.root.destroy()
        self.obj.JarvisMarch()
    def DisplayGraham(self):
        self.root.destroy()
        self.obj.GrahamScan()
    def DisplayBruteForce(self):
        self.root.destroy()
        self.obj.BruteForce()
    def CloseWindow(self):
        self.root.destroy()
        self.obj.root.destroy()
    def DisplayMenu(self):
        self.root.geometry("900x900")
        self.root.title("Main Menu")
        self.root.protocol("WM_DELETE_WINDOW",self.CloseWindow)
        self.root.configure(bg="Black")
        title_lbl = tk.Label(self.root,text = "Simulations for algorithms to obtain Convex Hull", font=('Comic Sans',25))

        lbl1 = tk.Label(self.root,text="Click any of the following buttons:", font=('Comic Sans',20))

        title_lbl.config(bg="Black", fg="White")
        lbl1.configure(bg="Black",fg="White",anchor='w', justify="left")
        jarvis_btn = tk.Button(self.root,text="Simulate Jarvis March", font=('Comic Sans',18),command=self.DisplayJarvis)

        graham_btn = tk.Button(self.root, text="Simulate Graham Scan", font=('Comic Sans', 18),command=self.DisplayGraham)

        bruteforce_btn = tk.Button(self.root, text="Simulate Brute Force approach", font=('Comic Sans', 18),command=self.DisplayBruteForce)

        title_lbl.pack()
        lbl1.pack(padx=20,pady=70,anchor="w")
        jarvis_btn.pack(padx=20,pady=10,anchor="w")
        graham_btn.pack(padx=20,pady=10,anchor="w")
        bruteforce_btn.pack(padx=20,pady=10,anchor="w")
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
        self.root = tk.Tk()
        self.root.withdraw()
    def display_Hull(self):
        print('Displaying points that are part of the hull')
        for point in self.Hull:
            print(str(point.x) + ',' + str(point.y))
    def CloseWindow(self):
        self.root.destroy()
        MainMenu()
    def JarvisMarch(self):
        def proceed():
            result_var.set(False)

        self.root.deiconify()
        self.root.geometry(f"{self.screenheight}x{self.screenwidth}")
        self.root.protocol("WM_DELETE_WINDOW", self.CloseWindow)
        result_var = tk.BooleanVar()
        self.root.configure(bg="Black")
        self.root.title('Jarvis March')
        c = tk.Canvas(self.root, bg="black", height=700, width=700)
        title_label = tk.Label(c,text="Simulation for Jarvis March Algorithm",font=('Comic Sans',15), bg="black", fg="white")
        c.create_window(350,20,window=title_label,anchor="center")
        origin_index = left_most()
        origin = self.Points[origin_index]
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
        simulation_speed = 500
        while True:
            self.Hull.append(self.Points[p])
            q = (p + 1) % n
            line_id = Add_Line(self.updated_points[self.Points[p]], self.updated_points[self.Points[q]], c, "white")
            c.pack()
            for i in range(n):
                if p == i or q == i or p == i:
                    continue
                result_var.set(False)
                self.root.after(simulation_speed, proceed)
                self.root.wait_variable(result_var)
                line_id2 = Add_Line(self.updated_points[self.Points[q]], self.updated_points[self.Points[i]], c,
                                    "purple")
                c.pack()
                result_var.set(False)
                self.root.after(simulation_speed, proceed)
                self.root.wait_variable(result_var)
                o = orientation(self.Points[p], self.Points[i], self.Points[q])
                if o == 2:
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
        self.root.mainloop()
    '''
    write your code in the function below aimon, btw deiconify is used to open the screen again which was initially put to sleep
    in the constructor using root.withdraw()...
    '''
    def GrahamScan(self):
        self.root.deiconify()
        self.root.geometry(f"{self.screenwidth}x{self.screenheight}")
        self.root.title("Graham Scan")
        c = tk.Canvas(self.root,width=700,height=700,bg="Black")
        title_label = tk.Label(c, text="Simulation for Graham Scan Algorithm", font=('Comic Sans', 15), bg="black",fg="white")
        c.create_window(350, 20, window=title_label, anchor="center")
        self.root.protocol("WM_DELETE_WINDOW",self.CloseWindow)
        c.pack()
        self.root.mainloop()
    def BruteForce(self):
        self.root.deiconify()
        self.root.geometry(f"{self.screenwidth}x{self.screenheight}")
        self.root.title("Brute Force")
        c = tk.Canvas(self.root, width=700, height=700, bg="Black")
        title_label = tk.Label(c, text="Simulation for Brute force approach", font=('Comic Sans', 15), bg="black",
                               fg="white")
        c.create_window(350, 20, window=title_label, anchor="center")
        self.root.protocol("WM_DELETE_WINDOW", self.CloseWindow)
        origin = self.Points[left_most()]
        for point in self.Points:
            temp = Point(point.x, point.y)
            temp.x = abs(origin.x - temp.x) * 30 + self.start.x
            temp.y = self.start.y - abs(origin.x + temp.y) * 30
            self.updated_points[point] = temp
            c.create_oval(temp.x, temp.y, temp.x + self.circle_radius, temp.y + self.circle_radius, fill="red")
            coordinates = tk.Label(c, text=f"{point.x},{point.y}", font=('Comic Sans', 5), bg="black", fg="white")
            label_window = c.create_window(temp.x, temp.y - 5, window=coordinates)
        n = len(self.Points)
        c.pack()
        self.root.mainloop()




points = []
Generate_Points()
Main = MainMenu()

