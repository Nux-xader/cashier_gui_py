import os
from tkinter import *
from tkinter import messagebox

main = Tk()
main.geometry("1366x768")
main.title("Retail Master")
main.resizable(0, 0)
main.configure(background='black')

def Exit():
    sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=main)
    if sure == True:
        main.destroy()
        
main.protocol("WM_DELETE_WINDOW", Exit)

def emp():
    main.withdraw()
    os.system("python employee.py")
    main.deiconify()


def adm():
    main.withdraw()
    os.system("python admin.py")
    main.deiconify()


label2 = Label(main)
label2.place(relx=0.353, rely=0.275)
label2.configure(text="Welcome to RETAIL MASTER")
label2.configure(font="-family {Poppins} -size 20")
label2.configure(foreground="#ffffff")
label2.configure(background="#000000")

label3 = Label(main)
label3.place(relx=0.390, rely=0.335)
label3.configure(text="Please Choose Login")
label3.configure(font="-family {Poppins} -size 20")
label3.configure(foreground="#ffffff")
label3.configure(background="#000000")

button1 = Button(main)
button1.place(relx=0.316, rely=0.446, width=146, height=90)
button1.configure(relief="flat")
button1.configure(overrelief="flat")
button1.configure(activebackground="#ffffff")
button1.configure(cursor="hand2")
button1.configure(foreground="#ffffff")
button1.configure(background="#ffffff")
button1.configure(borderwidth="0")
img2 = PhotoImage(file="./images/1.png")
button1.configure(image=img2)
button1.configure(command=emp)

button2 = Button(main)
button2.place(relx=0.566, rely=0.448, width=146, height=90)
button2.configure(relief="flat")
button2.configure(overrelief="flat")
button2.configure(activebackground="#ffffff")
button2.configure(cursor="hand2")
button2.configure(foreground="#ffffff")
button2.configure(background="#ffffff")
button2.configure(borderwidth="0")
img3 = PhotoImage(file="./images/2.png")
button2.configure(image=img3)
button2.configure(command=adm)

main.mainloop()
