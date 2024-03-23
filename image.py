from tkinter import *

def on_image_click():
    print("Image clicked")

# Create Tkinter window
root = Tk()
root.title("Image Button Example")

# Load the image
image = PhotoImage(file="assets/plus.png").subsample(4, 4)
 # Replace "button_image.png" with your image file path

# Create a label widget to display the image
image_label = Label(root, image=image)
image_label.place(x=400,y=300)

# Bind a click event to the image label
image_label.bind("<Button-1>", lambda event: on_image_click())

# Run Tkinter event loop
root.mainloop()
