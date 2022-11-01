import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Label

from Simuladores.MM1_calc import calcular as mm1_calc
from Simuladores.MD1_calc import calcular as md1_calc
from Simuladores.ME1_calc import calcular as me1_calc
from Simuladores.MMs_calc import calcular as mms_calc
from Simuladores.MMG1_calc import calcular as mmg1_calc
from Simuladores.MMsK_calc import calcular as mmsk_calc

calcs = mm1_calc(1, 2)
pokemon_info = calcs.items()


frame_styles = {"relief": "groove",
                "bd": 3, "bg": "#FFFFFF",
                "fg": "#073bb3", "font": ("Century Gothic", 9, "bold")}



class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)

        menu_file = tk.Menu(self, tearoff=0)
        self.add_cascade(label="M/M/1", menu=menu_file)
       # menu_file.add_command(label="All Widgets", command=lambda: parent.show_frame(Some_Widgets))
        #menu_file.add_separator()
        menu_file.add_command(label="Exit Application", command=lambda: parent.Quit_application())

        menu_orders = tk.Menu(self, tearoff=0)
        self.add_cascade(label="M/M/s", menu=menu_orders)

        menu_pricing = tk.Menu(self, tearoff=0)
        self.add_cascade(label="M/M/s/K", menu=menu_pricing)

        menu_operations = tk.Menu(self, tearoff=0)
        self.add_cascade(label="M/M/G/1", menu=menu_operations)

        menu_positions = tk.Menu(menu_operations, tearoff=0)
        self.add_cascade(label="M/E/1", menu=menu_positions)

        menu_help = tk.Menu(self, tearoff=0)
        self.add_cascade(label="M/D/1", menu=menu_help)

        menu_exit = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Ajustes", menu=menu_file)
        menu_exit.add_command(label="Salir", command=lambda: parent.Quit_application())
class MyApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        main_frame = tk.Frame(self, bg="#84CEEB", height=600, width=1024)
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        # self.resizable(0, 0) prevents the app from being resized
        # self.geometry("1024x600") fixes the applications size
        self.frames = {}
        pages = (Some_Widgets, PageOne, PageTwo, PageThree, PageFour)
        for F in pages:
            frame = F(main_frame, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Some_Widgets)
        menubar = MenuBar(self)
        tk.Tk.config(self, menu=menubar)

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def OpenNewWindow(self):
        OpenNewWindow()

    def Quit_application(self):
        self.destroy()


class GUI(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.main_frame = tk.Frame(self, bg="#F1EFFA", height=600, width=1024)
        # self.main_frame.pack_propagate(0)
        self.main_frame.pack(fill="both", expand="true")
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)


class Some_Widgets(GUI):  # inherits from the GUI class
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        frame1 = tk.LabelFrame(self, frame_styles, text="Results")
        frame1.place(rely=0.05, relx=0.02, height=400, width=400)



        # Create a Button to validate Entry Widget
        frame2 = tk.LabelFrame(self, frame_styles, text="Some widgets")
        frame2.place(rely=0.05, relx=0.45, height=500, width=500)

        txt1 = tk.Label(frame1, text="Ingresa de tasa servicios")
        tip1 = tk.Label(frame1, text="Tip:")

        txt1.pack()
        tip1.pack()
        tasa_servicios = tk.Entry(frame1)
        tasa_servicios.pack()

        txt2 = tk.Label(frame1, text="Ingresa de tasa llegadas")
        tip2 = tk.Label(frame1, text="Tip:")
        txt2.pack()
        tip2.pack()
        tasa_llegadas = tk.Entry(frame1)
        tasa_llegadas.pack()



        button1 = tk.Button(frame1, text="tk button", command=lambda: Refresh_data())
        button1.pack()


        # This is a treeview.
        tv1 = ttk.Treeview(frame2)
        column_list_account = ["Name", "Value"]
        tv1['columns'] = column_list_account
        tv1["show"] = "headings"  # removes empty column
        for column in column_list_account:
            tv1.heading(column, text=column)
            tv1.column(column, width=50)
        tv1.place(relheight=1, relwidth=0.995)
        treescroll = tk.Scrollbar(frame1)
        treescroll.configure(command=tv1.yview)
        tv1.configure(yscrollcommand=treescroll.set)
        treescroll.pack(side="right", fill="y")

        def Load_data():
            for row in pokemon_info:
                tv1.insert("", "end", values=row)

        def Refresh_data():
            # Deletes the data in the current treeview and reinserts it.
            tv1.delete(*tv1.get_children())  # *=splat operator
            Load_data()

        Load_data()


class PageOne(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="Page One")
        label1.pack(side="top")


class PageThree(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="Page Three")
        label1.pack(side="top")


class PageFour(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="Page Four")
        label1.pack(side="top")


class PageTwo(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="Page Two")
        label1.pack(side="top")


class OpenNewWindow(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        main_frame = tk.Frame(self)
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        self.title("Here is the Title of the Window")
        self.geometry("500x500")
        self.resizable(0, 0)

        frame1 = ttk.LabelFrame(main_frame, text="This is a ttk LabelFrame")
        frame1.pack(expand=True, fill="both")

        label1 = tk.Label(frame1, font=("Verdana", 20), text="OpenNewWindow Page")
        label1.pack(side="top")


top = MyApp()
top.title("Simulador de Modelos de Filas y Colas Equipo 2")
root = MyApp()
root.withdraw()
root.title("Simulador de Modelos de Filas y Colas Equipo 2")

root.mainloop()