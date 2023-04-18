from inpfilter import *
from tkinter import *
from tkinter import ttk

root = Tk()
scw = root.winfo_screenwidth()
sch = root.winfo_screenheight()
root.geometry(f'{scw}x{sch}')
root.minsize(scw, sch)
root.title('UNI-CARD')
bg = PhotoImage(file="uni.png")
canvas1 = Label(root, width=scw, height=sch, image=bg, justify=CENTER)
canvas1.place(x=0, y=-100)
root.config(bg="#DDDDDD")
x = root.winfo_x()
y = root.winfo_y()
# -----------------------------------------------------------------------------data


ubtn1 = {}
ubtn2 = {}
ubtn3 = {}
ubtn4 = {}


# button_id=0
def get_button_text1(button_id):
    global btn_text1
    """Function to retrieve text of a button with a given identifier"""
    # print(ubtn)
    btn_text1 = ubtn1[button_id]['text']
    take1()
    top1.destroy()


def take1():
    desentry1.delete(0, END)
    desentry1.insert(0, btn_text1)


def get_button_text2(button_id):
    global btn_text2
    """Function to retrieve text of a button with a given identifier"""
    # print(ubtn)
    btn_text2 = ubtn2[button_id]['text']
    take2()
    top2.destroy()


def take2():
    desentry2.delete(0, END)
    desentry2.insert(0, btn_text2)


def get_button_text3(button_id):
    global btn_text3
    """Function to retrieve text of a button with a given identifier"""
    # print(ubtn)
    btn_text3 = ubtn3[button_id]['text']
    take3()
    top3.destroy()


def take3():
    desentry3.delete(0, END)
    desentry3.insert(0, btn_text3)


def get_button_text4(button_id):
    global btn_text4
    """Function to retrieve text of a button with a given identifier"""
    # print(ubtn)
    btn_text4 = ubtn4[button_id]['text']
    take4()
    top4.destroy()


def take4():
    desentry4.delete(0, END)
    desentry4.insert(0, btn_text4)


# from home import *
def to1():
    global top1
    top1 = Toplevel()
    # top1.minsize(500,500)
    string_list = []  # empty list to store the strings
    c = desentry1.get()
    a = str(c)
    # print(a)
    b = ""
    if a.startswith("UC") or a.startswith("uc") or a.startswith("nibp"):
        a = a.upper()
    else:
        a = a.capitalize()
    b = a
    # print(b)
    search_words = b.split()
    i = 0
    with open("materialcode.txt", "r") as file:
        lines = file.readlines()
    # key = k.upper()

    for line in lines:
        # if word in key:

        for word in search_words:
            if word in line:
                global buttons
                # print(line)
                buttons = {}

                string_name = f"string1_{i + 1}"  # create a variable name with a unique number
                string_value = f"{line}"  # create the string value
                locals()[string_name] = string_value  # dynamically create the variable and assign the string value
                string_list.append(locals()[string_name])  # add the variable to the list
                button_text = locals()[f"string1_{i + 1}"]  # create the text for the button
                button = ttk.Button(top1, text=button_text, command=lambda button_id=i: get_button_text1(
                    button_id))  # create the button with the text
                button.pack()  # add the button to the GUI
                buttons[i] = button
                # print(button)
                ubtn1.update(buttons)
                i += 1
                break
    # print(string_list)
    top1.wm_iconbitmap('favicon.ico')


