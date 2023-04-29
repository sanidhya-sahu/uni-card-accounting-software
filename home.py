from inpfilter import *
from tkinter import *
from tkinter import ttk

# import cplist
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
cbtnen = {}
cbtnserv = {}


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


def get_button_textcnamserv(button_id):
    global btn_textcna
    """Function to retrieve text of a button with a given identifier"""
    # print(ubtn)
    btn_textcna = cbtnserv[button_id]['text']
    takecnamserv()
    cnaserv.destroy()


def takecnamserv():
    mesentry.delete(0, END)
    mesentry.insert(0, btn_textcna)
    coustname.delete(0,END)
    coustname.insert(0,btn_textcna)


def get_button_textcnamen(button_id):
    global btn_textcnaen
    """Function to retrieve text of a button with a given identifier"""
    # print(ubtn)
    btn_textcnaen = cbtnen[button_id]['text']
    takecnamen()
    cnaen.destroy()


def takecnamen():
    mesentry.delete(0, END)
    mesentry.insert(0, btn_textcnaen)
    coustname.delete(0, END)
    coustname.insert(0, btn_textcnaen)


# from home import *
def cnamen(self):
    # print(sta)
    global cnaen
    cnaen = Toplevel()
    cnaen.geometry('400x400')
    cnaen.minsize(400, 400)
    mf = Frame(cnaen)
    mf.pack(fill=BOTH, expand=1)
    mcan = Canvas(mf)
    mcan.pack(side=LEFT, fill=BOTH, expand=1)
    scrbar = ttk.Scrollbar(mf, orient=VERTICAL, command=mcan.yview)
    scrbar.pack(side=RIGHT, fill=Y)
    mcan.config(yscrollcommand=scrbar.set)
    mcan.bind('<Configure>', lambda e: mcan.config(scrollregion=mcan.bbox('all')))

    sf = Frame(mcan)
    mcan.create_window((0, 0), window=sf, anchor=NW)

    # top1.minsize(500,500)
    string_list = []  # empty list to store the strings
    if bool(mesentry.winfo_ismapped()) == TRUE:
        c = mesentry.get()
    elif bool(coustname.winfo_ismapped()) == TRUE:
        c = coustname.get()
    a = str(c)
    # print(a)
    # b = ""
    # if a.startswith("UC") or a.startswith("uc") or a.startswith("nibp") or a.startswith("ecg"):
    #     a = a.upper()
    # else:
    #     a = a.capitalize()
    b = a.lower()
    # print(b)
    search_words = b.split()
    i = 0
    with open("coustomerlistent.txt", "r") as file:
        out = file.readlines()
        lines = map(lambda x: x.lower(), out)
    # key = k.upper()

    for line in lines:
        # if word in key:
        # line.lower()
        # print(line)
        for word in search_words:
            if word in line:
                global buttons
                # print(line)
                buttons = {}

                string_name = f"string1_{i + 1}"  # create a variable name with a unique number
                string_value = f"{line}"  # create the string value
                locals()[string_name] = string_value  # dynamically create the variable and assign the string value
                string_list.append(locals()[string_name])  # add the variable to the list
                button_text = str(locals()[f"string1_{i + 1}"]).upper()  # create the text for the button
                button = ttk.Button(sf, text=button_text, command=lambda button_id=i: get_button_textcnamen(
                    button_id))  # create the button with the text
                button.grid(row=i, column=0, sticky=W, ipadx=10, columnspan=2)  # add the button to the GUI
                buttons[i] = button
                # print(button_text)
                # print(type(button_text))
                cbtnen.update(buttons)

                i += 1
                break
    # print(string_list)
    # top1.config

    cnaen.wm_iconbitmap('favicon.ico')


