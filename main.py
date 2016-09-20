import Tkinter
import calendar
import time
import tkFont
import ttk


def sequence(*functions):  # to run 2 or more functions on button click
    for function in functions:
        function()


def update(y, m, tx, curdate):  # generate calendar with right colors
    calstr = calendar.month(y, m)
    tx.configure(state=Tkinter.NORMAL)
    tx.delete('0.0', Tkinter.END)  # remove previous calendar
    tx.insert(Tkinter.INSERT, calstr)
    for i in range(2, 9):
        tx.tag_add("others", '{}.0'.format(i), '{}.end'.format(i))  # tag days for coloring
        if len(tx.get('{}.0'.format(i), '{}.end'.format(i))) == 20:
            tx.tag_add("sun", '{}.end-2c'.format(i), '{}.end'.format(i))
    tx.tag_config("sun", foreground="#fb4622")
    tx.tag_config("others", foreground="#427eb5")
    tx.tag_add("head", '1.0', '1.end')
    if curdate[0] == y and curdate[1] == m:
        index = tx.search(str(curdate[2]), '2.0')  # search for today's date
        tx.tag_add("cur", index, '{}+2c'.format(index))  # highlight today's date
        tx.tag_config("cur", background="blue", foreground="white")
    tx.tag_config("head", font=segoe, foreground="#0d8241", justify=Tkinter.CENTER)
    tx.configure(state=Tkinter.DISABLED)  # make text view not editable


top = Tkinter.Tk()
top.title("Calendar")
top.minsize(200, 200)
top.maxsize(250, 250)
logo = Tkinter.PhotoImage(file="Britalstar.gif")
top.tk.call('wm', 'iconphoto', top._w, logo)
segoe = tkFont.Font(family='Segoe UI')
curtime = time.localtime()
year = Tkinter.StringVar()
month = Tkinter.StringVar()
yearInt = curtime[0]
monthInt = curtime[1]
dateInt = curtime[2]
HLayout = ttk.PanedWindow(top, orient=Tkinter.HORIZONTAL)
ctx = Tkinter.Text(top, padx=10, pady=10, bg="#f3e9ae", relief=Tkinter.FLAT, height=9,
                   width=20)  # text view to passing to functions


def nextb():  # on click next button
    global monthInt, yearInt, ctx, curtime
    monthInt += 1
    if monthInt > 12:
        monthInt = monthInt % 12
        yearInt += 1
    update(yearInt, monthInt, ctx, curtime)


def prevb():  # on click previous button
    global monthInt, yearInt, ctx, curtime
    monthInt -= 1
    if monthInt < 1:
        monthInt = 12
        yearInt -= 1
    update(yearInt, monthInt, ctx, curtime)


def okcall():  # ok button click inside go to date window
    global monthInt, yearInt, ctx, curtime
    if (year.get().isdigit() and month.get().isdigit()) and (
                (0 < int(year.get()) < 10000) and (0 < int(month.get()) < 13)):
        yearInt = int(year.get())
        monthInt = int(month.get())
        update(yearInt, monthInt, ctx, curtime)


def gotod():  # go to date window creation
    newtop = Tkinter.Toplevel()
    newtop.title("Calendar")
    newtop.maxsize(190, 190)
    newtop.focus_set()
    newtop.tk.call('wm', 'iconphoto', newtop._w, logo)
    HLayout = ttk.PanedWindow(newtop, orient=Tkinter.HORIZONTAL)
    HLayout2 = ttk.PanedWindow(newtop, orient=Tkinter.HORIZONTAL)
    yearText = ttk.Label(HLayout, text="Year :")
    yearEdit = ttk.Entry(HLayout, textvariable=year)
    monthText = ttk.Label(HLayout2, text="Month:")
    monthEdit = ttk.Entry(HLayout2, textvariable=month)
    okb = ttk.Button(newtop, text="Ok", command=lambda: sequence(okcall, newtop.destroy))
    yearText.pack(side=Tkinter.LEFT)
    yearEdit.pack(side=Tkinter.RIGHT)
    monthText.pack(side=Tkinter.LEFT)
    monthEdit.pack(side=Tkinter.RIGHT)
    HLayout.pack()
    HLayout2.pack()
    okb.pack()
    newtop.mainloop()


def about_show():  # about window creation
    newtop = Tkinter.Toplevel()
    newtop.title("Calendar")
    newtop.maxsize(190, 190)
    newtop.focus_set()
    newtop.tk.call('wm', 'iconphoto', newtop._w, logo)
    about = ttk.LabelFrame(newtop, text="About")
    Tkinter.Label(about, text="Calendar 2.0").pack()
    Tkinter.Label(about, image=logo, text="Developer: Britalstar", compound=Tkinter.BOTTOM).pack()
    about.pack()
    newtop.mainloop()


update(yearInt, monthInt, ctx, curtime)  # for first run, generate calendar
prev = ttk.Button(HLayout, text="<<", command=prevb)
nex = ttk.Button(HLayout, text=">>", command=nextb)
goto = ttk.Button(top, text="Goto", command=gotod)
menubar = Tkinter.Menu(top, relief=Tkinter.FLAT)
filemenu = Tkinter.Menu(menubar, tearoff=0, relief=Tkinter.FLAT)
helpmenu = Tkinter.Menu(menubar, tearoff=0, relief=Tkinter.FLAT)
filemenu.add_command(label="Goto", command=gotod)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=top.destroy)
helpmenu.add_command(label="About", command=about_show)
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Help", menu=helpmenu)
top.config(menu=menubar)
prev.pack(side=Tkinter.LEFT)
nex.pack(side=Tkinter.RIGHT)
ctx.pack()
HLayout.pack()
goto.pack()
top.mainloop()