def to2():
    global top2
    top2 = Toplevel()
    string_list = []  # empty list to store the strings
    c = desentry2.get()
    a = str(c)
    # print(a)
    b = ""
    if a.startswith("UC") or a.startswith("uc") or a.startswith("nibp"):
        a = a.upper()
    else:
        a = a.capitalize()
    b = a
    # print(b)
    search_words = b.split()
    i = 0
    with open("materialcode.txt", "r") as file:
        lines = file.readlines()
    # key = k.upper()

    for line in lines:
        # if word in key:

        for word in search_words:
            if word in line:
                # print(line)
                string_name = f"string2_{i + 1}"  # create a variable name with a unique number
                string_value = f"{line}"  # create the string value
                locals()[string_name] = string_value  # dynamically create the variable and assign the string value
                string_list.append(locals()[string_name])  # add the variable to the list
                button_text = locals()[f"string2_{i + 1}"]  # create the text for the button
                button = ttk.Button(top2, text=button_text, command=lambda button_id=i: get_button_text2(
                    button_id))  # create the button with the text
                button.pack()  # add the button to the GUI
                buttons[i] = button
                # print(button)
                ubtn2.update(buttons)
                i += 1
                # MAKE SEPrATE INPUTS FOr SEPArATE BUTTONS
                break
    # print(string_list)
    top2.wm_iconbitmap('favicon.ico')


def to3():
    global top3
    top3 = Toplevel()
    string_list = []  # empty list to store the strings
    c = desentry3.get()
    a = str(c)
    # print(a)
    b = ""
    if a.startswith("UC") or a.startswith("uc") or a.startswith("nibp"):
        a = a.upper()
    else:
        a = a.capitalize()
    b = a
    # print(b)
    search_words = b.split()
    i = 0
    with open("materialcode.txt", "r") as file:
        lines = file.readlines()
    # key = k.upper()

    for line in lines:
        # if word in key:

        for word in search_words:
            if word in line:
                # print(line)
                string_name = f"string3_{i + 1}"  # create a variable name with a unique number
                string_value = f"{line}"  # create the string value
                locals()[string_name] = string_value  # dynamically create the variable and assign the string value
                string_list.append(locals()[string_name])  # add the variable to the list
                button_text = locals()[f"string3_{i + 1}"]  # create the text for the button
                button = ttk.Button(top3, text=button_text, command=lambda button_id=i: get_button_text3(
                    button_id))  # create the button with the text
                button.pack()  # add the button to the GUI
                buttons[i] = button
                # print(button)
                ubtn3.update(buttons)
                i += 1
                break
    # print(string_list)
    top3.wm_iconbitmap('favicon.ico')


def to4():
    global top4
    top4 = Toplevel()
    string_list = []  # empty list to store the strings
    c = desentry4.get()
    a = str(c)
    # print(a)
    b = ""
    if a.startswith("UC") or a.startswith("uc") or a.startswith("nibp"):
        a = a.upper()
    else:
        a = a.capitalize()
    b = a
    # print(b)
    search_words = b.split()
    i = 0
    with open("materialcode.txt", "r") as file:
        lines = file.readlines()
    # key = k.upper()

    for line in lines:
        # if word in key:

        for word in search_words:
            if word in line:
                # print(line)
                string_name = f"string4_{i + 1}"  # create a variable name with a unique number
                string_value = f"{line}"  # create the string value
                locals()[string_name] = string_value  # dynamically create the variable and assign the string value
                string_list.append(locals()[string_name])  # add the variable to the list
                button_text = locals()[f"string4_{i + 1}"]  # create the text for the button
                button = ttk.Button(top4, text=button_text, command=lambda button_id=i: get_button_text4(
                    button_id))  # create the button with the text
                button.pack()  # add the button to the GUI
                buttons[i] = button
                # print(button)
                ubtn4.update(buttons)
                i += 1
                break
    # print(string_list)
    top4.wm_iconbitmap('favicon.ico')


# -----------------------------------------------------------------------------funx

def totupdate_supply():
    totupdate(1)


def totupdate(self):
    # print(sta)
    match sta:
        case 1:
            secalc()
        case 2:
            sscal()