def cnamserv(self):
    # print(sta)
    global cnaserv
    cnaserv = Toplevel()
    cnaserv.geometry('400x400')
    cnaserv.minsize(400, 400)
    mf = Frame(cnaserv)
    mf.pack(fill=BOTH, expand=1)
    mcan = Canvas(mf)
    mcan.pack(side=LEFT, fill=BOTH, expand=1)
    scrbar = ttk.Scrollbar(mf, orient=VERTICAL, command=mcan.yview)
    scrbar.pack(side=RIGHT, fill=Y)
    mcan.config(yscrollcommand=scrbar.set)
    mcan.bind('<Configure>', lambda e: mcan.config(scrollregion=mcan.bbox('all')))

    sf = Frame(mcan)
    mcan.create_window((0, 0), window=sf, anchor=NW)

    # top1.minsize(500,500)
    string_list = []  # empty list to store the strings

    if bool(mesentry.winfo_ismapped())==TRUE:
        c = mesentry.get()
    elif bool(coustname.winfo_ismapped())==TRUE:
        c=coustname.get()
    a = str(c)
    # print(a)
    # b = ""
    # if a.startswith("UC") or a.startswith("uc") or a.startswith("nibp") or a.startswith("ecg"):
    #     a = a.upper()
    # else:
    #     a = a.capitalize()
    b = a.lower()
    # print(b)
    search_words = b.split()
    i = 0
    with open("coustomerlistserv.txt", "r") as file:
        out = file.readlines()
        lines = map(lambda x: x.lower(), out)
    # key = k.upper()

    for line in lines:
        # if word in key:
        # line.lower()
        # print(line)
        for word in search_words:
            if word in line:
                global buttons
                # print(line)
                buttons = {}

                string_name = f"string1_{i + 1}"  # create a variable name with a unique number
                string_value = f"{line}"  # create the string value
                locals()[string_name] = string_value  # dynamically create the variable and assign the string value
                string_list.append(locals()[string_name])  # add the variable to the list
                button_text = str(locals()[f"string1_{i + 1}"]).upper()  # create the text for the button
                button = ttk.Button(sf, text=button_text, command=lambda button_id=i: get_button_textcnamserv(
                    button_id))  # create the button with the text
                button.grid(row=i, column=0, sticky=W, ipadx=10, columnspan=2)  # add the button to the GUI
                buttons[i] = button
                # print(button_text)
                # print(type(button_text))
                cbtnserv.update(buttons)

                i += 1
                break
    # print(string_list)
    # top1.config

    cnaserv.wm_iconbitmap('favicon.ico')


def to1(self):
    global top1
    top1 = Toplevel()
    top1.geometry('400x400')
    top1.minsize(400, 400)
    mf = Frame(top1)
    mf.pack(fill=BOTH, expand=1)
    mcan = Canvas(mf)
    mcan.pack(side=LEFT, fill=BOTH, expand=1)
    scrbar = ttk.Scrollbar(mf, orient=VERTICAL, command=mcan.yview)
    scrbar.pack(side=RIGHT, fill=Y)
    mcan.config(yscrollcommand=scrbar.set)
    mcan.bind('<Configure>', lambda e: mcan.config(scrollregion=mcan.bbox('all')))

    sf = Frame(mcan)
    mcan.create_window((0, 0), window=sf, anchor=NW)

    # top1.minsize(500,500)
    string_list = []  # empty list to store the strings
    c = desentry1.get()
    a = str(c)
    # print(a)
    b = ""
    if a.startswith("UC") or a.startswith("uc") or a.startswith("nibp") or a.startswith("ecg"):
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
                button = ttk.Button(sf, text=button_text, command=lambda button_id=i: get_button_text1(
                    button_id))  # create the button with the text
                button.grid(row=i, column=0, sticky=W, ipadx=10, columnspan=2)  # add the button to the GUI
                buttons[i] = button
                # print(button)
                ubtn1.update(buttons)

                i += 1
                break
    # print(string_list)
    # top1.config

    top1.wm_iconbitmap('favicon.ico')


