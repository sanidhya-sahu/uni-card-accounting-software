
from inpfilter import *
from tkinter import *
from tkinter import ttk
import ckbc
import dataIO
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


# -----------------------------------------------------------------------------funx
def find1():
    d1=desentry1.get()
    dataIO.takeentry(d1,None,None,None)
    ckbc.to1()
def find2():
    d2=desentry2.get()
    dataIO.takeentry(None,d2,None,None)
    ckbc.to2()
def find3():
    d3=desentry3.get()
    dataIO.takeentry(None, None, d3, None)
    ckbc.to3()
def find4():
    d4=desentry4.get()
    dataIO.takeentry(None, None, None, d4)
    ckbc.to3()
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
    se = (r1 + ((r1 * g1) / 100) + r2 + ((r2 * g2) / 100) + r3 + ((r3 * g3) / 100) + r4 + ((r4 * g4) / 100))
    totdata.config(text=se)


def sscal():
    ratin1 = rat1.get(0, END)
    ratin2 = rat2.get(0, END)
    ratin3 = rat3.get(0, END)
    ratin4 = rat4.get(0, END)
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
    ss = (r1 + r2 + r3 + r4)
    totdata.config(text=ss)


def clear():
    rat1.delete(0, END)
    rat2.delete(0, END)
    rat3.delete(0, END)
    rat4.delete(0, END)
    desentry1.delete(0, END)
    desentry2.delete(0, END)
    desentry3.delete(0, END)
    desentry4.delete(0, END)


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


# -----------------------------------------------------------------------------funx

# -----------------------------------------------------------------------------page en
def ce():
    mes.grid(row=0, column=0, padx=15, pady=20)
    mesentry.grid(row=0, column=1)
    srno.grid(row=1, column=0, padx=15, pady=20)
    desc.grid(row=1, column=1, padx=15, pady=20)
    rat.grid(row=1, column=3, padx=15, pady=20)
    gst.grid(row=1, column=4, padx=15, pady=20)
    beof.grid(row=6, column=0, padx=15, pady=20)
    totdata.grid(row=6, column=3, columnspan=2)
    billndata.grid(row=0, column=3, columnspan=2)
    tot.grid(row=6, column=3, padx=15, pady=20)
    billn.grid(row=0, column=3, padx=15, pady=20)
    srn1.grid(row=r, column=0, padx=15, pady=20)
    srn2.grid(row=r + 1, column=0, padx=15, pady=20)
    srn3.grid(row=r + 2, column=0, padx=15, pady=20)
    srn4.grid(row=r + 3, column=0, padx=15, pady=20)
    desentry1.grid(row=2, column=1, columnspan=2)
    find1.grid(row=2,column=1,rowspan=2,sticky="w")
    desentry2.grid(row=3, column=1, columnspan=2)
    find2.grid(row=3,column=1,rowspan=2,sticky="w")
    desentry3.grid(row=4, column=1, columnspan=2)
    find3.grid(row=4,column=1,rowspan=2,sticky="w")
    desentry4.grid(row=5, column=1, columnspan=2)
    find4.grid(row=5, column=1,rowspan=2,sticky="w")
    beofentry.grid(row=7, column=1, columnspan=2)
    rat1.grid(row=2, column=3)
    # rat1.unbind("<Return>")
    rat2.grid(row=3, column=3)
    rat3.grid(row=4, column=3)
    rat4.grid(row=5, column=3)
    subbtn.grid(row=7, column=3, columnspan=2)
    global se, r1, r2, r3, r4, g1, g2, g3, g4, ratin1, ratin2, ratin3, ratin4, gstin1, gstin2, gstin3, gstin4

    gst1.grid(row=2, column=4)
    gst2.grid(row=3, column=4)
    gst3.grid(row=4, column=4)
    gst4.grid(row=5, column=4)
    gst.grid(row=1, column=4, padx=15, pady=20)
    subbtn.config(command=totupdate_supply)


