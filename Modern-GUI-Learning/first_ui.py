import customtkinter as ctk

root = ctk.CTk()
root.title("My First Ui")
root.geometry("400x500")

label = ctk.CTkLabel(root, text="Welcome to CustomTkinter!", font=("Arial", 20, "bold"))
label.pack(pady=20)

root.mainloop()
