import tkinter as tk
from tkinter import ttk

# main window

window = tk.Tk()
window.title('Pygame first project')
window.geometry("800x600")
window.configure(bg="light grey")

# input label and entry

tk.Label(window, text = "pygwidgets example by Irv Kalb", bg = "light gray", font =("Arial 20 bold")).place(x = 190, y = 20)
entry = tk.Entry(window, width=30, bg = "black", font =("Arial 11 bold"), fg='white')
entry.insert(0, "Default input text")
entry.place(x=20, y=90)

# Empty label
entry = tk.Entry(window, width=30, bg = "white", font =("Arial 11 bold"), fg='white')
entry.insert(0, "")
entry.place(x=20, y=200)

# Centered text (multi-line)
centered_text = "Here is some centered display text.\nShowing the\nnumber of frames.\nLoop counter: 95"
tk.Label(window, text=centered_text, bg='light grey',font=("arial 11 bold"),fg="white", justify="center").place(x=20, y=290)

# Drag me label (simulated as a button)
drag_label = tk.Label(window, text="DRAG\nME", bg="gray", fg="black",font=("arial 11 bold"), width=10, height=5, relief="raised")
drag_label.place(x=350, y=210)

# Display text at bottom
tk.Label(window, text="Here is some display text.  Loop counter:95", font=('Arial', 10, 'bold'), bg='white').place(x=20, y=400)

# Restart button
restart_button = tk.Button(window, text="Restart", font=('arial 11 bold'), width=10)
restart_button.place(x=100, y=430)

# Bottom instructions (left and right)
tk.Label(window, text="Click then up or down arrow to resize,\nleft or right arrow to rotate,\nh or v to flip horizontal or vertical", bg='light grey',font=("arial 9 bold"), justify='left').place(x=20, y=550)

# Checkbox: Allow radio btns (top right)
allow_radio_var = tk.IntVar(value=1)
tk.Checkbutton(window, text="Allow radio btns",font=('Arial', 12, 'bold'), variable=allow_radio_var, bg='light grey').place(x=550, y=70)

# Radio group: Low/Med/High
level_var = tk.StringVar(value="Med")
tk.Radiobutton(window, text="Low", variable=level_var, value="Low",bg='light grey', font=('Arial', 11, 'bold'),indicatoron=False, width=10, relief='raised', bd=2).place(x=580, y=130)
tk.Radiobutton(window, text="Med", variable=level_var, value="Low",bg='light grey', font=('Arial', 11, 'bold'),indicatoron=False, width=10, relief='raised', bd=2).place(x=580, y=170)
tk.Radiobutton(window, text="High", variable=level_var, value="Low",bg='light grey', font=('Arial', 11, 'bold'),indicatoron=False, width=10, relief='raised', bd=2).place(x=580, y=210)

# Another checkbox: Allow Radio Buttons
allow_radio_2 = tk.IntVar(value=1)
tk.Checkbutton(window, text="Allow Radio Buttons", font=('Arial', 11, 'bold'), variable=allow_radio_2, bg='light grey').place(x=550, y=270)

# Another set of radio buttons
radio_var = tk.StringVar(value="Radio Text 2")
tk.Radiobutton(window, text="Radio Text 1",font=('Arial', 11, 'bold'), variable=radio_var, value="Radio Text 1", bg='light grey').place(x=580, y=300)
tk.Radiobutton(window, text="Radio Text 2",font=('Arial', 11, 'bold'), variable=radio_var, value="Radio Text 2", bg='light grey').place(x=580, y=330)
tk.Radiobutton(window, text="Radio Text 3",font=('Arial', 11, 'bold'), variable=radio_var, value="Radio Text 3", bg='light grey').place(x=580, y=360)

# Show Status button
tk.Button(window, text="Show Status",font=('Arial', 11, 'bold'), width=12).place(x=590, y=400)

# START button (bottom right)
tk.Button(window, text="START", font=('Arial', 12, 'bold'), bg='light grey', width=15, height=2).place(x=520, y=480)

tk.Label(window, text="Click then type l, r, d, u, s, or Space",font=('Arial', 9, 'bold'), bg='light grey', justify='left').place(x=520, y=540)

window.mainloop()

