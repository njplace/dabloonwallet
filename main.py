import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox


ico = "icon.ico"
mbg = "#c9af2c"
curbal = 0
curitems = {}

db = "db"
items = "items"

with open(db,'r') as f:
    curbal = int(f.read())
    f.close()


with open(items,'r') as f:
    curitems = f.readlines()
    f.close()



window = tk.Tk() #Main window
window.geometry("200x350")
window.title("")
window.iconbitmap(ico)
window['background']="#c9af2c"

def adddb():
    add = simpledialog.askstring("Add Dabloons","How many dabloons would you like to add?",parent=window)
    add = int(add)

    with open(db,'r') as f:
        curbal = int(f.read())
        f.close()
    with open(db,'w') as f:
        newbal = curbal + add
        f.write(str(newbal))
        f.close()
    quit()

def remdb():
    rem = simpledialog.askstring("Remove Dabloons","How many dabloons would you like to remove?",parent=window)
    rem = int(rem)

    with open(db,'r') as f:
        curbal = int(f.read())
        f.close()
    with open(db,'w') as f:
        newbal = curbal - rem
        f.write(str(newbal))
        f.close()
    quit()


def purchase():
    item = simpledialog.askstring("Purchase Item","What item would you like to purchase?",parent=window)
    price = simpledialog.askstring("Purchase Item","How much does this item cost?",parent=window)
    pricei = int(price)

    curitems.append(item + ".." + price + "\n")

    with open(db,'r') as f:
        curbal = int(f.read())
        f.close()
    with open(db,'w') as f:
        newbal = curbal - pricei
        f.write(str(newbal))
        f.close()
    
    with open(items,'w') as f:
        f.writelines(curitems)
    quit()

def sell():
    out = 0
    itemsel = simpledialog.askstring("Sell Item","What item would you like to sell?",parent=window)
    itemprice = simpledialog.askstring("Sell Item","What was the price of " + itemsel + "?")

    comp = itemsel + ".." + itemprice + "\n"

    cur = -1
    for item in curitems:
        cur += 1
        if item == comp:
            out = 1
            curitems.remove(comp)

            with open(db,'r') as f:
                curbal = int(f.read())
                f.close()
            with open(db,'w') as f:
                newbal = curbal + int(itemprice)
                f.write(str(newbal))
                f.close()

            with open(items,"w") as f:
                f.writelines(curitems)
            


        
    if out == 0:
        messagebox.showerror("Sell Item","Item not found.")
    if out == 1:
        quit()


def showItems():
    lis = ""

    for item in curitems:
        item = item.split("..")
        name = item[0]
        price = item[1]

        lis = lis + name + "\n" + price + " DB\n\n"
    
    messagebox.showinfo("Item List","Items: \n" + lis)
    




canvas = tk.Canvas(window,width=200,height=100)
canvas.configure(bg="#c9af2c",borderwidth=0,highlightthickness=0)
canvas.pack()
img = tk.PhotoImage(file="cat.png")
canvas.create_image(55,0,anchor=tk.NW,image=img)

lbl = tk.Label(window,text="Welcome to the Dabloon Bank!\nCurrent Balance: " + str(curbal),background=mbg)
lbl.pack()

Adddbbtn = tk.Button(window,text="Add Dabloons",background="limegreen",command=adddb) #Adds dabloons
Adddbbtn.pack()

Remdbbtn = tk.Button(window,text="Remove Dabloons",background="red",command=remdb) #Removes dabloons
Remdbbtn.pack()

Purchaseitembtn = tk.Button(window,text="Purchase Item",command=purchase) #Purchase
Purchaseitembtn.pack()

Sellitembtn = tk.Button(window,text="Sell Item",command=sell) #Sell
Sellitembtn.pack()

listItems = tk.Button(window,text="Items",command=showItems) #Shows Items
listItems.pack()

q = tk.Button(window,text="Close",background="red",command=quit) #Exit
q.pack()

window.mainloop() #Init