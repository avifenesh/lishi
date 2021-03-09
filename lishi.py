from tkinter import *
from tkinter.ttk import *

# open file for saving orders
f = open("orderList.txt", "w")
f.close()

# made global list for use between the different funcs
orderList = []


# func for save the order the user add to his list
def save_order():
    # use the global list for use data from another func
    global orderList
    # check if empty
    if not orderList:
        return
    cloth = orderList[0]
    size = orderList[1]
    # open the file and save information
    f = open("orderList.txt", "a")  # פתיחת קובץ לשמירת הזמנות
    f.write(cloth + " " + size + "\n")
    f.close()
    # clear the list for next use
    orderList.clear()
    return



# order window
def order():
    # use the global list for use the data in other funcs
    global orderList
    #פתיחת דף חדש
    root1 = Tk()
    #בניית החלון
    root1.title("Order")
    root1.minsize(300, 100)
    root1.geometry("320x200")
    root1.configure(bg='#ffadff')
    #כותרות
    lbl1 = Label(root1, text="Now order whatever you like!")
    lbl1.pack()
    # בחירה מרשימה
    combo=Combobox(root1, state='readonly', values=["choose", "shirt", "pants", "coat", "skirt"])
    combo.current(0)
    combo.pack()
    size=Combobox(root1, state='readonly', values= ["choose", "S", "M", "L", "XL"])
    size.current(0)
    size.pack()
    # every time the user choose something we use lambada func to add the chose the list
    combo.bind("<<ComboboxSelected>>", lambda e: orderList.append(combo.get()))
    size.bind("<<ComboboxSelected>>", lambda d: orderList.append(size.get()))
    # button for save and close
    save = Button(root1, text="Save my order", command=save_order)
    close = Button(root1, text="close", command=root1.destroy)
    save.pack()
    close.pack()

    root1.mainloop()

# window for adding personal details
def personal_details():
    # פתיחת דף חדש
    root2 = Tk()
    # בניית החלון
    root2.title("Personal Details")
    root2.minsize(400, 300)
    root2.geometry("320x200")
    root2.configure(bg='#ffadff')
    # כותרות
    lbl1 = Label(root2, text="please enter your personal details")
    lbl1.pack()
    # adding details
    lbl2 = Label(root2, text="First name")
    fNametext = Entry(root2, width=20)
    lbl3 = Label(root2, text="Family name")
    sNametext = Entry(root2, width=20)
    lbl4 = Label(root2, text="Phone number")
    phonetext = Entry(root2, width=12)
    lbl5 = Label(root2, text="Card number")
    cNumbertext = Entry(root2, width=16)
    rad = Radiobutton(root2, text="male", value=1)
    rad2 = Radiobutton(root2, text="female", value=2)
    # כפתורים לשמירה וסגירה
    close = Button(root2, text="Close page", command=root2.destroy)
    lbl2.pack()
    fNametext.pack()
    lbl3.pack()
    sNametext.pack()
    lbl4.pack()
    phonetext.pack()
    lbl5.pack()
    cNumbertext.pack()
    rad.pack()
    rad2.pack()
    close.pack()
    root2.mainloop()

# window for seeing what in your order
def check_out():
    clothes = ""
    # פתיחת דף חדש
    root3 = Tk()
    # בניית החלון
    root3.title("Check Out")
    root3.minsize(300, 100)
    root3.geometry("320x200")
    root3.configure(bg='#ffadff')
    # כותרות
    lbl1 = Label(root3, text="this is what you ordered")
    lbl1.pack()
    # adding details
    f = open("orderList.txt", "r")
    for x in f:
        clothes += x
        clothes += "\n"
    f.close()
    lbl2 = Label(root3, text=clothes)
    lbl2.pack()
    # close button
    close = Button(root3, text="Close page", command=root3.destroy)
    close.pack()
    root3.mainloop()

# window that offer for specials
def Specials():
    # פתיחת דף חדש
    root4 = Tk()
    # בניית החלון
    root4.title("Specials")
    root4.minsize(300, 100)
    root4.geometry("320x200")
    root4.configure(bg='#ffadff')
    # כותרות
    lbl1 = Label(root4, text="W'anna try our specials?")
    lbl1.pack()
    # creating the check button
    checkSpecial = BooleanVar()
    checkSpecial.set(True)
    chk = Checkbutton(root4, text="give me 10% discount", var=checkSpecial)
    chk.pack()
    # כפתורים לשמירה וסגירה
    close = Button(root4, text="Close page", command=root4.destroy)
    close.pack()
    root4.mainloop()


#חלון ראשי
root=Tk()
# פרטי חלון
root.title("Lishi Clothes")
root.minsize(300, 100)
root.geometry("320x200")
root.configure(bg='#ffcdff')
# כותרות
lbl1=Label(root, text="Welcome to Lishi")
lbl1.pack()
lbl2=Label(root,text="Enjoy!")
lbl2.pack()
#כפתורים לפי סדר 1 - הזמנותת 2 - פרטים אישייםת 3- צ'ק אאוטת 4 - מבצעים
btn1 = Button(root, text="Order Page", command=order)
btn2 = Button(root, text="Personal details", command=personal_details)
btn3 = Button(root, text="Check-Out", command=check_out)
btn4 = Button(root, text="Specials", command=Specials)
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()


root.mainloop()