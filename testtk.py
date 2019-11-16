from tkinter import *

import tkinter

top = Tk()

mb = Menubutton(top, text="condiments", relief=RAISED)
mb2 = Menubutton(top, text="condiments", relief=RAISED)
mb.grid()
mb.menu1 = Menu(mb, tearoff=0)
mb.menu2 = Menu(mb2,tearoff=0)
print(type(mb))
# mb["m"] = mb.menu1
mb["m1"] = mb.menu2

mayoVar = IntVar()
ketchVar = IntVar()

mb.menu1.add_checkbutton(label="mayo",
                        variable=mayoVar)
mb.menu1.add_checkbutton(label="ketchup",
                        variable=ketchVar)

mb.pack()
top.mainloop()