from tkinter import*
import time
import punchtime


# Window for the software
root = Tk()
root.geometry("1000x500+0+0")
root.title("Maintenance Training Time")

text_Input = StringVar()
operator = ""

Tops = Frame(root, width=800, bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=400, height=700, relief=SUNKEN)
f1.pack(side=TOP)

f2 = Frame(root, width=400, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

# =========================================Time========================================================
localtime = time.asctime(time.localtime(time.time()))

# ========================================Info=======================================================
lblInfo = Label(Tops, font=('arial', 30, 'bold'), text="Welcome to Maintenance Training", fg="Steel Blue", bd=10,
                anchor='w')
lblInfo.grid(row=0, column=0)
clock = Label(Tops, font=('arial', 15, 'bold'), text=localtime, fg="Steel Blue", bd=10,
              anchor='w')
clock.grid(row=1, column=0)


def qExit():
    root.destroy()


# ==============================================Restaurant Info 1=====================================================
rand = StringVar()
Fries = StringVar()
Burger = StringVar()
Fillet = StringVar()
SubTotal = StringVar()
Total = StringVar()
Service = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
Chicken_Burger = StringVar()
Cheese_Burger = StringVar()

lblReference = Label(f1, font=('arial', 16, 'bold'), text="TM Name", bd=16, anchor='w')
lblReference.grid(row=0, column=0)
txtReference = Entry(f1, font=('arial', 16, 'bold'), textvariable=rand, bd=10, insertwidth=4,
                     bg="#ffffff", justify='right')
txtReference.grid(row=0, column=1)

lblFries = Label(f1, font=('arial', 16, 'bold'), text="TM Personnel Number", bd=16, anchor='w')
lblFries.grid(row=1, column=0)
txtFries = Entry(f1, font=('arial', 16, 'bold'), textvariable=Fries, bd=10, insertwidth=4,
                 bg="#ffffff", justify='right')
txtFries.grid(row=1, column=1)

lblBurger = Label(f1, font=('arial', 16, 'bold'), text="Crew Number", bd=16, anchor='w')
lblBurger.grid(row=2, column=0)
txtBurger = Entry(f1, font=('arial', 16, 'bold'), textvariable=Burger, bd=10, insertwidth=4,
                 bg="#ffffff", justify='right')
txtBurger.grid(row=2, column=1)

lblFillet = Label(f1, font=('arial', 16, 'bold'), text="Supervisor Name", bd=16, anchor='w')
lblFillet.grid(row=3, column=0)
txtFillet = Entry(f1, font=('arial', 16, 'bold'), textvariable=Fillet, bd=10, insertwidth=4,
                 bg="#ffffff", justify='right')
txtFillet.grid(row=3, column=1)

lblChicken = Label(f1, font=('arial', 16, 'bold'), text="TM Level", bd=16, anchor='w')
lblChicken.grid(row=4, column=0)
txtChicken = Entry(f1, font=('arial', 16, 'bold'), textvariable=Chicken_Burger, bd=10, insertwidth=4,
                 bg="#ffffff", justify='right')
txtChicken.grid(row=4, column=1)

lblCheese = Label(f1, font=('arial', 16, 'bold'), text="Cheese Meal", bd=16, anchor='w')
lblCheese.grid(row=5, column=0)
txtCheese = Entry(f1, font=('arial', 16, 'bold'), textvariable=Cheese_Burger, bd=10, insertwidth=4,
                 bg="#ffffff", justify='right')
txtCheese.grid(row=5, column=1)


# ==============================================Restaurant Info 2=====================================================

lblDrinks = Label(f1, font=('arial', 16, 'bold'), text="Drinks", bd=16, anchor='w')
lblDrinks.grid(row=0, column=2)
txtDrinks = Entry(f1, font=('arial', 16, 'bold'), textvariable=Drinks, bd=10, insertwidth=4,
                     bg="#ffffff", justify='right')
txtDrinks.grid(row=0, column=3)

lblCost = Label(f1, font=('arial', 16, 'bold'), text="Cost of Meal", bd=16, anchor='w')
lblCost.grid(row=1, column=2)
txtCost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Cost, bd=10, insertwidth=4,
                 bg="#ffffff", justify='right')
txtCost.grid(row=1, column=3)

lblService = Label(f1, font=('arial', 16, 'bold'), text="Service Charge", bd=16, anchor='w')
lblService.grid(row=2, column=2)
txtService = Entry(f1, font=('arial', 16, 'bold'), textvariable=Service, bd=10, insertwidth=4,
                 bg="#ffffff", justify='right')
txtService.grid(row=2, column=3)

lblStateTax = Label(f1, font=('arial', 16, 'bold'), text="State Tax", bd=16, anchor='w')
lblStateTax.grid(row=3, column=2)
txtStateTax = Entry(f1, font=('arial', 16, 'bold'), textvariable=Tax, bd=10, insertwidth=4,
                 bg="#ffffff", justify='right')
txtStateTax.grid(row=3, column=3)

lblSubTotal = Label(f1, font=('arial', 16, 'bold'), text="Sub Total", bd=16, anchor='w')
lblSubTotal.grid(row=4, column=2)
txtSubTotal = Entry(f1, font=('arial', 16, 'bold'), textvariable=SubTotal, bd=10, insertwidth=4,
                 bg="#ffffff", justify='right')
txtSubTotal.grid(row=4, column=3)

lblTotalCost = Label(f1, font=('arial', 16, 'bold'), text="Total Cost", bd=16, anchor='w')
lblTotalCost.grid(row=5, column=2)
txtTotalCost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Total, bd=10, insertwidth=4,
                 bg="#ffffff", justify='right')
txtTotalCost.grid(row=5, column=3)



mainloop()