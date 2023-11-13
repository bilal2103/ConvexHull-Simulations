import tkinter as tk
from functools import cmp_to_key
import External_functions as F
import random
import time
n = 20
def Generate_Points():                      #Function to generate random points
    random.seed(time.time())
    while len(points) < n:
        x = random.randint(0, 20)
        y = random.randint(0, 20)
        point = Point(x, y)
        is_unique = all((point.x != p.x or point.y != p.y) for p in points)
        if is_unique:
            points.append(point)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p0_gs=Point(0,0)

class MainMenu:         #for the functionalities of main screen...
    def __init__(self):
        self.root = tk.Tk()
        self.DisplayMenu()
    def CloseWindow(self):
        self.root.destroy()
    def OpenCHMenu(self):
        self.CloseWindow()
        CHMenu()
    def OpenLineSeg(self):
        self.CloseWindow()
        LIMenu(LinePoints)
    def DisplayMenu(self):
        self.root.geometry("900x900")
        self.root.title("Main Menu")
        self.root.protocol("WM_DELETE_WINDOW",self.CloseWindow)
        self.root.configure(bg="Black")
        title_lbl = tk.Label(self.root,text = "CS2009 - Design and Analysis of Algorithm", font=('Century Schoolbook',25))
        title_lbl.config(bg="Black", fg="White")
        title_lbl.place(x=110, y=140)
        title_lbl2 = tk.Label(self.root, text="Semester Project", font=('Century Schoolbook', 25))
        title_lbl2.config(bg="Black", fg="White")
        title_lbl2.place(x=290, y=200)
        grp1 = tk.Label(self.root, text="Bilal Hassan 21K-4669",font=('Century Schoolbook', 12))
        grp2 = tk.Label(self.root, text="Aiman Imran 21K-4525", font=('Century Schoolbook', 12))
        grp3 = tk.Label(self.root, text="Seher Imtiaz 21K-3363", font=('Century Schoolbook', 12))
        grp1.config(bg="Black", fg="White")
        grp2.config(bg="Black", fg="White")
        grp3.config(bg="Black", fg="White")
        grp1.place(x=650,y=610)
        grp2.place(x=650, y=640)
        grp3.place(x=650, y=670)
        ch_btn = tk.Button(self.root, text="Convex Hull Simulations", font=('Century Gothic', 18),command=self.OpenCHMenu)
        lineseg_btn = tk.Button(self.root, text="Intersecting Line Segments", font=('Century Gothic', 18),command=self.OpenLineSeg)
        ch_btn.place(x=275, y=350)
        lineseg_btn.place(x=260, y=450)
        self.root.mainloop()
class CHMenu:         #for the functionalities of main screen...
    def __init__(self):
        self.root = tk.Tk()
        Generate_Points()
        self.obj = ConvexHull(points)
        self.DisplayCHMenu()
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
    def DisplayChans(self):
        self.root.destroy()
        self.obj.Chans()
    def CloseWindow(self):
        self.root.destroy()
        self.obj.root.destroy()
        MainMenu()
    def DisplayCHMenu(self):
        self.root.geometry("900x900")
        self.root.title("Convex Hull")
        self.root.protocol("WM_DELETE_WINDOW",self.CloseWindow)
        self.root.configure(bg="Black")
        title_lbl = tk.Label(self.root,text = "Simulations of algorithms to obtain Convex Hull", font=('Century Gothic',25))
        title_lbl.config(bg="Black", fg="White")
        jarvis_btn = tk.Button(self.root,text="Simulate Jarvis March", font=('Century Gothic',18),command=self.DisplayJarvis)
        graham_btn = tk.Button(self.root, text="Simulate Graham Scan", font=('Century Gothic', 18),command=self.DisplayGraham)
        bruteforce_btn = tk.Button(self.root, text="Simulate Brute Force approach", font=('Century Gothic', 18),command=self.DisplayBruteForce)
        quickelm_btn = tk.Button(self.root,text="Simulate Quick Elimination", font=('Century Gothic', 18),command=self.DisplayQuickElimination)
        chans_btn = tk.Button(self.root,text="Simulate Chan's Algorithm",font=('Century Gothic', 18),command=self.DisplayChans)
        title_lbl.pack(pady=30)
        bruteforce_btn.place(x=250, y=150)
        jarvis_btn.place(x=290, y=250)
        graham_btn.place(x=285, y=350)
        quickelm_btn.place(x=265, y=450)
        chans_btn.place(x=267, y=550)
        self.root.mainloop()
