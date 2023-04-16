from tkinter import *
from tkinter import ttk
import dataIO
ubtn1={}
ubtn2={}
ubtn3={}
ubtn4={}
# button_id=0
def get_button_text1(button_id):
    """Function to retrieve text of a button with a given identifier"""
    # print(ubtn)
    btn_text = ubtn1[button_id]['text']
    print(btn_text)
def get_button_text2(button_id):
    """Function to retrieve text of a button with a given identifier"""
    # print(ubtn)
    btn_text = ubtn2[button_id]['text']
    print(btn_text)
def get_button_text3(button_id):
    """Function to retrieve text of a button with a given identifier"""
    # print(ubtn)
    btn_text = ubtn3[button_id]['text']
    print(btn_text)

def get_button_text4(button_id):
        """Function to retrieve text of a button with a given identifier"""
        # print(ubtn)
        btn_text = ubtn4[button_id]['text']
        print(btn_text)
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
                global buttons
                # print(line)
                buttons = {}

                string_name = f"string1_{i + 1}"  # create a variable name with a unique number
                string_value = f"{line}"  # create the string value
                locals()[string_name] = string_value  # dynamically create the variable and assign the string value
                string_list.append(locals()[string_name])  # add the variable to the list
                button_text = locals()[f"string1_{i + 1}"]  # create the text for the button
                button = ttk.Button(top, text=button_text,command=lambda button_id=i: get_button_text1(button_id))  # create the button with the text
                button.pack()  # add the button to the GUI
                buttons[i] = button
                # print(button)
                ubtn1.update(buttons)
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
                string_name = f"string2_{i + 1}"  # create a variable name with a unique number
                string_value = f"{line}"  # create the string value
                locals()[string_name] = string_value  # dynamically create the variable and assign the string value
                string_list.append(locals()[string_name])  # add the variable to the list
                button_text = locals()[f"string2_{i + 1}"]  # create the text for the button
                button = ttk.Button(top, text=button_text,command=lambda button_id=i: get_button_text2(button_id))  # create the button with the text
                button.pack()  # add the button to the GUI
                buttons[i] = button
                # print(button)
                ubtn2.update(buttons)
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
                button = ttk.Button(top, text=button_text,command=lambda button_id=i: get_button_text3(button_id))  # create the button with the text
                button.pack()  # add the button to the GUI
                buttons[i] = button
                # print(button)
                ubtn3.update(buttons)
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
                button = ttk.Button(top, text=button_text,command=lambda button_id=i: get_button_text4(button_id))  # create the button with the text
                button.pack()  # add the button to the GUI
                buttons[i] = button
                # print(button)
                ubtn4.update(buttons)
                i += 1
                break
    # print(string_list)