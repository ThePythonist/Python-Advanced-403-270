import tkinter

root = tkinter.Tk()
root.title("My First GUI App")
root.geometry("400x500")
root.resizable(height=False, width=False)
root.configure(bg="#684E6E")

msg = tkinter.Label(root, text="Welcome")
msg.pack()
msg.configure(bg="black", fg="white", font="Impact 16", padx="20", pady="8")

tkinter.mainloop()  # Keep the program running