# noinspection PyStatementEffect
class ConvexHull:
    Hull = []
    Points = []
    updated_points = {}         #Hashmap that maps points to appropriate coordinates on the screen
    def __init__(self, p):
        self.Points = p
        self.circle_radius = 10
        self.start = Point(200,550)
        self.screenheight = 700
        self.screenwidth = 700
        self.root = tk.Tk()
        self.result_var = tk.BooleanVar(self.root)
        self.simulation_speed = 100             #Change this so that program runs faster/slower.
        self.root.withdraw()

    def CloseWindow(self):
        self.root.destroy()
        CHMenu()
    def proceed(self):
        self.result_var.set(True)
    def JarvisMarch(self):
        c = self.InitializeWindow("Jarvis March", "Simulation for Jarvis March algorithm")
        # perform Jarvis March
        n = len(self.Points)
        l = F.left_most(self.Points)
        p = l

        while True:
            self.Hull.append(self.Points[p])
            q = (p + 1) % n
            line_id = F.Add_Line(self.updated_points[self.Points[p]], self.updated_points[self.Points[q]], c, "white")
            c.pack()
            for i in range(n):
                if p == i or q == i or p == i:
                    continue
                self.result_var.set(False)                              #To pause the execution for some time
                self.root.after(self.simulation_speed, self.proceed)    #to call proceed() function after some time
                self.root.wait_variable(self.result_var)                #Waiting...
                line_id2 = F.Add_Line(self.updated_points[self.Points[q]], self.updated_points[self.Points[i]], c,
                                    "purple")
                c.pack()
                self.result_var.set(False)
                self.root.after(self.simulation_speed, self.proceed)
                self.root.wait_variable(self.result_var)
                o = F.orientation(self.Points[p], self.Points[i], self.Points[q])
                if o == 2:
                    c.delete(line_id)
                    c.delete(line_id2)
                    q = i
                    line_id = F.Add_Line(self.updated_points[self.Points[p]], self.updated_points[self.Points[q]], c,
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
        def compare(p1, p2):
            o = F.orientation(p0_gs, p1, p2)
            if o == 0:
                if F.distance(p0_gs, p2) ** 2 >= F.distance(p0_gs, p1) ** 2:
                    return -1
                else:
                    return 1
            else:
                if o == 2:
                    return -1
                else:
                    return 1
        c = self.InitializeWindow("Graham Scan","Simulation for Graham scan algorithm")
        n = len(self.Points)
        ymin = self.Points[0].y
        min = 0
        for i in range(1, n):
            y = self.Points[i].y
            if ((y < ymin) or (ymin == y and self.Points[i].x < self.Points[min].x)):
                ymin = self.Points[i].y
                min = i
        self.Points[0], self.Points[min] = self.Points[min], self.Points[0]
        p0_gs = self.Points[0]
        self.Points = sorted(self.Points, key=cmp_to_key(compare))
        line_id = F.Add_Line(self.updated_points[self.Points[0]], self.updated_points[self.Points[1]], c, "white")
        c.pack()
        m = 1
        for i in range(1, n):
            while ((i < n - 1) and (F.orientation(p0_gs, self.Points[i], self.Points[i + 1]) == 0)):
                i += 1

            self.Points[m] = self.Points[i]
            m += 1
        S = []
        L = []
        L.append(line_id)
        S.append(self.Points[0])
        S.append(self.Points[1])
        S.append(self.Points[2])
        self.result_var.set(False)
        self.root.after(self.simulation_speed, self.proceed)
        self.root.wait_variable(self.result_var)
        line_id = F.Add_Line(self.updated_points[self.Points[1]], self.updated_points[self.Points[2]], c,"white")
        L.append(line_id)
        for i in range(3, m):
            while ((len(S) > 1) and (F.orientation(F.nextToTop(S), S[-1], self.Points[i]) != 2)):
                S.pop()
                c.delete(L[-1])
                c.pack()
                L.pop()
            S.append(self.Points[i])
            self.result_var.set(False)
            self.root.after(self.simulation_speed, self.proceed)
            self.root.wait_variable(self.result_var)
            line_id2 = F.Add_Line(self.updated_points[self.Points[i-1]], self.updated_points[self.Points[i]], c,"purple")
            c.pack()
            self.result_var.set(False)
            self.root.after(self.simulation_speed, self.proceed)
            self.root.wait_variable(self.result_var)
            line_id = F.Add_Line(self.updated_points[S[-2]], self.updated_points[S[-1]], c,"white")
            L.append(line_id)
            c.delete(line_id2)
            c.pack()
        line_id = F.Add_Line(self.updated_points[S[-1]], self.updated_points[S[0]], c, "white")
        while S:
            p = S[-1]
            print("(" + str(p.x) + ", " + str(p.y) + ")")
            S.pop()
        c.pack()
        self.root.mainloop()
    def InitializeWindow(self,title,text):
        self.root.deiconify()
        self.root.geometry(f"{self.screenwidth}x{self.screenheight}")
        self.root.title(title)
        c = tk.Canvas(self.root, width=self.screenwidth, height=self.screenheight, bg="Black")
        title_label = tk.Label(c, text=text, font=('Century Gothic', 15), bg="black",fg="white")
        c.create_window(350, 20, window=title_label, anchor="center")
        self.root.protocol("WM_DELETE_WINDOW", self.CloseWindow)
        exit_btn = tk.Button(c,text="Back",font=("Century Gothic", 12),command=self.CloseWindow)
        c.create_window(100,100,window=exit_btn)
        exit_btn.place(x=550, y=615)
        origin = self.Points[F.left_most(self.Points)]
        for point in self.Points:
            temp = Point(point.x, point.y)
            temp.x = abs(origin.x - temp.x) * 20 + self.start.x
            temp.y = self.start.y - abs(origin.x + temp.y) * 20
            self.updated_points[point] = temp
            c.create_oval(temp.x, temp.y, temp.x + self.circle_radius, temp.y + self.circle_radius, fill="red")
            coordinates = tk.Label(c, text=f"{point.x},{point.y}", font=('Helvetica', 5), bg="black", fg="white")
            label_window = c.create_window(temp.x, temp.y - 5, window=coordinates)
        c.pack()
        return c
    def graham_scan_utility(self,points):

        if len(points) <= 2 :
            return points

        def compare(p1, p2):
            # Find F.orientation
            o = F.orientation(p0, p1, p2)
            if o == 0:
                if F.distSq(p0, p2) >= F.distSq(p0, p1):
                    return -1
                else:
                    return 1
            else:
                if o == 2:
                    return -1
                else:
                    return 1
        #perform graham scan here
        n = len(points)
        ymin = points[0].y
        min = 0
        for i in range(1, n):
            y = points[i].y
            if ((y < ymin) or
                    (ymin == y and points[i].x < points[min].x)):
                ymin = points[i].y
                min = i
        points[0], points[min] = points[min], points[0]
        p0 = points[0]
        points = sorted(points, key=cmp_to_key(compare))
        m = 1
        for i in range(1, n):

            # Keep removing i while angle of i and i+1 is same
            # with respect to p0
            while ((i < n - 1) and
                   (F.orientation(p0, points[i], points[i + 1]) == 0)):
                i += 1

            points[m] = points[i]
            m += 1  # Update size of modified array
        S = []
        S.append(points[0])
        S.append(points[1])
        S.append(points[2])
        for i in range(3, m):
            while ((len(S) > 1) and
                   (F.orientation(S[-2], S[-1], points[i]) != 2)):
                S.pop()
            S.append(points[i])
        return S
    def Chans(self):
        c = self.InitializeWindow("Chans Algorithm", "Simulation for Chan's Algorithm")
        marked = {}
        Merged_Hull = []
        for t in range(n):
            found=False
            Merged_Hull = []
            for m in range(2, (1 << (1 << t))):
                if m in marked:
                    continue
                Merged_Hull = self.Chans_utility(m,c)
                if len(Merged_Hull) > 0:
                    print("Solution found for m = ", m)
                    found = True
                    break
                marked[m] = found
            if found:
                break
        for i in range(1,len(Merged_Hull)):
            self.result_var.set(False)
            self.root.after(self.simulation_speed, self.proceed)
            self.root.wait_variable(self.result_var)
            F.Add_Line(self.updated_points[Merged_Hull[i]],self.updated_points[Merged_Hull[i-1]],c,"white")
        F.Add_Line(self.updated_points[Merged_Hull[0]], self.updated_points[Merged_Hull[-1]], c, "white")
        c.pack()
        self.root.mainloop()
    def Chans_utility(self,k,c):
        def extreme_hullpoint():
            h, p = 0, 0
            for i in range(len(hulls)):
                min_index, min_y = 0, hulls[i][0].y
                for j in range(1, len(hulls[i])):
                    if hulls[i][j].y < min_y:
                        min_y = hulls[i][j].y
                        min_index = j
                if hulls[i][min_index].y < hulls[h][p].y:
                    h = i
                    p = min_index
            return (h, p)
        def tangent(v,p):
            n = len(v)
            l=0
            r,l_before,l_after = n,F.orientation(p,v[0],v[n-1]),F.orientation(p,v[0],v[(l+1)%n])
            while l < r:
                c = ((l + r) >> 1)
                c_before = F.orientation(p, v[c], v[(c - 1) % n])
                c_after = F.orientation(p, v[c], v[(c + 1) % n])
                c_side = F.orientation(p, v[l], v[c])
                if c_before != 1 and c_after != 1:
                    return c
                elif (c_side == 2) and (l_after == 1 or l_before == l_after) or (c_side == 1 and c_before == 1):
                    r = c
                else:
                    l = c+1
                l_before = -c_after
                l_after = F.orientation(p, v[l%n], v[(l + 1) % n])
            return l%n
        def next_hullpoint():

            lpoint = merged_hull[-1]
            p = hulls[lpoint[0]][lpoint[1]]
            next = (lpoint[0],(lpoint[1]+1) % len(hulls[lpoint[0]]))
            for h in range(len(hulls)):
                if h == lpoint[0]:
                    continue
                s = tangent(hulls[h],p)
                q = hulls[next[0]][next[1]]
                r = hulls[h][s]
                t = F.orientation(p,q,r)
                if t == 1 or (t == 0 and F.distance(p,r) > F.distance(p,q)):
                    next = (h,s)
            return next

        print("Utility function called for k: ", k)
        subsets = []
        subsets_size = n // k
        for i in range(0, n, subsets_size):
            subsets.append(self.Points[i:i + subsets_size])
        hulls = [self.graham_scan_utility(subset) for subset in subsets]
        colors = ["blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan", "magenta", "lime",
                  "olive", "gold", "silver", "gray", "lightblue", "lightgreen", "lightgray"]
        temp = 0
        lines = []
        for h in hulls:
            for i in range(0, len(h)):
                self.result_var.set(False)
                self.root.after(self.simulation_speed, self.proceed)
                self.root.wait_variable(self.result_var)
                lines.append(F.Add_Line(self.updated_points[h[i]], self.updated_points[h[(i+1)%len(h)]], c, colors[temp]))
            temp = temp+1 % 17

        merged_hull_points = []
        merged_hull = []
        merged_hull.append(extreme_hullpoint())
        sol_found=False
        for i in range(k):

            p = next_hullpoint()

            if p == merged_hull[0]:
                sol_found = True
                for j in range(len(merged_hull)):
                    merged_hull_points.append(hulls[merged_hull[j][0]][merged_hull[j][1]])
            if sol_found:
                break
            merged_hull.append(p)
        if not sol_found:
            for i in range(len(lines)):
                self.result_var.set(False)
                self.root.after(self.simulation_speed, self.proceed)
                self.root.wait_variable(self.result_var)
                c.delete(lines[i])
        return merged_hull_points
    def BruteForce(self):
        n = len(self.Points)
        c = self.InitializeWindow("Brute Force","Simulation for brute force approach")
        #Perform brute force
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                l1 = F.Add_Line(self.updated_points[self.Points[i]],self.updated_points[self.Points[j]],c,"Purple")
                caninclude = True
                for k in range(n):
                    if k == j or k == i:
                        continue
                    l2 = F.Add_Line(self.updated_points[self.Points[j]],self.updated_points[self.Points[k]],c,"Green")
                    result = F.CheckLine(self.Points[i],self.Points[j],self.Points[k])
                    self.result_var.set(False)
                    self.root.after(self.simulation_speed,self.proceed)
                    self.root.wait_variable(self.result_var)
                    c.delete(l2)
                    if result < 0:
                        caninclude = False
                        break
                c.delete(l1)
                if caninclude:
                    F.Add_Line(self.updated_points[self.Points[i]],self.updated_points[self.Points[j]], c, "White")
                c.pack()
        self.root.mainloop()
    def QuickElimination(self):
        c = self.InitializeWindow("Quick elimination", "Simulation for Quick Elimination algorithm")
        n = len(self.Points)
        c.pack()
        self.root.mainloop()
class LIMenu:
    def __init__(self,lines):
        self.Points = lines
        self.root = tk.Tk()
        self.obj = LineIntersection(self.Points)
        self.DisplayOptions()

    def CloseWindow(self):
        self.root.destroy()
        self.obj.root.destroy()
        MainMenu()

    def CheckOrientation(self):
        self.root.destroy()
        self.obj.CheckOrientation()
    def AntoniosMethod(self):
        self.root.destroy()
        self.obj.AntoniosMethod()
    def DisplayOptions(self):
        self.root.geometry("900x900")
        self.root.config(bg="black")
        self.root.title("Line intersection")
        self.root.protocol("WM_DELETE_WINDOW", self.CloseWindow)
        title_lbl = tk.Label(self.root,text="Algorithms to identify whether two\n line segments intersect",font=('Comic Sans ms',20),bg="black",fg="white")
        title_lbl.pack()
        method1_btn = tk.Button(self.root,text="Check using orientation",command=self.CheckOrientation,font=('Comic Sans ms',15))
        method2_btn = tk.Button(self.root,text="Check using Franklin Antonio's Method", command=self.AntoniosMethod,font=('Comic Sans ms', 15))
        lbl1 = tk.Label(self.root, text="Click any of the following buttons:", font=('Comic Sans ms', 20))
        lbl1.config(bg="black",fg="white")
        lbl1.pack(padx=20,pady=70,anchor="w")
        method1_btn.pack(padx=20,pady=10,anchor="w")
        method2_btn.pack(padx=20, pady=10, anchor="w")
        self.root.mainloop()

class LineIntersection:
    def __init__(self,points):
        self.Points = points
        self.updated_points = {}
        self.circle_radius = 10
        self.start = Point(200, 650)
        self.screenheight = 700
        self.screenwidth = 700
        self.root = tk.Tk()
        self.root.withdraw()
    def CloseWindow(self):
        self.root.destroy()
        LIMenu(self.Points)

    def InitializeWindow(self,title,text):
        self.root.deiconify()
        self.root.protocol("WM_DELETE_WINDOW", self.CloseWindow)
        self.root.geometry("700x700")
        self.root.config(bg="black")
        self.root.title(title)
        title_lbl = tk.Label(self.root,text=text, font=('Comic Sans ms', 20))
        title_lbl.pack(pady=20, anchor="center")
        title_lbl.config(bg="black", fg="white")
        c = tk.Canvas(self.root,width=700, height=700, highlightthickness=0, bg="black")
        origin = self.Points[F.left_most(self.Points)]
        for point in self.Points:
            temp = Point(point.x, point.y)
            temp.x = abs(origin.x - temp.x) * 20 + self.start.x
            temp.y = self.start.y - abs(origin.x + temp.y) * 20
            self.updated_points[point] = temp
            c.create_oval(temp.x, temp.y, temp.x + self.circle_radius, temp.y + self.circle_radius, fill="red")
            coordinates = tk.Label(c, text=f"{point.x},{point.y}", font=('Helvetica', 5), bg="black", fg="white")
            label_window = c.create_window(temp.x, temp.y - 5, window=coordinates)
        F.Add_Line(self.updated_points[self.Points[0]],self.updated_points[self.Points[1]],c,"Green")
        F.Add_Line(self.updated_points[self.Points[2]], self.updated_points[self.Points[3]], c, "Blue")
        c.pack(anchor='w')
        return c,origin
    def CheckOrientation(self):
        c,origin = self.InitializeWindow("Orientation Window","Orientation test")
        displayRes = tk.Text(c,height=10,width=200,bd=0)
        displayRes.place(x=10,y=100,anchor='w')
        fltp = F.StringOrientation(self.Points[0],self.Points[1],self.Points[2])
        flfp = F.StringOrientation(self.Points[0],self.Points[1],self.Points[3])
        slfp = F.StringOrientation(self.Points[2],self.Points[3],self.Points[0])
        slsp = F.StringOrientation(self.Points[2],self.Points[3],self.Points[1])
        flag = F.doIntersect(self.Points[0],self.Points[1],self.Points[2],self.Points[3])
        orientationText = (f"First Point:  ({self.Points[0].x},{self.Points[0].y})\n"
                           f"Second Point: ({self.Points[1].x},{self.Points[1].y})\n"
                           f"Third Point:  ({self.Points[2].x},{self.Points[2].y})\n"
                           f"Fourth Point: ({self.Points[3].x},{self.Points[3].y})\n"
                           f"Orientation of first line segment w.r.t third point: {fltp}\n"
                           f"Orientation of first line segment w.r.t fourth point: {flfp}\n"
                           f"Orientation of second line segment w.r.t first point: {slfp}\n"
                           f"Orientation of second line segment w.r.t second point: {slsp}\n"
                           )
        if flag:
            orientationText += 'The given line segments intersect'
        else:
            orientationText += 'The given line segments do not intersect'
        displayRes.insert("1.0",orientationText)
        displayRes.config(bg="black",fg="white")
        c.pack()
        self.root.mainloop()
    def AntoniosMethod(self):
        c,origin = self.InitializeWindow("Antonio's Intersection", "Franklin Antonio's Faster Line Segment Intersection")
        x,y = F.AntoniosMethod(self.Points)
        IntersectingPoint = Point(x,y)
        displayRes = tk.Text(c, height=10, width=200, bd=0)
        displayRes.place(x=10, y=100, anchor='w')
        orientationText = ""
        if IntersectingPoint.x == -1 and IntersectingPoint.y == -1:
            orientationText += 'The given line segments do not intersect'
        else:
            orientationText += f"The given line segments intersect at ({IntersectingPoint.x},{IntersectingPoint.y})"
            temp = Point(IntersectingPoint.x, IntersectingPoint.y)
            temp.x = abs(origin.x - temp.x) * 20 + self.start.x-5
            temp.y = self.start.y - abs(origin.x + temp.y) * 20 -5
            c.create_oval(temp.x, temp.y, temp.x + self.circle_radius, temp.y + self.circle_radius, fill="purple")
            coordinates = tk.Label(c, text=f"{format(IntersectingPoint.x,'.2f')},{format(IntersectingPoint.y,'.2f')}", font=('Helvetica', 5), bg="black", fg="white")
            label_window = c.create_window(temp.x+30, temp.y+20, window=coordinates)
        displayRes.insert("1.0", orientationText)
        displayRes.config(bg="black", fg="white")
        c.pack()
        self.root.mainloop()

points = []
LinePoints = [Point(3, 8),Point(19, 12),Point(13, 20),Point(8, 2)]
MainMenu()