import customtkinter as ctk

root = ctk.CTk()

root.title("Simple Calculater")
root.geometry("450x500")

lbl= ctk.CTkLabel(root,text="Welcome To Alevn x First Ui !",font=("Poppins",20,"bold"))
lbl.pack(pady=20)


lbl2= ctk.CTkLabel(root,text="Calculation .... !",font=("Poppins",15,"bold"))
lbl2.pack(pady=10)


inpu1= ctk.CTkEntry(root,placeholder_text="Enter 1st Number ",font=("Poppins",10,"bold"))
inpu1.pack(pady=20)

inpu2= ctk.CTkEntry(root,placeholder_text="Enter 2nd Number ",font=("Poppins",10,"bold"))
inpu2.pack(pady=5)


def btn_event():
    num1 = inpu1.get()
    num2 = inpu2.get()
    
    try:
        reslut=int(num1)+int(num2)
        print("Click Done")
        lbl2.configure(text=f"Addtion : {reslut}",text_color="blue")
    except ValueError:
        lbl2.configure(text="Error: Please enter numbers!", text_color="red")    
    
btn=ctk.CTkButton(root,text="+",command=btn_event,fg_color="green", hover_color="darkgreen")
btn.pack(pady=5)

def btn2_event():
    num1 = inpu1.get()
    num2 = inpu2.get()
    
    try:
        reslut=int(num1)-int(num2)
        print("Click Done")
        lbl2.configure(text=f"Substraction : {reslut}",text_color="blue")
    except ValueError:
        lbl2.configure(text="Error: Please enter numbers!", text_color="red")    
    
btn=ctk.CTkButton(root,text="-",command=btn2_event,fg_color="green", hover_color="darkgreen")
btn.pack(pady=5)

def btn3_event():
    num1 = inpu1.get()
    num2 = inpu2.get()
    
    try:
        reslut=int(num1)*int(num2)
        print("Click Done")
        lbl2.configure(text=f"Multiplication : {reslut}",text_color="blue")
    except ValueError:
        lbl2.configure(text="Error: Please enter numbers!", text_color="red")    
    
btn=ctk.CTkButton(root,text="*",command=btn3_event,fg_color="green", hover_color="darkgreen")
btn.pack(pady=5)


def btn3_event():
    num1 = inpu1.get()
    num2 = inpu2.get()
    
    try:
        reslut=int(num1)/int(num2)
        print("Click Done")
        lbl2.configure(text=f"Dividation : {reslut}",text_color="blue")
    except ValueError:
        lbl2.configure(text="Error: Please enter numbers!", text_color="red")    
    
btn=ctk.CTkButton(root,text="*",command=btn3_event,fg_color="green", hover_color="darkgreen")
btn.pack(pady=5)







root.mainloop()