def secalc():
    ratin1 = rat1.get()
    ratin2 = rat2.get()
    ratin3 = rat3.get()
    ratin4 = rat4.get()
    gstin1 = gst1.get()
    gstin2 = gst2.get()
    gstin3 = gst3.get()
    gstin4 = gst4.get()
    qtin1 = qt1.get()
    qtin2 = qt2.get()
    qtin3 = qt3.get()
    qtin4 = qt4.get()
    r1 = printInput(ratin1)[1]
    rat1.delete(0, END)
    rat1.insert(0, r1)
    r2 = printInput(ratin2)[1]
    rat2.delete(0, END)
    rat2.insert(0, r2)
    r3 = printInput(ratin3)[1]
    rat3.delete(0, END)
    rat3.insert(0, r3)
    r4 = printInput(ratin4)[1]
    rat4.delete(0, END)
    rat4.insert(0, r4)
    g1 = printInput(gstin1)[1]
    gst1.delete(0, END)
    gst1.insert(0, g1)
    g2 = printInput(gstin2)[1]
    gst2.delete(0, END)
    gst2.insert(0, g2)
    g3 = printInput(gstin3)[1]
    gst3.delete(0, END)
    gst3.insert(0, g3)
    g4 = printInput(gstin4)[1]
    gst4.delete(0, END)
    gst4.insert(0, g4)
    q1 = printInput(qtin1)[1]
    qt1.delete(0, END)
    qt1.insert(0, q1)
    q2 = printInput(qtin2)[1]
    qt2.delete(0, END)
    qt2.insert(0, q2)
    q3 = printInput(qtin3)[1]
    qt3.delete(0, END)
    qt3.insert(0, q3)
    q4 = printInput(qtin4)[1]
    qt4.delete(0, END)
    qt4.insert(0, q4)
    nr1 = r1 * q1
    nr2 = r2 * q2
    nr3 = r3 * q3
    nr4 = r4 * q4
    se = (nr1 + ((nr1 * g1) / 100) + nr2 + ((nr2 * g2) / 100) + nr3 + ((nr3 * g3) / 100) + nr4 + ((nr4 * g4) / 100))
    totdata.config(text=se)


def sscal():
    ratin1 = rat1.get()
    ratin2 = rat2.get()
    ratin3 = rat3.get()
    ratin4 = rat4.get()
    qtin1 = qt1.get()
    qtin2 = qt2.get()
    qtin3 = qt3.get()
    qtin4 = qt4.get()
    r1 = printInput(ratin1)[1]
    rat1.delete(0, END)
    rat1.insert(0, r1)
    r2 = printInput(ratin2)[1]
    rat2.delete(0, END)
    rat2.insert(0, r2)
    r3 = printInput(ratin3)[1]
    rat3.delete(0, END)
    rat3.insert(0, r3)
    r4 = printInput(ratin4)[1]
    rat4.delete(0, END)
    rat4.insert(0, r4)
    q1 = printInput(qtin1)[1]
    qt1.delete(0, END)
    qt1.insert(0, q1)
    q2 = printInput(qtin2)[1]
    qt2.delete(0, END)
    qt2.insert(0, q2)
    q3 = printInput(qtin3)[1]
    qt3.delete(0, END)
    qt3.insert(0, q3)
    q4 = printInput(qtin4)[1]
    qt4.delete(0, END)
    qt4.insert(0, q4)
    nr1 = r1 * q1
    nr2 = r2 * q2
    nr3 = r3 * q3
    nr4 = r4 * q4
    ss = (nr1 + nr2 + nr3 + nr4)
    totdata.config(text=ss)


def clear():
    ghost.grid_forget()
    enter1.grid_forget()
    enter2.grid_forget()
    enter3.grid_forget()
    enter4.grid_forget()
    enter5.grid_forget()
    rat1.delete(0, END)
    rat2.delete(0, END)
    rat3.delete(0, END)
    rat4.delete(0, END)
    desentry1.delete(0, END)
    desentry2.delete(0, END)
    desentry3.delete(0, END)
    desentry4.delete(0, END)
    mesentry.delete(0, END)
    billndata.config(text='')
    beofentry.delete(0, END)
    totdata.config(text='')
    qt1.delete(0, END)
    qt1.insert(0, '1')
    qt2.delete(0, END)
    qt2.insert(0, '1')
    qt3.delete(0, END)
    qt3.insert(0, '1')
    qt4.delete(0, END)
    qt4.insert(0, '1')


