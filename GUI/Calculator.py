import tkinter as tk

root = tk.Tk()
root.title("CalCulator")


entry = tk.Entry(root)
entry.pack(pady=10)
entry.config(state="normal")

frame = tk.Frame(root,bg="lightgrey",padx=10,pady=10)
frame.pack(padx=20, pady=20)


buttons=[
    ("/",1,0),("*",1,1),("-",1,2),
    ("7",2,0),("8",2,1),("9",2,2),
    ("4",3,0),("5",3,1),("6",3,2),
    ("1",4,0),("2",4,1),("3",4,2),
    ("+",5,0),("0",5,1),("=",5,2),
    ("C",6,1)
]

for text,row,col in buttons:
    btn=tk.Button(frame,text=text,width=5,height=2,command=lambda t=text:button_click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

def button_click(value):
    entry.config(state="normal")
    User_num=entry.get()
    if User_num=="0":
        entry.delete(0,tk.END)
    else:
        entry.insert(tk.END,value)
        entry.config(state="readonly")
            
def Clear():
    entry.config(state="normal")
    entry.delete(0,tk.END)
    entry.insert(0,"0")
    entry.config(state="readonly")

def Calculation():
    try:
        entry.config(state="normal")
        expression = entry.get()
        if "/0" in expression: 
            raise ZeroDivisionError  
        result = eval(expression)  
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
        entry.config(state="readonly")
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Math Error")  
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        
        
for text, row, col in buttons:
    if text == "=":
        btn = tk.Button(frame, text=text, width=5, height=2, command=Calculation)
    elif text == "C":
        btn = tk.Button(frame, text=text, width=5, height=2, command=Clear)
    else:
        btn = tk.Button(frame, text=text, width=5, height=2, command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)
         
    
root.mainloop()