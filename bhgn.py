import tkinter as tk

def get_button_text(button_id):
    """Function to retrieve text of a button with a given identifier"""
    button_text = buttons[button_id]['text']
    print(f"The text of button {button_id} is: {button_text}")

def create_buttons():
    """Function to create a group of buttons with unique identifiers"""
    global buttons
    buttons = {}
    for i in range(5):
        button = tk.Button(root, text=f"Button {i+1}", command=lambda button_id=i: get_button_text(button_id))
        button.pack()
        buttons[i] = button
    print(buttons)
root = tk.Tk()
create_buttons()
root.mainloop()