def callent():
    global sta
    sta = 1
    root.title('Uni-Card Enterprises')
    clear()
    ce()


def callserv():
    global sta
    sta = 2
    root.title('Uni-Card Services')
    clear()
    cs()


# -----------------------------------------------------------------------------page en
def ce():
    mes.grid(row=0, column=0, padx=15, pady=20)
    mesentry.grid(row=0, column=1)
    srno.grid(row=1, column=0, padx=15, pady=20)
    desc.grid(row=1, column=1, padx=15, pady=20)
    rat.grid(row=1, column=3, padx=15, pady=20)
    gst.grid(row=1, column=4, padx=15, pady=20)
    beof.grid(row=6, column=0, padx=15, pady=20)
    totdata.grid(row=6, column=4, columnspan=2, sticky="E")
    billndata.grid(row=0, column=4, columnspan=2, sticky="E")
    tot.grid(row=6, column=3, padx=15, pady=20, sticky="E")
    billn.grid(row=0, column=3, padx=15, pady=20, sticky="E")
    srn1.grid(row=r, column=0, padx=15, pady=20)
    srn2.grid(row=r + 1, column=0, padx=15, pady=20)
    srn3.grid(row=r + 2, column=0, padx=15, pady=20)
    srn4.grid(row=r + 3, column=0, padx=15, pady=20)
    desentry1.grid(row=2, column=1, columnspan=2, sticky="w")
    find1.grid(row=2, column=1, rowspan=2, sticky="w")
    desentry2.grid(row=3, column=1, columnspan=2, sticky="w")
    find2.grid(row=3, column=1, rowspan=2, sticky="w")
    desentry3.grid(row=4, column=1, columnspan=2, sticky="w")
    find3.grid(row=4, column=1, rowspan=2, sticky="w")
    desentry4.grid(row=5, column=1, columnspan=2, sticky="w")
    find4.grid(row=5, column=1, rowspan=2, sticky="w")
    beofentry.grid(row=6, column=1, columnspan=2, sticky="w")
    rat1.grid(row=2, column=3)
    # rat1.unbind("<Return>")
    rat2.grid(row=3, column=3)
    rat3.grid(row=4, column=3)
    rat4.grid(row=5, column=3)
    qt.grid(row=1, column=4, sticky="w", padx=0)
    qt1.grid(row=2, column=4, padx=0)
    qt2.grid(row=3, column=4, padx=0)
    qt3.grid(row=4, column=4, padx=0)
    qt4.grid(row=5, column=4, padx=0)
    subbtn.grid(row=7, column=5, columnspan=2)
    global se, r1, r2, r3, r4, g1, g2, g3, g4, ratin1, ratin2, ratin3, ratin4, gstin1, gstin2, gstin3, gstin4

    gst1.grid(row=2, column=5, sticky="w")
    gst2.grid(row=3, column=5, sticky="w")
    gst3.grid(row=4, column=5, sticky="w")
    gst4.grid(row=5, column=5, sticky="w")
    gst.grid(row=1, column=5, padx=15, pady=20)
    subbtn.config(command=totupdate_supply)


