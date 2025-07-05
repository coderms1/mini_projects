<<<<<<< HEAD
# 01_framesButtons.py

# mini window / frame project
# coder: matty sim
# subject: frames

## >> What is a Frame?
## >> a FRAME is a container (rectangle) that groups/holds widgets

from tkinter import *

window = Tk()

frame = Frame(window,bg="pink",bd=5,relief=SUNKEN)
frame.place(x=100,y=100)

Button(frame, text="W",font=("Consolas",25),width=3).pack(side=TOP)
Button(frame, text="A",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame, text="S",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame, text="D",font=("Consolas",25),width=3).pack(side=LEFT)


=======
# 01_framesButtons.py

# mini window / frame project
# coder: matty sim
# subject: frames

## >> What is a Frame?
## >> a FRAME is a container (rectangle) that groups/holds widgets

from tkinter import *

window = Tk()

frame = Frame(window,bg="pink",bd=5,relief=SUNKEN)
frame.place(x=100,y=100)

Button(frame, text="W",font=("Consolas",25),width=3).pack(side=TOP)
Button(frame, text="A",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame, text="S",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame, text="D",font=("Consolas",25),width=3).pack(side=LEFT)


>>>>>>> bc16a2cb0614200f98071b2fb1d6b09d52237b6f
window.mainloop()