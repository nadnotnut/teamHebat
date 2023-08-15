import tensorflow as tf
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo

def predictThis(folder_path):
  from keras.models import load_model
  import numpy as np
  from keras.utils import load_img, img_to_array
  from numpy import argmax

  model = tf.keras.models.load_model('C:/Users/ADMIN/Documents/CSC583/Python AI/Mushroom/saved_model/my_model')
  img_width = 150
  img_height = 150
  mushroom = {0:"Amanita bisporigera", 1:"Amanita muscaria", 2:"Boletus edulis", 3:"Cantharellus", 4:"Enoki mushroom", 5:"Russula mariae"}

  img = load_img(folder_path, target_size=(300,300))     
  x = img_to_array(img)
  test_image = np.expand_dims(x,axis=0)
  result = model.predict(test_image)

  category_result = argmax(result)

  return mushroom[category_result]   


#allow user to select a directory
def browse_button():
  global img_path
  filename = filedialog.askopenfilename(title = "Select file",filetypes = [("JPG Files", "*.jpg")])
  img_path.set(filename)
  im = Image.open(filename)
  im = im.resize((300,300), Image.Resampling.LANCZOS)
  tkimage = ImageTk.PhotoImage(im)
  myvar.configure(image=tkimage)
  myvar.image=tkimage

  result = predictThis(filename)

  if result == 'Amanita bisporigera':
     lblresult['text'] = "It is Amanita bisporigera - Dangerous and not safe to eat! "
  elif result == 'Amanita muscaria':
     lblresult['text'] = "It is Amanita muscaria - Dangerous and not safe to eat! "
  elif result == 'Boletus edulis':
     lblresult['text'] = "It is Boletus edulis - Not dangerous and safe to eat "
  elif result == 'Cantharellus':
     lblresult['text'] = "It is Cantharellus - Not dangerous and safe to eat "
  elif result == 'Enoki mushroom':
     lblresult['text']= "It is Enoki Mushroom - Not dangerous and safe to eat"
  elif result == 'Russula mariae':
     lblresult['text'] = "It is Russula mariae - Not dangerous and safe to eat"
     

root = tk.Tk()
root.title("Mushroom Classification")

img_path = StringVar()


#Frame 1
canvas = tk.Canvas(root, height='650', width='800', bg="#8EA248")
canvas.pack(fill=BOTH, expand=YES)

frame0 =tk.Frame(root, bg="#C69C76", bd="10")
frame0.place(relwidth=0.85,relheight=0.09,relx=0.5,rely=0.15, anchor='n')

lbltitle = tk.Label(frame0, text="MUSHROOM CLASSIFICATION", font=('Eras Bold ITC', 20, 'bold'), bg='#9D6C47')
lbltitle.pack()

frame1 =tk.Frame(root, bg="#C69C76", bd="10")
frame1.place(relwidth=0.85,relheight=0.09,relx=0.5,rely=0.05, anchor='n')

textbox1 = tk.Entry(frame1, font=('Courier New', 10), textvariable=img_path)
textbox1.place(relwidth=0.65, relheight=1)

#button browse
browse = tk.Button(frame1, text = "BROWSE", bg = '#E8E8E8', font = ('Arial', 10, 'bold'), command=browse_button)
browse.place(relx = 0.7, relwidth = 0.3, relheight=1 )

#Frame 2
frame2 =tk.Frame(root, bg="#D5DEB7", bd="10")
frame2.place(relwidth=0.8,relheight=0.45,relx=0.5,rely=0.30, anchor='n')

myvar=Label(frame2)
myvar.pack()

#Frame 3
frame3 =tk.Frame(root, bg="#E8E8E8", bd="10")
frame3.place(relwidth=0.6,relheight=0.1,relx=0.5,rely=0.8, anchor='n')

lblresult = tk.Label(frame3, font=('Courier New', 10, 'bold'), bg='#E8E8E8')
lblresult.pack()

root.mainloop()