# -----------------------------------------------------------------------------page serv
def cs():
    global se, r1, r2, r3, r4, g1, g2, g3, g4, ratin1, ratin2, ratin3, ratin4, gstin1, gstin2, gstin3, gstin4

    mes.grid(row=0, column=0, padx=15, pady=20)
    mesentry.grid(row=0, column=1)
    srno.grid(row=1, column=0, padx=15, pady=20)
    desc.grid(row=1, column=1, padx=15, pady=20)
    rat.grid(row=1, column=3, padx=15, pady=20)
    beof.grid(row=6, column=0, padx=15, pady=20)
    totdata.grid(row=6, column=4)
    billndata.grid(row=0, column=4, columnspan=2)
    billn.grid(row=0, column=3, padx=15, pady=20)
    tot.grid(row=6, column=3, padx=15, pady=20)
    srn1.grid(row=r, column=0, padx=15, pady=20)
    srn2.grid(row=r + 1, column=0, padx=15, pady=20)
    srn3.grid(row=r + 2, column=0, padx=15, pady=20)
    srn4.grid(row=r + 3, column=0, padx=15, pady=20)
    desentry1.grid(row=2, column=1, columnspan=2, sticky="w")
    find1.grid(row=2, column=1, rowspan=2, sticky="w")
    desentry2.grid(row=3, column=1, columnspan=2, sticky="w")
    find2.grid(row=3, column=1, rowspan=2, sticky="w")
    desentry3.grid(row=4, column=1, columnspan=2, sticky="w")
    find3.grid(row=4, column=1, rowspan=2, sticky="w")
    desentry4.grid(row=5, column=1, columnspan=2, sticky="w")
    find4.grid(row=5, column=1, rowspan=2, sticky="w")
    beofentry.grid(row=6, column=1, columnspan=2, sticky="w")
    rat1.grid(row=2, column=3)
    rat2.grid(row=3, column=3)
    rat3.grid(row=4, column=3)
    rat4.grid(row=5, column=3)
    subbtn.grid(row=7, column=3, padx=15, pady=20)
    qt.grid(row=1, column=4, padx=30)
    qt1.grid(row=2, column=4, padx=20)
    qt2.grid(row=3, column=4, padx=20)
    qt3.grid(row=4, column=4, padx=20)
    qt4.grid(row=5, column=4, padx=20)
    gst1.grid_forget()
    gst2.grid_forget()
    gst3.grid_forget()
    gst4.grid_forget()
    gst.grid_forget()
    subbtn.config(command=totupdate_supply)

    # subbtn.config(command=totupdate)


# -----------------------------------------------------------------------------invoice
# def inv():

# -----------------------------------------------------------------------------deliveryChallan
# def dc():
# -----------------------------------------------------------------------------widgets
billndata = ttk.Label(root, text="", width=20, relief='sunken', font=('Arial', 12))
totdata = ttk.Label(root, text="", width=20, relief='sunken', font=('Arial', 12))
mes = Label(root, text='Messers :', font=("Arial", 15), bg="#DDDDDD")
mesenvar = StringVar()
mesentry = ttk.Entry(root, textvariable=mesenvar, width=90, xscrollcommand='-wrapt', font=('Arial', 12))
srno = Label(root, text='Sr no.', font=("Arial", 15), bg="#DDDDDD")
desc = Label(root, text='Description', font=("Arial", 15), bg="#DDDDDD")
rat = Label(root, text='Rate', font=("Arial", 15), bg="#DDDDDD")
qt = Label(root, text='Quantity', font=("Arial", 15), bg="#DDDDDD", padx=10)
gst = Label(root, text='% GST', font=("Arial", 15), bg="#DDDDDD")
beof = Label(root, text='On Behalf of Uni-Card Enterprises :', font=("Arial", 12), wrap=155, bg="#DDDDDD", )
tot = Label(root, text='Total :', font=("Arial", 15), bg="#DDDDDD", )
billn = Label(root, text='Bill no. :', font=("Arial", 15), bg="#DDDDDD", )
r = 2
srn1 = Label(root, text='1.', font=("Arial", 15), bg="#DDDDDD", height=3)
srn2 = Label(root, text='2.', font=("Arial", 15), bg="#DDDDDD", height=3)
srn3 = Label(root, text='3.', font=("Arial", 15), bg="#DDDDDD", height=3)
srn4 = Label(root, text='4.', font=("Arial", 15), bg="#DDDDDD", height=3)
desenvar1 = StringVar()
desenvar2 = StringVar()
desenvar3 = StringVar()
desenvar4 = StringVar()
beofenvar = StringVar()
desentry1 = ttk.Entry(root, textvariable=desenvar1, width=85, font=('Arial', 12))
find1 = ttk.Button(root, text='Find1', width=10, command=to1)
desentry2 = ttk.Entry(root, textvariable=desenvar2, width=85, font=('Arial', 12))
find2 = ttk.Button(root, text='Find2', width=10, command=to2)
desentry3 = ttk.Entry(root, textvariable=desenvar3, width=85, font=('Arial', 12))
find3 = ttk.Button(root, text='Find3', width=10, command=to3)
desentry4 = ttk.Entry(root, textvariable=desenvar4, width=85, font=('Arial', 12))
find4 = ttk.Button(root, text='Find4', width=10, command=to4)
beofentry = ttk.Entry(root, textvariable=beofenvar, width=85, font=('Arial', 12))
beoff = beofenvar.get()

