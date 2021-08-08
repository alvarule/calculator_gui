# Creating a Calculator using Tkinter

from tkinter import *


# --------------Actual logic of calculator goes here--------------
def click(event):
    global scvalue

    # Will automatically clear the display if Error is generated in previous calculations
    if display.get() == "Error":
        scvalue.set("")
        display.update()

    # Will extract the value of the clicked button
    text = event.widget.cget("text")

    # if "=" button is clicked, it will evaluate the expression on the display
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            # when the evaluating expression is not valid
            try:
                value = eval(display.get())
            except Exception as e:
                value = "Error"
                print(e)

        # updating the display with the result
        scvalue.set(value)
        display.update()

    # if "C" button is clicked, it will clear the display
    elif text == "C":
        scvalue.set("")
        display.update()

    # if "<-" button is clicked, it will erase the last char of expression on the display
    elif text == "<-":
        scvalue.set(scvalue.get()[:-1])
        display.update()

    # except all above, if any other button is clicked, it will be appended to the expression on the display
    else:
        scvalue.set(scvalue.get() + text)
        display.update()


# --------------Defining the GUI structure--------------
root = Tk()
root.geometry("345x640")
root.minsize(345, 640)
root.maxsize(345, 640)
root.title("Calculator by Atharva")
root.configure(background="black")

scvalue = StringVar()
scvalue.set("")

# Creating main display where i/o will be displayed
display = Entry(root, textvariable=scvalue, font=("times new roman", 35, "bold"),
               justify=RIGHT, bg="black", fg="white", relief=FLAT)
display.pack(side=TOP, fill=X, pady=10, padx=10, ipady=20)

# List of buttons to be placed in the calculator
buttons = [["C", "%", "<-", "/"],
           ["7", "8", "9", "*"],
           ["4", "5", "6", "-"],
           ["1", "2", "3", "+"],
           ["00", "0", ".", "="]]

# creating buttons using for loops and iterating the items in above list
for row in buttons:
    f = Frame(root, bg="black", borderwidth=0)
    f.pack(side=TOP, fill=X, padx=20)
    for btn in row:
        b = Button(f, text=btn, font=("times new roman", 28, "bold"), relief=FLAT,
                   width=3, height=1, pady=15, bg="black", fg="white",
                   activebackground="black", activeforeground="white")
        b.pack(side=LEFT)
        b.bind("<Button-1>", click)

root.mainloop()
