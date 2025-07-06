from tkinter import *
from PIL import ImageTk, Image
import os

def rotate_image():
    global counter
    img_label.config(image=img_array[counter%len(img_array)])
    counter = counter + 1

counter = 1
root = Tk()
root.title("Wallpaper viewer")
root.geometry('350x500')
root.config(bg='black')

files = os.listdir('wallpapers')

img_array = []
for file in files:
    img = Image.open(os.path.join('wallpapers',file))
    resized_img = img.resize((600,600))
    img_array.append(ImageTk.PhotoImage(resized_img))

# print(img_array)

img_label = Label(root,image=img_array[0])
img_label.pack(pady=(50,10))

next_btn = Button(root,text="Next", width=20, height=3, bg='black', fg='white', command=rotate_image)
next_btn.pack(pady=(10,2))
next_btn.config(font=('verdena',12))

root.mainloop()
