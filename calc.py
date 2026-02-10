import tkinter as tk

prob = []

def update_bar(p):
    l = ["x","-", "+","÷",".","%"]
    if p in l:
        print(f"p = {p}")
        try:
            then = prob[-1]
            if p == then or then in l:
                print(f"p = {p}", f"then = {then}")
                return
        except IndexError:
            p = p
        
    q = ""
    prob.append(p)
    print(prob)
    for i in prob:
        q += str(i)
    print(q)
    print(len(q))
    display_bar.config(text=f"{q}\n")

def c():
    prob.clear()
    print("Clear")
    display_bar.config(text="\n")

def remove():
    length = len(prob)
    last = length-1
    try:
        prob.pop()
    except IndexError:
        pass
    q= ""
    for i in prob:
        q += str(i)
    print(q)
    print(len(q))
    display_bar.config(text=f"{q}\n")

def sum(s):
    right = ""
    left = ""
    op = ""
    for i in prob:
        right =+ 
    print("sum")

root = tk.Tk()
root.title("Calculator")


#root.geometry("370x350") #w*h
#root.minsize(370,350)
#root.maxsize(370,350)

label = tk.Label(text="Calculator")
label.grid(row=0, column =1)

# Create the display bar with a border/relief to look like a bar
display_bar = tk.Label(root, relief="sunken", width=10,height=2, justify="right",anchor="e")
display_bar.grid(row=1, column=0, columnspan=4, sticky="we", padx=10, pady=10)

clear = tk.Button(text="C", width=5, height=2,command=lambda:c())
clear.grid(row=2, column=0, padx=10, pady=10)

percent = tk.Button(text="%", width=5, height=2,command=lambda:update_bar("%"))
percent.grid(row=2, column=2, padx=10, pady=10)

back = tk.Button(text="⌫", width=5, height=2,command=lambda:remove())
back.grid(row=2, column=3, padx=10, pady=10)

line = tk.Frame(root, height=2, bd=0, bg="black")
line.grid(row=3, column=0, columnspan=4, sticky="ew", padx=5, pady=5)

#Buttons
button = tk.Button(text="1", width=10, height=2,command=lambda:update_bar(1))
button.grid(row=4, column=0, padx=10, pady=10)

button = tk.Button(text="4", width=10, height=2,command=lambda:update_bar(4))
button.grid(row=5, column=0, padx=10, pady=10)

button = tk.Button(text="7",width=10, height=2, command=lambda:update_bar(7))
button.grid(row=6, column=0, padx=10, pady=10)

button = tk.Button(text="2", width=10, height=2,command=lambda: update_bar(2))
button.grid(row=4, column=1, padx=10, pady=10)

button = tk.Button(text="5", width=10, height=2, command=lambda: update_bar(5))
button.grid(row=5, column=1, padx=10, pady=10)

button = tk.Button(text="8",width=10, height=2, command=lambda: update_bar(8))
button.grid(row=6, column=1, padx=10, pady=10)

button = tk.Button(text="3", width=10, height=2, command=lambda: update_bar(3))
button.grid(row=4, column=2, padx=10, pady=10)

button = tk.Button(text="6", width=10, height=2, command=lambda: update_bar(6))
button.grid(row=5, column=2, padx=10, pady=10)

button = tk.Button(text="9", width=10, height=2, command=lambda: update_bar(9))
button.grid(row=6, column=2, padx=10, pady=10)

button = tk.Button(text="0", width=10, height=2, command=lambda: update_bar(0))
button.grid(row=7, column=1, padx=10, pady=10)

button = tk.Button(text="÷", width=5, height=2,command=lambda:update_bar("÷"))
button.grid(row=4, column=3, padx=10, pady=10)

button = tk.Button(text="x", width=5, height=2,command=lambda:update_bar("x"))
button.grid(row=5, column=3, padx=10, pady=10)

button = tk.Button(text="-", width=5, height=2,command=lambda:update_bar("-"))
button.grid(row=6, column=3, padx=10, pady=10)

button = tk.Button(text="+", width=5, height=2,command=lambda:update_bar("+"))
button.grid(row=7, column=3, padx=10, pady=10)

button = tk.Button(text="=", width=5, height=2,command=lambda:sum("="))
button.grid(row=7, column=2, padx=10, pady=10)

button = tk.Button(text=".", width=5, height=2,command=lambda:update_bar("."))
button.grid(row=7, column=0, padx=10, pady=10)

root.mainloop()
