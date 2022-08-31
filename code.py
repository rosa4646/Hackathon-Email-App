import yagmail 
from tkinter import *
from tkinter.ttk import *

# yagmail code
yag = yagmail.SMTP("zombiefree12333@gmail.com", 
                    "noZombie4me%&87")
# creates the window
root = Tk()
root.title("futuristic email sending technology braced to survive the zombies")
root.geometry('600x400')
# function to send emails
def func():
   yag.send(emailx, subjectx, contentx)

# text box 
var1=StringVar()
var2=StringVar()
var3=StringVar()
entry1 = Entry(root,textvariable = var1, font=('calibre',10,'normal'), width=70)
entry2 = Entry(root,textvariable = var2, font=('calibre',10,'normal'), width=70)
entry3 = Entry(root,textvariable = var3, font=('calibre',10,'normal'), width=70)
entry1.grid(row=0,column=0)
entry2.grid(row=1,column=0)
entry3.grid(row=2,column=0)

# style :)
style = Style()
style.configure('TButton', font =
               ('x', 10, 'bold', 'underline'),
                foreground = 'purple')
# yeah
def submit():
    global emailx
    global subjectx
    global contentx
    emailx=var1.get()
    subjectx=var2.get()
    contentx=var3.get()
    func()

# creates button
btn1 = Button(root, text = 'Send!',
                command = submit)
btn1.grid(row=3,column=0)

# makes the window/gui
root.mainloop()