# -----------------------------------------------------------------------------page en

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
    desentry1.grid(row=2, column=1, columnspan=2)
    desentry2.grid(row=3, column=1, columnspan=2)
    desentry3.grid(row=4, column=1, columnspan=2)
    desentry4.grid(row=5, column=1, columnspan=2)
    beofentry.grid(row=6, column=1, columnspan=2)
    rat1.grid(row=2, column=3)
    rat2.grid(row=3, column=3)
    rat3.grid(row=4, column=3)
    rat4.grid(row=5, column=3)
    subbtn.grid(row=7, column=3, padx=15, pady=20)

    gst1.grid_forget()
    gst2.grid_forget()
    gst3.grid_forget()
    gst4.grid_forget()
    gst.grid_forget()

    # subbtn.config(command=totupdate)


# -----------------------------------------------------------------------------page serv

# -----------------------------------------------------------------------------widgets
billndata = ttk.Label(root, text="", width=20, relief='sunken', font=('Arial', 12))
global totdata
totdata = ttk.Label(root, text="", width=20, relief='sunken', font=('Arial', 12))
mes = Label(root, text='Messers :', font=("Arial", 15), bg="#DDDDDD")
mesenvar = StringVar()
mesentry = ttk.Entry(root, textvariable=mesenvar, width=90, xscrollcommand='-wrapt',font=('Arial', 12))
global gst
srno = Label(root, text='Sr no.', font=("Arial", 15), bg="#DDDDDD")
desc = Label(root, text='Description', font=("Arial", 15), bg="#DDDDDD")
rat = Label(root, text='Rate', font=("Arial", 15), bg="#DDDDDD", padx=90)
gst = Label(root, text='% GST', font=("Arial", 15), bg="#DDDDDD", padx=90)
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
desentry1 = ttk.Entry(root, textvariable=desenvar1, width=90, font=('Arial', 12))
find1 =ttk.Button(root, text='Find1', width=10,command=find1)
desentry2 = ttk.Entry(root, textvariable=desenvar2, width=90, font=('Arial', 12))
find2 =ttk.Button(root, text='Find2', width=10,command=find2)
desentry3 = ttk.Entry(root, textvariable=desenvar3, width=90, font=('Arial', 12))
find3 =ttk.Button(root, text='Find3', width=10,command=find3)
desentry4 = ttk.Entry(root, textvariable=desenvar4, width=90, font=('Arial', 12))
find4 =ttk.Button(root, text='Find4', width=10,command=find4)
beofentry = ttk.Entry(root, textvariable=beofenvar, width=90, font=('Arial', 12))
beoff = beofenvar.get()

global rat1, rat2, rat3, rat4, gst1, gst2, gst3, gst4
rat1 = ttk.Entry(root, width=20, font=('Arial', 12))
rat2 = ttk.Entry(root, width=20, font=('Arial', 12))
rat3 = ttk.Entry(root, width=20, font=('Arial', 12))
rat4 = ttk.Entry(root, width=20, font=('Arial', 12))
gst1 = ttk.Entry(root, width=20, font=('Arial', 12))
# gst1.grid(row=2, column=4)
gst2 = ttk.Entry(root, width=20, font=('Arial', 12))
# gst2.grid(row=3, column=4)
gst3 = ttk.Entry(root, width=20, font=('Arial', 12))
# gst3.grid(row=4, column=4)
gst4 = ttk.Entry(root, width=20, font=('Arial', 12))
# gst4.grid(row=5, column=4)
rat1.bind("<Return>",totupdate)
# rat2.bind("<Return>",totupdate)
# rat3.bind("<Return>",totupdate)
# rat4.bind("<Return>",totupdate)
# gst1.bind("<Return>",totupdate)
# gst2.bind("<Return>",totupdate)
# gst3.bind("<Return>",totupdate)
# gst4.bind("<Return>",totupdate)
subbtn =ttk.Button(root, text='Calculate', width=20)
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