def to2(self):
    global top2
    top2 = Toplevel()
    top2.geometry('400x400')
    top2.minsize(400, 400)
    mf2 = Frame(top2)
    mf2.pack(fill=BOTH, expand=1)
    mcan2 = Canvas(mf2)
    mcan2.pack(side=LEFT, fill=BOTH, expand=1)
    scrbar2 = ttk.Scrollbar(mf2, orient=VERTICAL, command=mcan2.yview)
    scrbar2.pack(side=RIGHT, fill=Y)
    mcan2.config(yscrollcommand=scrbar2.set)
    mcan2.bind('<Configure>', lambda e: mcan2.config(scrollregion=mcan2.bbox('all')))
    sf2 = Frame(mcan2)
    mcan2.create_window((0, 0), window=sf2, anchor=NW)
    string_list = []  # empty list to store the strings
    c = desentry2.get()
    a = str(c)
    # print(a)
    b = ""
    if a.startswith("UC") or a.startswith("uc") or a.startswith("nibp") or a.startswith("ecg"):
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
                button = ttk.Button(sf2, text=button_text, command=lambda button_id=i: get_button_text2(
                    button_id))  # create the button with the text
                button.grid(row=i, column=0, columnspan=2, sticky=W, ipadx=10)  # add the button to the GUI
                buttons[i] = button
                # print(button)
                ubtn2.update(buttons)
                i += 1
                # MAKE SEPrATE INPUTS FOr SEPArATE BUTTONS
                break
    # print(string_list)
    top2.wm_iconbitmap('favicon.ico')


def to3(self):
    global top3
    top3 = Toplevel()
    top3.geometry('400x400')
    top3.minsize(400, 400)
    mf3 = Frame(top3)
    mf3.pack(fill=BOTH, expand=1)
    mcan3 = Canvas(mf3)
    mcan3.pack(side=LEFT, fill=BOTH, expand=1)
    scrbar3 = ttk.Scrollbar(mf3, orient=VERTICAL, command=mcan3.yview)
    scrbar3.pack(side=RIGHT, fill=Y)
    mcan3.config(yscrollcommand=scrbar3.set)
    mcan3.bind('<Configure>', lambda e: mcan3.config(scrollregion=mcan3.bbox('all')))
    sf3 = Frame(mcan3)
    mcan3.create_window((0, 0), window=sf3, anchor=NW)
    string_list = []  # empty list to store the strings
    c = desentry3.get()
    a = str(c)
    # print(a)
    b = ""
    if a.startswith("UC") or a.startswith("uc") or a.startswith("nibp") or a.startswith("ecg"):
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
                button = ttk.Button(sf3, text=button_text, command=lambda button_id=i: get_button_text3(
                    button_id))  # create the button with the text
                button.grid(row=i, column=0, columnspan=2, sticky=W, ipadx=10)  # add the button to the GUI
                buttons[i] = button
                # print(button)
                ubtn3.update(buttons)
                i += 1
                break
    # print(string_list)
    top3.wm_iconbitmap('favicon.ico')


def to4(self):
    global top4
    top4 = Toplevel()
    top4.geometry('400x400')
    top4.minsize(400, 400)
    mf4 = Frame(top4)
    mf4.pack(fill=BOTH, expand=1)
    mcan4 = Canvas(mf4)
    mcan4.pack(side=LEFT, fill=BOTH, expand=1)
    scrbar4 = ttk.Scrollbar(mf4, orient=VERTICAL, command=mcan4.yview)
    scrbar4.pack(side=RIGHT, fill=Y)
    mcan4.config(yscrollcommand=scrbar4.set)
    mcan4.bind('<Configure>', lambda e: mcan4.config(scrollregion=mcan4.bbox('all')))
    sf4 = Frame(mcan4)
    mcan4.create_window((0, 0), window=sf4, anchor=NW)
    string_list = []  # empty list to store the strings
    c = desentry4.get()
    a = str(c)
    # print(a)
    b = ""
    if a.startswith("UC") or a.startswith("uc") or a.startswith("nibp") or a.startswith("ecg"):
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
                button = ttk.Button(sf4, text=button_text, command=lambda button_id=i: get_button_text4(
                    button_id))  # create the button with the text
                button.grid(row=i, column=0, columnspan=2, sticky=W, ipadx=10)  # add the button to the GUI
                buttons[i] = button
                # print(button)
                ubtn4.update(buttons)
                i += 1
                break
    # print(string_list)
    top4.wm_iconbitmap('favicon.ico')


