from tkinter import *

root = Tk()
root.title("My Programme")
root.geometry('200x300')

def function():
  pass

lbl_show_hello = Label(
  root,
  text = "Hello, World!",
  bg = 'red',
  rg = 'black'
).pack() # you can use grid to have indexable page

btn = Button(
  root,
  text = "Click Me!"
  command = function
).pack()

root.mainloop()
