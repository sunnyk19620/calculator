from tkinter import *

def click(event):
         global scvalue
        #  event.widget gives us that button where the user clicked.
        #  and .cget gives us the text from which we extract text form button.
         text=event.widget.cget("text")
         print(text)
         if text=="=":
                 if scvalue.get().isdigit():
                         value=int(scvalue.get())
                 else:
                    try:  
                        value=eval(screen.get())

                    except Exception  as e:
                            print(e)
                            value="Error"
          
                 scvalue.set(value)
                 screen.update()      
         elif text=="c":
                 scvalue.set("")
                 screen.update()
         else:
                 scvalue.set(scvalue.get()+text)
                 screen.update()

                 
root=Tk()
root.geometry("644x900")
root.title("GUI Calculator")

# sereen for calculator
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)


# frame for pack the buttons
frame=Frame(root,bg="grey")
button=Button(frame,text="9",padx=28,pady=18,font="lucida 20 bold")
button.pack(side=LEFT,padx=18,pady=5)
button.bind("<Button-1>",click)

button=Button(frame,text="8",padx=28,pady=18,font="lucida 20 bold")
button.pack(side=LEFT,padx=18,pady=5)
button.bind("<Button-1>",click)

button=Button(frame,text="7",padx=28,pady=18,font="lucida 20 bold")
button.pack(side=LEFT,padx=18,pady=5)
button.bind("<Button-1>",click)
frame.pack()



frame=Frame(root,bg="grey")
button=Button(frame,text="6",padx=28,pady=18,font="lucida 20 bold")
button.pack(side=LEFT,padx=18,pady=5)
button.bind("<Button-1>",click)

button=Button(frame,text="5",padx=28,pady=18,font="lucida 20 bold")
button.pack(side=LEFT,padx=18,pady=5)
button.bind("<Button-1>",click)

button=Button(frame,text="4",padx=28,pady=18,font="lucida 20 bold")
button.pack(side=LEFT,padx=18,pady=5)
button.bind("<Button-1>",click)
frame.pack()



frame=Frame(root,bg="grey")
button=Button(frame,text="3",padx=28,pady=18,font="lucida 20 bold")
button.pack(side=LEFT,padx=18,pady=5)
button.bind("<Button-1>",click)

button=Button(frame,text="2",padx=28,pady=18,font="lucida 20 bold")
button.pack(side=LEFT,padx=18,pady=5)
button.bind("<Button-1>",click)

button=Button(frame,text="1",padx=28,pady=18,font="lucida 20 bold")
button.pack(side=LEFT,padx=18,pady=5)
button.bind("<Button-1>",click)
frame.pack()



frame=Frame(root,bg="grey")
button=Button(frame,text="0",padx=29,pady=18,font="lucida 22 bold")
button.pack(side=LEFT,padx=18,pady=5)
button.bind("<Button-1>",click)

button=Button(frame,text="+",padx=29,pady=18,font="lucida 19 bold")
button.pack(side=LEFT,padx=18,pady=5)
button.bind("<Button-1>",click)

button=Button(frame,text="-",padx=29,pady=18,font="lucida 22 bold")
button.pack(side=LEFT,padx=18,pady=5)
button.bind("<Button-1>",click)
frame.pack()



frame=Frame(root,bg="grey")
button=Button(frame,text="*",padx=30,pady=18,font="lucida 20 bold")
button.pack(side=LEFT,padx=18,pady=5)
button.bind("<Button-1>",click)

button=Button(frame,text="/",padx=30,pady=18,font="lucida 20 bold")
button.pack(side=LEFT,padx=18,pady=5)
button.bind("<Button-1>",click)

button=Button(frame,text="=",padx=30,pady=18,font="lucida 20 bold")
button.pack(side=LEFT,padx=18,pady=5)
button.bind("<Button-1>",click)
frame.pack()

frame=Frame(root,bg="grey")
button=Button(frame,text="c",padx=28,pady=18,font="lucida 20 bold")
button.pack(side=LEFT,padx=18,pady=5)
button.bind("<Button-1>",click)
frame.pack()



root.mainloop()