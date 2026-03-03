import tkinter as tk

q = ""
prob = []
l = ["x","-", "+","÷",".","%"]
history = {}

def kill(p):
    global q
    if p in l:
        print(f"p = {p}")
        try:
            then = prob[-1]
            if p == then or then in l:
                print(f"p = {p}", f"then = {then}")
                return
        except IndexError:
            p = p
    prob.append(p)
    
def update_bar(p):
    kill(p)
    que = ""
    for i in prob:
        que += str(i)
    q = que
    print(q)
    print("length:", len(q))
    print(prob)
    display_bar.config(text=f"{q}\n")

def c(eq=None):
    global q
    prob.clear()
    print("Clear")
    q = ""
    if eq == None:
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
    #print(q)
    #print(len(q))
    display_bar.config(text=f"{q}\n")

def change(num):
    print("changing")
    print(num, type(num))
    t = type(num)
    if t == float:
        print("float")
        if num.is_integer():
            ans = int(num)
        else:
            ans = num
    else:
        ans = num
    return ans

def sub_op(ls):
    p =""
    for i in ls:
        if i == "x":
            p += "*"
        elif i == "÷":
            p += "/"
        else:
            p += str(i)
    return p

def ans():
    print(prob)
    p= sub_op(prob)
    q = ""
    for i in prob:
        q += str(i)
    print(p)
    value = eval(p)
    print(type(value))
    ans = change(value)
    print(ans)
    print(f"q is ....{q}")
    display_bar.config(text=f"{q}\n{ans}")
    c(True)
    
#changing modes
def calc():
    mode(number_mode)
def binary_calc():
    mode(binary_mode)
def hexadecimal():
    mode(hex_mode)
    
#calculating bin and hex
def get_bin():
    q=""
    op = []
    print(op)
    for i in prob:
        op.append(True) if i in l else(op.append (False))
        q+= str(i)
    print(prob, "to convert to bin")
    print(q)
    print(op)
    qu = sub_op(prob)
    if True in op:
        ans = eval(qu)
        print(f"ans == {ans}")
        result = bin(int(ans))
    else:
        result = bin(int(q))
        
    b = str(result)[2:]
    c(True)
    display_bar.config(text=f"{q}\n{b}")
    
def get_hex():
    q=""
    op = []
    print(op)
    for i in prob:
        op.append(True) if i in l else(op.append (False))
        q+= str(i)
    print(prob, "to convert to bin")
    print(q)
    print(op)
    qu = sub_op(prob)
    if True in op:
        ans = eval(qu)
        print(f"ans == {ans}")
        result = hex(int(ans))
    else:
        result = hex(int(q))
        
    b = str(result)[2:]
    print(result, b)
    c(True)
    display_bar.config(text=f"{q}\n{b}")
    
def mode(mode):
    for item in mode:
    # We use a default argument (v=item["val"]) in lambda to capture the current value
        btn = tk.Button(root, text=item["text"], width=10, height=2,
                        command=lambda v=item["val"], t=item["func"]: 
                        update_bar(v) if t == "update" else (
                        c() if t == "clear" else (
                        remove() if t == "remove" else (
                        ans() if t == "ans" else(
                        binary_calc()if t == "binary_calc" else (
                        calc() if t == "calc" else (
                        hexadecimal() if t == "hex" else (
                        get_bin() if t =="get_bin" else (
                        get_hex() if t == "get_hex" else None)))))))))
        btn.grid(row=item["row"], column=item["col"], padx=10, pady=10)

root = tk.Tk()
root.title("Calculator")


#root.geometry("370x350") #w*h
#root.minsize(370,350)
#root.maxsize(370,350)
# updatebar, sum, remove, c

number_mode = [
    {"text": "Clear", "row": 2, "col": 0, "val": None, "func":"clear"}, 
    {"text": "Bin", "row": 2, "col": 1, "val": None, "func":"binary_calc"},
    {"text": "Hex", "row": 2, "col": 2, "val": None, "func":"hex"},
    {"text": "⌫", "row": 2, "col": 3, "val": None, "func":"remove"},
    {"text": "1", "row": 4, "col": 0, "val": 1, "func":"update"},
    {"text": "2", "row": 4, "col": 1, "val": 2, "func":"update"},
    {"text": "3", "row": 4, "col": 2, "val": 3, "func":"update"},
    {"text": "÷", "row": 4, "col": 3, "val": "÷", "func":"update"},
    {"text": "4", "row": 5, "col": 0, "val": 4, "func":"update"},
    {"text": "5", "row": 5, "col": 1, "val": 5, "func":"update"},
    {"text": "6", "row": 5, "col": 2, "val": 6, "func":"update"},
    {"text": "x", "row": 5, "col": 3, "val": "x", "func":"update"}, 
    {"text": "7", "row": 6, "col": 0, "val": 7, "func":"update"},
    {"text": "8", "row": 6, "col": 1, "val": 8, "func":"update"},
    {"text": "9", "row": 6, "col": 2, "val": 9, "func":"update"},
    {"text": "-", "row": 6, "col": 3, "val": "-", "func":"update"},
    {"text": ".", "row": 7, "col": 0, "val": ".", "func":"update"},
    {"text": "0", "row": 7, "col": 1, "val": 0, "func":"update"},
    {"text": "=", "row": 7, "col": 2, "val": "=", "func":"ans"},
    {"text": "-", "row": 7, "col": 3, "val": "-", "func":"update"},
]