# global rat1, rat2, rat3, rat4, gst1, gst2, gst3, gst4
rat1 = ttk.Entry(root, width=20, font=('Arial', 12))
rat2 = ttk.Entry(root, width=20, font=('Arial', 12))
rat3 = ttk.Entry(root, width=20, font=('Arial', 12))
rat4 = ttk.Entry(root, width=20, font=('Arial', 12))
qt1 = Spinbox(root, width=5, font=('Arial', 12), justify='center', from_=0, to=10000)
qt2 = Spinbox(root, width=5, font=('Arial', 12), justify='center', from_=0, to=10000)
qt3 = Spinbox(root, width=5, font=('Arial', 12), justify='center', from_=0, to=10000)
qt4 = Spinbox(root, width=5, font=('Arial', 12), justify='center', from_=0, to=10000)
gst1 = ttk.Entry(root, width=20, font=('Arial', 12))
# gst1.grid(row=2, column=4)
gst2 = ttk.Entry(root, width=20, font=('Arial', 12))
# gst2.grid(row=3, column=4)
gst3 = ttk.Entry(root, width=20, font=('Arial', 12))
# gst3.grid(row=4, column=4)
gst4 = ttk.Entry(root, width=20, font=('Arial', 12))
# gst4.grid(row=5, column=4)
rat1.bind("<Return>", totupdate)
rat2.bind("<Return>", totupdate)
rat3.bind("<Return>", totupdate)
rat4.bind("<Return>", totupdate)
gst1.bind("<Return>", totupdate)
gst2.bind("<Return>", totupdate)
gst3.bind("<Return>", totupdate)
gst4.bind("<Return>", totupdate)
subbtn = ttk.Button(root, text='Calculate', width=20)
ghost = Label(root, state='disabled', bg='#DDDDDD')
ghost.grid(column=0, row=0, padx=((scw // 2) - 130, 0))
enter1 = ttk.Button(root, text='Enterprises', width=40, command=callent)
enter1.grid(column=1, row=0, pady=10, ipady=10)
enter2 = ttk.Button(root, text='Services', width=40, command=callserv)
enter2.grid(column=1, row=1, pady=10, ipady=10)
enter3 = ttk.Button(root, text='Invoice', width=40)
enter3.grid(column=1, row=2, pady=10, ipady=10)
enter4 = ttk.Button(root, text='Delivery Challan', width=40)
enter4.grid(column=1, row=3, pady=10, ipady=10)
enter5 = ttk.Button(root, text='Recipt', width=40)
enter5.grid(column=1, row=4, pady=10, ipady=10)

# -----------------------------------------------------------------------------widgets

# -----------------------------------------------------------------------------menu
men = Menu(root)
submen = Menu(men, tearoff=0)
submen.add_command(label='Enterprises', command=callent)
submen.add_command(label='Services', command=callserv)
submen.add_command(label='Invoice')
submen.add_command(label='Recipt')
submen.add_command(label='Delivery Challan')
men.add_cascade(label='Billing', menu=submen)
root.config(menu=men)
# -----------------------------------------------------------------------------menu

root.attributes('-transparentcolor')
root.state('zoomed')
root.wm_iconbitmap('favicon.ico')
root.mainloop()
