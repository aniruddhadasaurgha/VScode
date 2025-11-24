from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title("Tkinter Widgets Example")
root.geometry("400x400")
upload = Image.open("path_to_your_image.jpg")
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, height = 350, width = 350)
label.place(x = 50, y = 0)
label2 = Label(root, text="This is an example of Tkinter widgets with an image.", font=("Aptos", 12))
label2.place(x = 40, y = 360)
root.mainloop()
