from tkinter import *
from PIL import Image, ImageTk

root= Tk()
root.title("Python: Simple Image Viewer")

width = 700
height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = screen_width/2 - width/2
y = screen_height/2 - height/2

root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0,0)

#create the main function

def DisplayImage(event = None):
    Home = Toplevel()
    Home.title("Simple Image Viewer/Viewer")
    width = 700
    height = 500
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = screen_width/2 - width/2
    y = screen_height/2 - height/2
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home.resizable(0,0)
    load = Image.open('images/flower.jpg')
    load = load.resize((width, height), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)
    panel = Label(Home, image = render)
    panel.image = render
    panel.pack(fill = BOTH, expand = YES)



    ##################################################################################



    Top = Frame(root, width = 600, bd = 1, relief = SOLID)
    Top.pack(side = TOP)
    Mid = Frame(root, width = 300, height = 200, bd =1, relief = SOLID)
    Mid.pack_propagate(0)
    Mid.pack(pady = 20)


    ########################--------LABEL WIDGETS---------###################


    lbl_title = Label(Top, text = "Python Image Viewer")
    lbl_title.pack(fill = X)
    lbl_text = Label(Mid, text = "flower.jpg", font = ("arial", 20))
    lbl_text.bind("<Button-1>", DisplayImage)
    lbl_text.pack()



    ##########-------INITIALIZATION---------#####
    if __name__ == '__main__':
        root.mainloop()


root.mainloop()

















































