import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('kdd')

root.geometry('800x800-100+100')

# width = root.winfo_screenwidth()
# height = root.winfo_screenheight()
# w, h = 500, 500
# print(f'{width} + {height}')
# widget(container, **options)
# message.pack()
# root.minsize(300, 500)
# root.maxsize(600, 600)

# transparent
root.attributes('-alpha', 1)
# put the window at the top of the stacking order
root.attributes('-topmost', 1)
# resize(bool, bool)
root.resizable(1, 1)

# root1 = tk.Tk()
# root1.title('kdd1')
# root1.geometry('200x150+30+30')
# root1.lower()
# only available on .ico


# tk.Label(root, text="hello1").pack()
# ttk.Label(root, text="hello2").pack()


# label_dic = ttk.Label(root)
# label_dic['text'] = "It is a test."
# label_dic.pack()

def button_clicked():
    print("clicked")


def select(option):
    print(option)


def printOUT():
    ttk.Label(root, text="command").pack()


def return_pressed(event):
    print('Return key pressed.')


def log(event):
    print(event)


# label = ttk.Label(root)
# label.config(text="hello3")
# label.pack()

# command no ()
# button0 = ttk.Button(root, text="hello4", command=printOUT)
# button0.pack()

# btn = ttk.Button(root, text='Save')
# btn.bind('<Return>', return_pressed)
# btn.bind('<Alt_L>', log, add='+')
# btn.focus()
# btn.pack(expand=True)

# text = tk.StringVar()
# textbox = ttk.Entry(root, textvariable=text)
# textbox.pack()
# text.get()
# ttk.Label(root,text='hello world', font=('hack',)).pack(ipadx=10,ipady=10)

img1 = tk.PhotoImage(file='./assets/logo.png')
img_label = ttk.Label(root,
                      image=img1,
                      text='logo',
                      compound='top')
img_label.pack()

btn = ttk.Button(root,
                 text='exit!',
                 command=lambda: root.quit()).pack()

root.mainloop()
# root1.mainloop()
