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
def CheckLine(lineEndptA, lineEndptB, ptSubject):       #For brute force method, checking which side of the line do points lie on
    return (ptSubject.x - lineEndptA.x) * (lineEndptB.y - lineEndptA.y) - (ptSubject.y - lineEndptA.y) * (
                lineEndptB.x - lineEndptA.x)
def distance(p, q):
    return mp.sqrt((p.x - q.x) ** 2 + (p.y - q.y) ** 2)
def left_most() -> int:                 #function for finding leftmost point
    minn = 0
    for i in range(1, len(points)):
        if points[i].x < points[minn].x:
            minn = i
        elif points[i].x == points[minn].x:
            if points[i].y > points[minn].y:
                minn = i
    return minn                 #
def Generate_Points():                      #Function to generate random points
    while len(points) < 10:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        point = Point(x, y)
        is_unique = all((point.x != p.x or point.y != p.y) for p in points)
        if is_unique:
            points.append(point)
def Add_Line(p1, p2, c, color):
    return c.create_line(p1.x, p1.y, p2.x, p2.y, fill=color)

class MainMenu:         #for the functionalities of main screen...
    def __init__(self):
        self.root = tk.Tk()
        Generate_Points()
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
    def DisplayQuickElimination(self):
        self.root.destroy()
        self.obj.QuickElimination()
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

        quickelm_btn = tk.Button(self.root,text="Simulate Quick Elimination", font=('Comic Sans', 18),command=self.DisplayQuickElimination)
        title_lbl.pack()
        lbl1.pack(padx=20,pady=70,anchor="w")
        bruteforce_btn.pack(padx=20, pady=10, anchor="w")
        jarvis_btn.pack(padx=20,pady=10,anchor="w")
        graham_btn.pack(padx=20,pady=10,anchor="w")
        quickelm_btn.pack(padx=20, pady=10, anchor="w")
        self.root.mainloop()

class ConvexHull:
    Hull = []
    Points = []
    updated_points = {}         #Hashmap that maps points to appropriate coordinates on the screen

    def __init__(self, p):
        self.Points = p
        self.circle_radius = 10
        self.start = Point(300,500)
        self.screenheight = 700
        self.screenwidth = 700
        self.root = tk.Tk()
        self.result_var = tk.BooleanVar(self.root)
        self.simulation_speed = 100             #Change this so that program runs faster/slower.
        self.root.withdraw()
    def display_Hull(self):
        print('Displaying points that are part of the hull')
        for point in self.Hull:
            print(str(point.x) + ',' + str(point.y))
    def CloseWindow(self):
        self.root.destroy()
        MainMenu()

    def proceed(self):
        self.result_var.set(True)
    def JarvisMarch(self):
        c = self.InitializeWindow("Jarvis March", "Simulation for Jarvis March algorithm")
        # perform Jarvis March
        n = len(self.Points)
        l = left_most()
        p = l
        q = 0

        while True:
            self.Hull.append(self.Points[p])
            q = (p + 1) % n
            line_id = Add_Line(self.updated_points[self.Points[p]], self.updated_points[self.Points[q]], c, "white")
            c.pack()
            for i in range(n):
                if p == i or q == i or p == i:
                    continue
                self.result_var.set(False)                              #To pause the execution for some time
                self.root.after(self.simulation_speed, self.proceed)    #to call proceed() function after some time
                self.root.wait_variable(self.result_var)                #Waiting...
                line_id2 = Add_Line(self.updated_points[self.Points[q]], self.updated_points[self.Points[i]], c,
                                    "purple")
                c.pack()
                self.result_var.set(False)
                self.root.after(self.simulation_speed, self.proceed)
                self.root.wait_variable(self.result_var)
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

    def GrahamScan(self):
        c = self.InitializeWindow("Graham Scan","Simulation for Graham scan algorithm")
        n = len(self.Points)
        c.pack()
        self.root.mainloop()
    def InitializeWindow(self,title,text):
        self.root.deiconify()
        self.root.geometry(f"{self.screenwidth}x{self.screenheight}")
        self.root.title(title)
        c = tk.Canvas(self.root, width=self.screenwidth, height=self.screenheight, bg="Black")
        title_label = tk.Label(c, text=text, font=('Comic Sans', 15), bg="black",fg="white")
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
        c.pack()
        return c

    def BruteForce(self):
        n = len(self.Points)
        c = self.InitializeWindow("Brute Force","Simulation for brute force approach")
        #Perform brute force
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                l1 = Add_Line(self.updated_points[self.Points[i]],self.updated_points[self.Points[j]],c,"Purple")
                caninclude = True
                for k in range(n):
                    if k == j or k == i:
                        continue
                    l2 = Add_Line(self.updated_points[self.Points[j]],self.updated_points[self.Points[k]],c,"Green")
                    result = CheckLine(self.Points[i],self.Points[j],self.Points[k])
                    self.result_var.set(False)
                    self.root.after(self.simulation_speed,self.proceed)
                    self.root.wait_variable(self.result_var)
                    c.delete(l2)
                    if result < 0:
                        caninclude = False
                        break
                c.delete(l1)
                if caninclude:
                    Add_Line(self.updated_points[self.Points[i]],self.updated_points[self.Points[j]], c, "White")
                c.pack()
        self.root.mainloop()

    def QuickElimination(self):
        c = self.InitializeWindow("Quick elimination", "Simulation for Quick Elimination algorithm")
        n = len(self.Points)
        c.pack()
        self.root.mainloop()

points = []

Main = MainMenu()