from tkinter import *
import json
from tkinter.filedialog import asksaveasfile
window = Tk()
window.geometry('640x300')
window.title('إدخال معلمات الطائرة')

name = Label(window, text="درجة الحرارة:")
Name = Entry(window)
age = Label(window, text="الإرتفاع:")
Age = Entry(window)
def check():
    a = Name.get()
    b = test * int(Age.get())
    c = Role.get()
    print(a)
    print(b)
    print(c)
    data = {}
    data['Temperature degree'] = a
    data['the height'] = b
    data['landing gear light'] = c
    files = [('agent', '*.json')]
    fileName = 'Agent.json'
    filepos = asksaveasfile(filetypes=files, defaultextension=json, initialfile='IOTEDU')
    writeToJSONFile(filepos, fileName, data)
role = Label(window, text="نظام الإطارات:")
Role = Entry(window)
submit = Button(window, text='إضافة', bg="green",command =check).grid(row=3, column=1)
submit=Button(window,text="خروج",bg="red",command=exit).grid(row=3, column=2)



test = 1


def writeToJSONFile(path, fileName, data):
    json.dump(data, path)


path = './'
name.grid(row=0, column=0)
age.grid(row=1, column=0)
role.grid(row=2, column=0)
Name.grid(row=0, column=1)
Age.grid(row=1, column=1)
Role.grid(row=2, column=1)

mainloop()