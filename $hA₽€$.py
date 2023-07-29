from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def message():
    messagebox.showinfo("Note", "Enter a StartX, StartY, EndX, EndY, and color.\n"
                                "Then, press C, R, O, or L on your keyboard to get a surprise!\n(O and C are the same)")
    
def more():
    messagebox.showinfo("More AMAZING projects created by Devansh Balani","I create projects in various languages like Python, HTML, CSS, JS, Block-based Coding etc. Check out my new codes!"
                        "\n"
                        "\n"
                        "\n"
                        "\n"
                        "\n"
                        "\n"
                        "\n"
                        "\n"
                        "\n"
                        "\n"
                        "\n"
                        "\n"
                        "\n"
                        "\n"
                        "(this popup is under construction!)")

def draw(keypress, oldx, oldy, newx, newy):
    colour = combobox.get()
    if keypress == 'c':
        canvas.create_oval(oldx, oldy, newx, newy, width=3, fill=colour)
    elif keypress == 'r':
        canvas.create_rectangle(oldx, oldy, newx, newy, width=3, fill=colour)
    elif keypress == 'o':
        canvas.create_oval(oldx, oldy, newx, newy, width=3, fill=colour)
    elif keypress == 'i':
        canvas.create_line(oldx, oldy, newx, newy, width=3, fill=colour)

def circle(event):
    oldx = startx_dropdown.get()
    oldy = starty_dropdown.get()
    newx = endx_dropdown.get()
    newy = endy_dropdown.get()
    keypress = 'c'
    draw(keypress, oldx, oldy, newx, newy)
    
def rectangle(event):
    oldx = startx_dropdown.get()
    oldy = starty_dropdown.get()
    newx = endx_dropdown.get()
    newy = endy_dropdown.get()
    keypress = 'r'
    draw(keypress, oldx, oldy, newx, newy)
    
def line(event):
    oldx = startx_dropdown.get()
    oldy = starty_dropdown.get()
    newx = endx_dropdown.get()
    newy = endy_dropdown.get()
    keypress = 'i'
    draw(keypress, oldx, oldy, newx, newy)
    
def oval(event):
    oldx = startx_dropdown.get()
    oldy = starty_dropdown.get()
    newx = endx_dropdown.get()
    newy = endy_dropdown.get()
    keypress = 'c'
    draw(keypress, oldx, oldy, newx, newy)

root = Tk()
root.title("Shapes")
root.geometry("850x675")
root.configure(bg="yellow")

canvas = Canvas(root, width=825, height=500, bg="white", highlightbackground="cyan", highlightthickness=5)
canvas.pack()

note_btn = Button(root, text="Note(Click me!)", bg="orange", fg="red", command=message)
note_btn.place(relx=0.25, rely=0.785, anchor=CENTER)

more_btn = Button(root, text="More", bg="brown", fg="white", command=more)
more_btn.place(relx=0.75, rely=0.785, anchor=CENTER)

label = Label(root, text="Pick a color:", bg="yellow", fg="brown")
label.place(relx=0.45, rely=0.96, anchor=CENTER)

color_list = ["orange", "cyan", "yellow", "purple", "pink", "red", "blue", "brown", "black"]
combobox = ttk.Combobox(root, state="readonly", values=color_list, width=15)
combobox.place(relx=0.6, rely=0.96, anchor=CENTER)

startx_label = Label(root, text="StartX =", bg="yellow", fg="brown")
startx_label.place(relx=0.075, rely=0.85, anchor=CENTER)

number_list = ["50", "100", "150", "200", "250", "300", "350", "400", "450", "500", "550", "600", "650", "700", "750", "800", "850", "900"]
startx_dropdown = ttk.Combobox(root, state="readonly", values=number_list, width=15)
startx_dropdown.place(relx=0.175, rely=0.85, anchor=CENTER)

starty_label = Label(root, text="StartY =", bg="yellow", fg="brown")
starty_label.place(relx=0.325, rely=0.85, anchor=CENTER)

starty_dropdown = ttk.Combobox(root, state="readonly", values=number_list, width=15)
starty_dropdown.place(relx=0.425, rely=0.85, anchor=CENTER)

endx_label = Label(root, text="EndX =", bg="yellow", fg="brown")
endx_label.place(relx=0.575, rely=0.85, anchor=CENTER)

endx_dropdown = ttk.Combobox(root, state="readonly", values=number_list, width=15)
endx_dropdown.place(relx=0.675, rely=0.85, anchor=CENTER)

endy_label = Label(root, text="EndY =", bg="yellow", fg="brown")
endy_label.place(relx=0.825, rely=0.85, anchor=CENTER)

endy_dropdown = ttk.Combobox(root, state="readonly", values=number_list, width=15)
endy_dropdown.place(relx=0.925, rely=0.85, anchor=CENTER)

root.bind("c", circle)
root.bind("r", rectangle)
root.bind("l", line)
root.bind("o", oval)

root.mainloop()