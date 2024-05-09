'''
MainGUI.py
'''

import tkinter as tk

root=tk.Tk()
value = 0


def plus():
    global value
    value+=1
    print(value)


def minus():
    global value
    value-=1
    print(value)    



# setting the windows size
root.geometry("600x400")

# declaring string variable for storing name and password
name_var=tk.StringVar()


name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))
name_label.grid(row=0,column=0)

# creating a entry for input name using widget Entry
name_entry = tk.Entry(root, textvariable = name_var, font=('calibre',10,'normal'))
name_entry.grid(row=0,column=1)


# performing an infinite loop for the window to display
root.mainloop()





#### top = Frame()
#### top.pack()
#### name_label = Label(top, text = 'Username', font=('calibre',10, 'bold'))
#### widget = Button(top, text = '+', command = plus).pack(side=LEFT)
#### widget = Button(top, text = '-', command = minus).pack(side=RIGHT)
#### widget = Button(top, text = '+', command = plus).pack(side=LEFT)
#### widget = Button(top, text = '-', command = minus).pack(side=RIGHT)
#### top.mainloop()