# -----------------------------------------------------------------------------funx
# def cnam():
#     b=sta
#     cnamee(b)
# def cnamee(asta):
#     match asta:
#         case 1:
#             cnamen(1)
#         case 2:
#             cnamserv(1)
def cnamecallen():
    cnamen(1)


def cnamecallserv():
    cnamserv(1)


def daten1():
    to1(1)


def daten2():
    to2(1)


def daten3():
    to3(1)


def daten4():
    to4(1)


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
    enter6.grid_forget()
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
    coustname.delete(0, END)
    product.delete(0, END)
    price.delete(0, END)
    pasw.delete(0, END)
    coustname.grid_forget()
    product.grid_forget()
    prdct.grid_forget()
    cust.grid_forget()
    pri.grid_forget()
    price.grid_forget()
    pasw.grid_forget()
    paswl.grid_forget()
    look.grid_forget()
def comclear():
    mes.grid_forget()
    mesentry.grid_forget()
    mesfind.grid_forget()
    srno.grid_forget()
    desc.grid_forget()
    rat.grid_forget()
    gst.grid_forget()
    beof.grid_forget()
    totdata.grid_forget()
    billndata.grid_forget()
    tot.grid_forget()
    billn.grid_forget()
    srn1.grid_forget()
    srn2.grid_forget()
    srn3.grid_forget()
    srn4.grid_forget()
    desentry1.grid_forget()
    find1.grid_forget()
    desentry2.grid_forget()
    find2.grid_forget()
    desentry3.grid_forget()
    find3.grid_forget()
    desentry4.grid_forget()
    find4.grid_forget()
    beofentry.grid_forget()
    rat1.grid_forget()
    rat2.grid_forget()
    rat3.grid_forget()
    rat4.grid_forget()
    qt.grid_forget()
    qt1.grid_forget()
    qt2.grid_forget()
    qt3.grid_forget()
    qt4.grid_forget()
    subbtn.grid_forget()
    gst1.grid_forget()
    gst2.grid_forget()
    gst3.grid_forget()
    gst4.grid_forget()
    gst.grid_forget()

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

def cpfilter(self):
    prin=price.get()
    pr = printInput(prin)[1]
    price.delete(0,END)
    price.insert(0,pr)


