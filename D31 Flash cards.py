from tkinter import *
import pandas as pd

data = pd.read_csv("D31_spanish_words_cut.csv")
print(data)
to_learn = data.to_dict()
print(to_learn)

BACKGROUND_COLOR = "#B1DDC6"

# tkinter window stuff
 
#my_image = PhotoImage("image_file.png")
#button = Button(image=my_image, highlightthickness=0)

 
