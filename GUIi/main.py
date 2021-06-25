from tkinter import *


history = []
def click(event):
    ll = ['+', '-', '/', '//', '.']
    global scvalue







    text = event.widget.cget("text")
    # print(text)

    if text=="=":
        cont = scvalue.get()
        history.append(cont)
        history.reverse()
        # print(history)
        status.configure(text="History:  "+' | '.join(history[0:4]),font="lucida 10 bold",padx=10,pady=10)

        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                # print(e)
                value = "Error"

        scvalue.set(value)
        screen.update()



    elif text=="c":
        scvalue.set("")
        screen.update()
    elif text=="del":
        leng=len(screen.get())
        # print(leng)
        screen.delete(leng-1,END)
        screen.update()





    else:
        tot=scvalue.get()
        # print(tot)
        last=tot[-1:]
        # slast = tot[-2:-1]
        # print(slast,last)
        # print(last)
        # print(text)
        if   last  in ll and not text.isdigit():
            pass
        else:
            scvalue.set(scvalue.get() + text)
            screen.update()












root =Tk()
root.geometry("300x500")
root.title("Calculator")
root.resizable(0,0)

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 20 bold",bg="black",fg="white")
screen.pack(expand=True,fill="both", pady=10, padx=10)



row1=Frame(root)

btn1 = Button(row1, text="1", font="verdana 16 bold")
btn1.pack(side=LEFT, expand=True, fill="both")
btn1.bind("<Button-1>", click)

btn2 = Button(row1, text="2", font="verdana 16 bold")
btn2.pack(side=LEFT, expand=True, fill="both")
btn2.bind("<Button-1>", click)

btn3= Button(row1, text="3", font="verdana 16 bold")
btn3.pack(side=LEFT, expand=True, fill="both")
btn3.bind("<Button-1>", click)

btn4= Button(row1, text="+", font="verdana 16 bold")
btn4.pack(side=LEFT, expand=True, fill="both")
btn4.bind("<Button-1>", click)

row1.pack(expand=True,fill="both")




row2=Frame(root)

btn1 = Button(row2, text="4", font="verdana 16 bold")
btn1.pack(side=LEFT, expand=True, fill="both")
btn1.bind("<Button-1>", click)

btn2 = Button(row2, text="5", font="verdana 16 bold")
btn2.pack(side=LEFT, expand=True, fill="both")
btn2.bind("<Button-1>", click)

btn3= Button(row2, text="6", font="verdana 16 bold")
btn3.pack(side=LEFT, expand=True, fill="both")
btn3.bind("<Button-1>", click)

btn4= Button(row2, text="-", font="verdana 16 bold")
btn4.pack(side=LEFT, expand=True, fill="both")
btn4.bind("<Button-1>", click)

row2.pack(expand=True,fill="both")


row3=Frame(root)

btn1 = Button(row3, text="7", font="verdana 16 bold")
btn1.pack(side=LEFT, expand=True, fill="both")
btn1.bind("<Button-1>", click)

btn2 = Button(row3, text="8", font="verdana 16 bold")
btn2.pack(side=LEFT, expand=True, fill="both")
btn2.bind("<Button-1>", click)

btn3= Button(row3, text="9", font="verdana 16 bold")
btn3.pack(side=LEFT, expand=True, fill="both")
btn3.bind("<Button-1>", click)

btn4= Button(row3, text="*", font="verdana 16 bold")
btn4.pack(side=LEFT, expand=True, fill="both")
btn4.bind("<Button-1>", click)



row3.pack(expand=True,fill="both")


row4=Frame(root)

btn1 = Button(row4, text="0", font="verdana 16 bold")
btn1.pack(side=LEFT, expand=True, fill="both")
btn1.bind("<Button-1>", click)

btn2 = Button(row4, text="c", font="verdana 16 bold")
btn2.pack(side=LEFT, expand=True, fill="both")
btn2.bind("<Button-1>", click)

btn3= Button(row4, text="=", font="verdana 16 bold")
btn3.pack(side=LEFT, expand=True, fill="both")
btn3.bind("<Button-1>", click)

btn4= Button(row4, text="/", font="verdana 16 bold")
btn4.pack(side=LEFT, expand=True, fill="both")
btn4.bind("<Button-1>", click)

row4.pack(expand=True,fill="both")




row5=Frame(root)

btn1 = Button(row5, text="00", font="verdana 16 bold")
btn1.pack(side=LEFT, expand=True, fill="both")
btn1.bind("<Button-1>", click)

btn2 = Button(row5, text="del", font="verdana 16 bold")
btn2.pack(side=LEFT, expand=True, fill="both")
btn2.bind("<Button-1>", click)

btn3= Button(row5, text=".", font="verdana 16 bold")
btn3.pack(side=LEFT, expand=True, fill="both")
btn3.bind("<Button-1>", click)

btn4= Button(row5, text="//", font="verdana 16 bold")
btn4.pack(side=LEFT, expand=True, fill="both")
btn4.bind("<Button-1>", click)

row5.pack(expand=True,fill="both")


row6=Frame(root)
status=Label(root,text="History: ",font="lucida 10 bold")
status.pack(side=LEFT)

row6.pack(expand=True,fill="both")








root.mainloop()