from tkinter import *
from tkinter import ttk
import dataIO


# from home import *
def to1():
    top = Toplevel()
    string_list = []  # empty list to store the strings
    c = dataIO.senddata()[0]
    a=str(c)
    # print(a)
    b = ""
    if a.startswith("UC") or a.startswith("uc") or a.startswith("nibp"):
        a = a.upper()
    else:
        a = a.capitalize()
    b=a
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
                string_name = f"string_{i + 1}"  # create a variable name with a unique number
                string_value = f"{line}"  # create the string value
                locals()[string_name] = string_value  # dynamically create the variable and assign the string value
                string_list.append(locals()[string_name])  # add the variable to the list
                button_text = locals()[f"string1_{i + 1}"]  # create the text for the button
                button = ttk.Button(top, text=button_text)  # create the button with the text
                button.pack()  # add the button to the GUI

                i += 1
                break
    # print(string_list)
def to2():
    top = Toplevel()
    string_list = []  # empty list to store the strings
    c = dataIO.senddata()[1]
    a=str(c)
    # print(a)
    b = ""
    if a.startswith("UC") or a.startswith("uc")or a.startswith("nibp"):
        a = a.upper()
    else:
        a = a.capitalize()
    b=a
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
                string_name = f"string_{i + 1}"  # create a variable name with a unique number
                string_value = f"{line}"  # create the string value
                locals()[string_name] = string_value  # dynamically create the variable and assign the string value
                string_list.append(locals()[string_name])  # add the variable to the list
                button_text = locals()[f"string2_{i + 1}"]  # create the text for the button
                button = ttk.Button(top, text=button_text)  # create the button with the text
                button.pack()  # add the button to the GUI
                i += 1
                # MAKE SEPrATE INPUTS FOr SEPArATE BUTTONS
                break
    # print(string_list)
def to3():
    top = Toplevel()
    string_list = []  # empty list to store the strings
    c = dataIO.senddata()[2]
    a=str(c)
    # print(a)
    b = ""
    if a.startswith("UC") or a.startswith("uc")or a.startswith("nibp"):
        a = a.upper()
    else:
        a = a.capitalize()
    b=a
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
                string_name = f"string_{i + 1}"  # create a variable name with a unique number
                string_value = f"{line}"  # create the string value
                locals()[string_name] = string_value  # dynamically create the variable and assign the string value
                string_list.append(locals()[string_name])  # add the variable to the list
                button_text = locals()[f"string3_{i + 1}"]  # create the text for the button
                button = ttk.Button(top, text=button_text)  # create the button with the text
                button.pack()  # add the button to the GUI
                i += 1
                break
    # print(string_list)
def to4():
    top = Toplevel()
    string_list = []  # empty list to store the strings
    c = dataIO.senddata()[3]
    a=str(c)
    # print(a)
    b = ""
    if a.startswith("UC") or a.startswith("uc")or a.startswith("nibp"):
        a = a.upper()
    else:
        a = a.capitalize()
    b=a
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
                string_name = f"string_{i + 1}"  # create a variable name with a unique number
                string_value = f"{line}"  # create the string value
                locals()[string_name] = string_value  # dynamically create the variable and assign the string value
                string_list.append(locals()[string_name])  # add the variable to the list
                button_text = locals()[f"string4_{i + 1}"]  # create the text for the button
                button = ttk.Button(top, text=button_text)  # create the button with the text
                button.pack()  # add the button to the GUI
                i += 1
                break
    # print(string_list)