binary_mode = [
    {"text": "Clear", "row": 2, "col": 0, "val": None, "func":"clear"}, 
    {"text": "Calc", "row": 2, "col": 1, "val": None, "func":"calc"},
    {"text": "Hex", "row": 2, "col": 2, "val": None, "func":"hex"},
    {"text": "⌫", "row": 2, "col": 3, "val": None, "func":"remove"},
    {"text": "1", "row": 4, "col": 0, "val": 1, "func":"update"},
    {"text": "2", "row": 4, "col": 1, "val": 2, "func":"update"},
    {"text": "3", "row": 4, "col": 2, "val": 3, "func":"update"},
    {"text": "÷", "row": 4, "col": 3, "val": "÷", "func":"update"},
    {"text": "4", "row": 5, "col": 0, "val": 4, "func":"update"},
    {"text": "5", "row": 5, "col": 1, "val": 5, "func":"update"},
    {"text": "6", "row": 5, "col": 2, "val": 6, "func":"update"},
    {"text": "x", "row": 5, "col": 3, "val": "x", "func":"update"}, 
    {"text": "7", "row": 6, "col": 0, "val": 7, "func":"update"},
    {"text": "8", "row": 6, "col": 1, "val": 8, "func":"update"},
    {"text": "9", "row": 6, "col": 2, "val": 9, "func":"update"},
    {"text": "-", "row": 6, "col": 3, "val": "-", "func":"update"},
    {"text": ".", "row": 7, "col": 0, "val": ".", "func":"update"},
    {"text": "0", "row": 7, "col": 1, "val": 0, "func":"update"},
    {"text": "Convert", "row": 7, "col": 2, "val": None, "func":"get_bin"},
    {"text": "-", "row": 7, "col": 3, "val": "-", "func":"update"},
]

hex_mode = [
    {"text": "Clear", "row": 2, "col": 0, "val": None, "func":"clear"}, 
    {"text": "Bin", "row": 2, "col": 1, "val": None, "func":"binary_calc"},
    {"text": "Calc", "row": 2, "col": 2, "val": None, "func":"calc"},
    {"text": "⌫", "row": 2, "col": 3, "val": None, "func":"remove"},
    {"text": "1", "row": 4, "col": 0, "val": 1, "func":"update"},
    {"text": "2", "row": 4, "col": 1, "val": 2, "func":"update"},
    {"text": "3", "row": 4, "col": 2, "val": 3, "func":"update"},
    {"text": "÷", "row": 4, "col": 3, "val": "÷", "func":"update"},
    {"text": "4", "row": 5, "col": 0, "val": 4, "func":"update"},
    {"text": "5", "row": 5, "col": 1, "val": 5, "func":"update"},
    {"text": "6", "row": 5, "col": 2, "val": 6, "func":"update"},
    {"text": "x", "row": 5, "col": 3, "val": "x", "func":"update"}, 
    {"text": "7", "row": 6, "col": 0, "val": 7, "func":"update"},
    {"text": "8", "row": 6, "col": 1, "val": 8, "func":"update"},
    {"text": "9", "row": 6, "col": 2, "val": 9, "func":"update"},
    {"text": "-", "row": 6, "col": 3, "val": "-", "func":"update"},
    {"text": ".", "row": 7, "col": 0, "val": ".", "func":"update"},
    {"text": "0", "row": 7, "col": 1, "val": 0, "func":"update"},
    {"text": "Convert", "row": 7, "col": 2, "val": None, "func":"get_hex"},
    {"text": "-", "row": 7, "col": 3, "val": "-", "func":"update"},
]

#label = tk.Label(text="Calculator")
#label.grid(row=0, column =1)

# Create the display bar with a border/relief to look like a bar
display_bar = tk.Label(root, relief="sunken", width=10,height=2, justify="right",anchor="e")
display_bar.grid(row=1, column=0, columnspan=4, sticky="we", padx=10, pady=10)

line = tk.Frame(root, height=2, bd=0, bg="black")
line.grid(row=3, column=0, columnspan=4, sticky="ew", padx=5, pady=5)

mode(number_mode)

root.mainloop()