# -----------------------------------------------------------------------------page en
def ce():
    mes.grid(row=0, column=0, padx=15, pady=20)
    mesentry.grid(row=0, column=1)
    mesentry.bind("<Return>", cnamen)
    mesfind.grid(row=0, column=2)
    mesfind.config(command=cnamecallen)
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
    mesentry.bind("<Return>", cnamserv)
    mesfind.grid(row=0, column=2)
    mesfind.config(command=cnamecallserv)
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
# -----------------------------------------------------------------------------cplist
def cp():
    root.title('Uni-Card | Customer Price List')
    clear()
    comclear()
    ghost.grid(column=0, row=0, padx=((scw // 2) - 130, 0),rowspan=3)
    paswl.grid(row=4,column=1)
    pasw.grid(row=4,column=2)
    pasw.bind("<Return>",pascheck)
def delpasen():
    pasw.config(show="⭐")
    pasw.delete(0, END)
def pascheck(self):
    passvalue = pasw.get()
    passval="1010"
    if passvalue == passval:
        clear()
        comclear()
        cpp()
    else:
        pasw.delete(0, END)
        pasw.config(show="",font=("Helvetica",12))
        pasw.insert(0, "Wrong Password")
        root.after(1000,delpasen)
        # pasw.config(show="⭐")
        # pasw.delete(0, END)


def cpp():
    cust.grid(row=0, column=0)
    prdct.grid(row=1, column=0)
    pri.grid(row=2, column=0)
    coustname.grid(row=0, column=1)
    coustname.bind("<Return>", cnamserv)
    product.grid(row=1, column=1)
    price.grid(row=2, column=1)
    price.bind("<Return>", cpfilter)
    look.grid(row=3, column=1)

# -----------------------------------------------------------------------------widgets
billndata = ttk.Label(root, text="", width=20, relief='sunken', font=('Arial', 12))
totdata = ttk.Label(root, text="", width=20, relief='sunken', font=('Arial', 12))
mes = Label(root, text='Messers :', font=("Arial", 15), bg="#DDDDDD")
mesenvar = StringVar()
mesentry = ttk.Entry(root, textvariable=mesenvar, width=79, xscrollcommand='-wrapt', font=('Arial', 12))
mesfind = ttk.Button(root, text='Search', width=10)
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
desentry1.bind("<Return>", to1)
find1 = ttk.Button(root, text='Find 1', width=10, command=daten1)
desentry2 = ttk.Entry(root, textvariable=desenvar2, width=85, font=('Arial', 12))
desentry2.bind("<Return>", to2)
find2 = ttk.Button(root, text='Find 2', width=10, command=daten2)
desentry3 = ttk.Entry(root, textvariable=desenvar3, width=85, font=('Arial', 12))
desentry3.bind("<Return>", to3)
find3 = ttk.Button(root, text='Find 3', width=10, command=daten3)
desentry4 = ttk.Entry(root, textvariable=desenvar4, width=85, font=('Arial', 12))
desentry4.bind("<Return>", to4)
find4 = ttk.Button(root, text='Find 4', width=10, command=daten4)
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

coustnamevar = StringVar()
productvar = StringVar()
passvar=StringVar()
cust = Label(root, text='Customer name :', font=("Arial", 15), bg="#DDDDDD")
prdct = Label(root, text='Product :', font=("Arial", 15), bg="#DDDDDD")
pri = Label(root, text='Price :', font=("Arial", 15), bg="#DDDDDD")
coustname = ttk.Entry(root, textvariable=coustnamevar, width=79, xscrollcommand='-wrapt', font=('Arial', 12))
product = ttk.Entry(root, textvariable=productvar, width=79, xscrollcommand='-wrapt', font=('Arial', 12))
price = ttk.Entry(root, width=20, font=('Arial', 12))
look = ttk.Button(root, text='Search', width=20)
adddata = ttk.Button(root, text='➕ Add to list', width=20)
paswl = Label(root, text='Password :', font=("Arial", 15), bg="#DDDDDD")
pasw = ttk.Entry(root,textvariable=passvar, width=20, font=('Arial', 12),show="⭐")


ghost = Label(root, state='disabled', bg='#DDDDDD')
ghost.grid(column=0, row=0, padx=((scw // 2) - 130, 0))
enter1 = ttk.Button(root, text='Enterprises', width=40, command=callent)
enter1.grid(column=1, row=1, pady=10, ipady=10)
enter2 = ttk.Button(root, text='Services', width=40, command=callserv)
enter2.grid(column=1, row=2, pady=10, ipady=10)
enter3 = ttk.Button(root, text='Invoice', width=40)
enter3.grid(column=1, row=3, pady=10, ipady=10)
enter4 = ttk.Button(root, text='Delivery Challan', width=40)
enter4.grid(column=1, row=4, pady=10, ipady=10)
enter5 = ttk.Button(root, text='Recipt', width=40, command=cp)
enter5.grid(column=1, row=5, pady=10, ipady=10)
enter6 = ttk.Button(root, text='Price list', width=40, command=cp)
enter6.grid(column=1, row=6, pady=10, ipady=10)

# -----------------------------------------------------------------------------widgets

# -----------------------------------------------------------------------------menu
men = Menu(root)
submen = Menu(men, tearoff=0)
submen2 = Menu(men, tearoff=0)
submen.add_command(label='Enterprises', command=callent)
submen.add_command(label='Services', command=callserv)
submen.add_command(label='Invoice')
submen.add_command(label='Recipt')
submen.add_command(label='Delivery Challan')
submen2.add_command(label='Price List',command=cp)
men.add_cascade(label='Billing', menu=submen)
men.add_cascade(label='Management', menu=submen2)
root.config(menu=men)
# -----------------------------------------------------------------------------menu

root.attributes('-transparentcolor')
root.state('zoomed')
root.wm_iconbitmap('favicon.ico')
if __name__ == '__main__':
    root.mainloop()
