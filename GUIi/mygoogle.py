from tkinter import *
import wikipedia

# print (wikipedia.summary("Wikipedia"))

def search():
    val=entry.get()
    print(val)
    Tex.delete(1.0, END)

    try:
        # ans = wikipedia.summary(entry)
        ans=wikipedia.summary(val)
        # print(ans)
        Tex.insert(INSERT, ans)
    except:
        Tex.insert(INSERT, "please check your connection")




root=Tk()
root.geometry("500x500")
root.wm_iconbitmap("pyy.ico")
root.title("MY-GOOGLE")
root.resizable(0,0)

f1=Frame(root)
f1.pack()

entry=Entry(f1,width=30,font="lucida 25",border=8)
entry.pack(padx=30,pady=30)
btn=Button(f1,text="Search",font="lucida 15",command=search)
btn.pack()


Tex=Text(root,font="lucida 17",padx=12,wrap=WORD)
Tex.pack(expand=True,fill="both",pady=25,padx=25)

scroll=Scrollbar(Tex)
scroll.pack(side=RIGHT,fill=Y)
scroll.config(command=Tex.yview)
Tex.config(yscrollcommand=scroll.set)








root.mainloop()