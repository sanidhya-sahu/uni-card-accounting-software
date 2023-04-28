while(True):
    string_list = []  # empty list to store the strings
    # c = desentry1.get()
    # a = str(c)
    a=input('=> ')
    # print(a)
    b = ""
    if a.startswith("UC") or a.startswith("uc") or a.startswith("nibp") or a.startswith("ecg"):
        a = a.upper()
    else:
        a = a.lower()
    b = a
    # print(b)
    search_words = b.split()
    i = 0
    with open("coustomerlistent.txt", "r") as file:
        out = file.readlines()
        lines = map(lambda x: x.lower() ,out)
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
                string_value = f"{line}" # create the string value
                locals()[string_name] = string_value  # dynamically create the variable and assign the string value
                string_list.append(locals()[string_name])  # add the variable to the list
                button_text = str(locals()[f"string1_{i + 1}"]).upper()  # create the text for the button
                button = ttk.Button(sf, text=button_text, command=lambda button_id=i: get_button_text1(
                    button_id))  # create the button with the text
                button.grid(row=i, column=0, sticky=W, ipadx=10, columnspan=2)  # add the button to the GUI
                buttons[i] = button
                # print(button_text)
                # print(type(button_text))
                cbtn1.update(buttons)

                i += 1
                break